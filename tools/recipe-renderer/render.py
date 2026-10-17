#!/usr/bin/env python3
"""Render the six documented recipes from checked-in Minecraft 26.2 assets."""
import argparse
from collections import Counter
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
WIKI = ROOT.parent.parent
SCALE = 3
SIZE = (176, 82)


def read_json(path):
    return json.loads((ROOT / path).read_text())


@lru_cache(maxsize=None)
def texture(path):
    return Image.open(ROOT / path).convert('RGBA')


def vanilla(path):
    return texture('assets/minecraft/' + path)


def glyph(char):
    # The official ASCII provider uses the code-point-indexed 16 x 16 atlas.
    atlas = vanilla('textures/font/ascii.png')
    n = ord(char)
    image = atlas.crop(((n % 16) * 8, (n // 16) * 8,
                        (n % 16 + 1) * 8, (n // 16 + 1) * 8))
    bounds = image.getchannel('A').getbbox()
    return image, bounds[2] if bounds else 3


def text_width(value):
    return sum(glyph(char)[1] + 1 for char in value)


def draw_text(image, value, x, y, color, shadow=False):
    if shadow:
        draw_text(image, value, x + 1, y + 1,
                  tuple(channel // 4 for channel in color))
    for char in value:
        bitmap, width = glyph(char)
        ink = Image.new('RGBA', bitmap.size, (*color, 255))
        ink.putalpha(bitmap.getchannel('A'))
        image.alpha_composite(ink.resize((24, 24), Image.Resampling.NEAREST),
                              (x * SCALE, y * SCALE))
        x += width + 1


def rotate(point, angles):
    """Minecraft ItemTransform.rotationXYZ: R_x * R_y * R_z."""
    x, y, z = point
    rx, ry, rz = map(math.radians, angles)
    x, y = x * math.cos(rz) - y * math.sin(rz), x * math.sin(rz) + y * math.cos(rz)
    x, z = x * math.cos(ry) + z * math.sin(ry), -x * math.sin(ry) + z * math.cos(ry)
    y, z = y * math.cos(rx) - z * math.sin(rx), y * math.sin(rx) + z * math.cos(rx)
    return x, y, z


def face(image, bitmap, vertices, brightness):
    """Nearest-texel orthographic rasterization of one planar cuboid face."""
    origin, right, _, bottom = vertices
    ax, ay = right[0] - origin[0], right[1] - origin[1]
    bx, by = bottom[0] - origin[0], bottom[1] - origin[1]
    determinant = ax * by - ay * bx
    layer = Image.new('RGBA', image.size)
    for y in range(max(0, math.floor(min(v[1] for v in vertices))),
                   min(image.height, math.ceil(max(v[1] for v in vertices)))):
        for x in range(max(0, math.floor(min(v[0] for v in vertices))),
                       min(image.width, math.ceil(max(v[0] for v in vertices)))):
            dx, dy = x + .5 - origin[0], y + .5 - origin[1]
            u = (dx * by - dy * bx) / determinant
            v = (ax * dy - ay * dx) / determinant
            if 0 <= u < 1 and 0 <= v < 1:
                r, g, b, a = bitmap.getpixel((int(u * bitmap.width), int(v * bitmap.height)))
                layer.putpixel((x, y), (round(r * brightness), round(g * brightness),
                                        round(b * brightness), a))
    image.alpha_composite(layer)


def head_faces(half):
    # Converted from the native SkullModel's -4..4, -8..0, -4..4 box,
    # after the player_head special model's 180-degree X rotation.
    h = half
    return {
        'top': [(-h, h, -h), (h, h, -h), (h, h, h), (-h, h, h)],
        'right': [(-h, h, -h), (-h, h, h), (-h, -h, h), (-h, -h, -h)],
        'front': [(-h, h, h), (h, h, h), (h, -h, h), (-h, -h, h)],
    }


def projected(vertices, display, center_offset=(0, 0, 0)):
    result = []
    for vertex in vertices:
        scaled = tuple((v + offset) * scale for v, offset, scale in
                       zip(vertex, center_offset, display['scale']))
        x, y, z = rotate(scaled, display['rotation'])
        tx, ty, tz = display['translation']
        result.append(((8 + x + tx) * SCALE, (8 - y - ty) * SCALE, z + tz))
    return result


@lru_cache(maxsize=None)
def render_head(path):
    skin = texture(path)
    display = read_json('assets/minecraft/models/item/template_skull.json')['display']['gui']
    icon = Image.new('RGBA', (16 * SCALE, 16 * SCALE))
    # UVs in the 64 x 64 player skin; the second layer is inflated by .25
    # model units per side, exactly as SkullModel.createHumanoidHeadLayer.
    crops = {'top': (8, 0, 16, 8), 'right': (0, 8, 8, 16), 'front': (8, 8, 16, 16)}
    for half, uv_offset in [(4, 0), (4.25, 32)]:
        for name, vertices in head_faces(half).items():
            box = crops[name]
            box = (box[0] + uv_offset, box[1], box[2] + uv_offset, box[3])
            # The head center sits four model units below the block center;
            # native GUI translation [0,3,0] raises it into the item slot.
            face(icon, skin.crop(box), projected(vertices, display, (0, -4, 0)),
                 {'top': 1.0, 'right': .80, 'front': .92}[name])
    return icon


@lru_cache(maxsize=None)
def render_block(name):
    display = read_json('assets/minecraft/models/block/block.json')['display']['gui']
    icon = Image.new('RGBA', (16 * SCALE, 16 * SCALE))
    # Native block rotation [30,225,0] exposes up, east and north.
    h = 8
    vertices = {
        'top': [(h, h, h), (-h, h, h), (-h, h, -h), (h, h, -h)],
        'side': [(h, h, h), (h, h, -h), (h, -h, -h), (h, -h, h)],
        'front': [(h, h, -h), (-h, h, -h), (-h, -h, -h), (h, -h, -h)],
    }
    observer = read_json('assets/minecraft/models/block/observer.json')
    for side, points in vertices.items():
        if name == 'blackstone':
            path = 'blackstone_top' if side == 'top' else 'blackstone'
        else:
            path = observer['textures'][side].removeprefix('block/')
        bitmap = vanilla('textures/block/' + path + '.png')
        if side == 'top':
            # The top model UV is [0,16,16,0]. The above vertex order also
            # reverses X, so this is a horizontal flip for the observer.
            bitmap = bitmap.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        face(icon, bitmap, projected(points, display),
             {'top': 1.0, 'side': .80, 'front': .92}[side])
    return icon


@lru_cache(maxsize=None)
def item_icon(item):
    definition = read_json('recipes.json')['items'][item]
    kind = definition['kind']
    if kind == 'head':
        return render_head(definition['skin'])
    if kind == 'block':
        return render_block(definition['block'])
    if kind == 'potion':
        icon = vanilla('textures/item/potion_overlay.png').copy()
        tint = definition['tint']
        channels = icon.split()
        icon = Image.merge('RGBA', tuple(channel.point(lambda value, t=t: round(value * t / 255))
                                         for channel, t in zip(channels[:3], tint)) + (channels[3],))
        icon.alpha_composite(vanilla('textures/item/potion.png'))
    else:
        icon = texture(definition['texture'])
    return icon.resize((16 * SCALE, 16 * SCALE), Image.Resampling.NEAREST)


def background():
    native = vanilla('textures/gui/container/crafting_table.png')
    # Preserve the original top/side borders and transplant the bottom four
    # rows. Inventory slots start at y=83 and are deliberately excluded.
    panel = native.crop((0, 0, SIZE[0], SIZE[1]))
    panel.paste(native.crop((0, 162, SIZE[0], 166)), (0, SIZE[1] - 4))
    image = panel.resize((SIZE[0] * SCALE, SIZE[1] * SCALE), Image.Resampling.NEAREST)
    draw_text(image, 'Crafting', 28, 6, (64, 64, 64))
    return image


def render_recipe(recipe):
    image = background()
    for index, item in enumerate(recipe['slots']):
        if item:
            image.alpha_composite(item_icon(item),
                                  ((30 + index % 3 * 18) * SCALE, (17 + index // 3 * 18) * SCALE))
    image.alpha_composite(item_icon(recipe['result']['item']), (124 * SCALE, 35 * SCALE))
    count = recipe['result']['count']
    if count > 1:
        value = str(count)
        draw_text(image, value, 124 + 17 - text_width(value), 35 + 9,
                  (255, 255, 255), shadow=True)
    return image


def validate_inputs():
    provenance = read_json('assets.json')
    paths = {entry['path'] for entry in provenance['assets']}
    actual = {str(path.relative_to(ROOT)) for path in (ROOT / 'assets').rglob('*') if path.is_file()}
    assert paths == actual, 'Source asset inventory is incomplete'
    for entry in provenance['assets']:
        assert hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest() == entry['sha256'], entry['path']
    recipes = read_json('recipes.json')
    expected = {
        'lunar-rover-solo.png': {'copper-ingot': 2, 'saddle': 1, 'iron-ingot': 2, 'lunar-alloy': 1, 'blackstone': 2},
        'lunar-rover-duo.png': {'copper-ingot': 1, 'saddle': 2, 'iron-ingot': 2, 'lunar-alloy': 1, 'blackstone': 2},
        'lunar-alloy.png': {'iron-ingot': 2, 'lunar-alloy-solution': 2},
        'copper-gun.png': {'copper-horse-armor': 1, 'spyglass': 1, 'crossbow': 1, 'lunar-alloy': 1},
        'rocket-launcher.png': {'iron-horse-armor': 1, 'observer': 1, 'crossbow': 1, 'lunar-alloy': 1},
        'homing-rocket-ammo.png': {'rocket-fuel': 1, 'oxidizer': 1, 'iron-ingot': 1},
    }
    assert {r['file'] for r in recipes['recipes']} == set(expected)
    for recipe in recipes['recipes']:
        assert len(recipe['slots']) == 9, recipe['file']
        assert Counter(item for item in recipe['slots'] if item) == expected[recipe['file']], recipe['file']
        if recipe['type'] == 'shaped':
            first_row = ['copper-ingot', 'saddle', 'copper-ingot'] if recipe['file'] == 'lunar-rover-solo.png' else ['saddle', 'copper-ingot', 'saddle']
            assert recipe['slots'] == first_row + ['iron-ingot', 'lunar-alloy', 'iron-ingot', 'blackstone', None, 'blackstone']
        assert all(item is None or item in recipes['items'] for item in recipe['slots'])
        assert recipe['result']['item'] in recipes['items']
        assert recipe['result']['count'] == (4 if recipe['file'] == 'homing-rocket-ammo.png' else 1)
    for definition in recipes['items'].values():
        for key in ['texture', 'skin']:
            if key in definition:
                assert definition[key] in paths, 'Untracked asset reference'
        if definition['kind'] == 'head':
            assert texture(definition['skin']).size == (64, 64)
            for box in [(8, 0, 16, 8), (0, 8, 8, 16), (8, 8, 16, 16)]:
                assert texture(definition['skin']).crop(box).getchannel('A').getextrema() == (255, 255)
    assert recipes['items']['lunar-alloy-solution']['tint'] == [128, 128, 128]
    font = read_json('assets/minecraft/font/include/default.json')
    provider = next(p for p in font['providers'] if p.get('file') == 'minecraft:font/ascii.png')
    for char in 'Crafting4':
        assert provider['chars'][ord(char) // 16][ord(char) % 16] == char
    return recipes['recipes']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=WIKI / 'docs/images/recipes')
    args = parser.parse_args()
    recipes = validate_inputs()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for recipe in recipes:
        image = render_recipe(recipe)
        image.save(args.output_dir / recipe['file'], optimize=False, compress_level=9)
        print(recipe['file'], f'{image.width}x{image.height}')


if __name__ == '__main__':
    main()
