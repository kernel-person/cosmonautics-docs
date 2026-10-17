# Crafting recipe images

These six static PNGs use the Minecraft Java Edition **26.2** crafting-table texture, bitmap font and item/block textures. Custom items use the exact head skins referenced by Cosmonautics. The renderer requires Python 3.10+ and Pillow; it does not launch Minecraft or require a browser, server, GPU, resource pack or network connection.

From the wiki checkout, regenerate with:

```sh
python3 tools/recipe-renderer/render.py
```

The outputs are `docs/images/recipes/{lunar-rover-solo,lunar-rover-duo,lunar-alloy,copper-gun,rocket-launcher,homing-rocket-ammo}.png`, each **528 × 246** pixels. `--output-dir PATH` can write a separate verification set. Pillow 12.3.0 was used for the checked-in images.

## Recipe and appearance sources

`recipes.json` records the nine ingredient slots, output and amount. Recipe semantics were checked against plugin commit **3029c7e6079999406df221470420ae42a9ff152a**, using `LunarRoverRecipes.java`, `LunarAlloyRecipe.java`, `CopperGunRecipe.java` and `RocketLauncherRecipes.java` under `src/main/java/ke/ric/spaceplugin/recipe/`.

Item appearance comes from `src/main/java/ke/ric/spaceplugin/item/ItemService.java` and `SpaceHeadTexture.java` at the same commit:

- Both rover variants use `SpaceHeadTexture.ROVER_ITEM`.
- Lunar Alloy, Rocket Fuel, Oxidizer and Homing Rocket Ammo use their named head textures.
- Lunar Alloy Solution uses the ordinary potion layers with the liquid tinted RGB **128, 128, 128**.
- The Copper Gun and Rocket Launcher retain ordinary copper/iron horse armor sprites; no special item model or enchantment glint is applied.
- The displayed shapeless arrangements are examples. The Lunar Alloy image has two Iron Ingots in the first row and two solution bottles in the second row. Homing Rocket Ammo produces four items.

The visible crafting panel retains the official GUI's original top and sides, with its bottom four border rows moved upward to omit the player inventory. The native label position, 18-pixel slot spacing, result slot, arrow and bitmap count are preserved. Source sprites use nearest-neighbor scaling at 3×. Three-dimensional icons are rasterized directly at the final resolution using nearest-texel sampling.

The head renderer uses the native `template_skull` GUI rotation **[30,45,0]**, translation **[0,3,0]**, scale **[1,1,1]**, and the special player-head model's 180° X rotation. The head box is 8×8×8 model units; the hat layer is inflated by **0.25** units per side. The top, front and right skin UVs and their corresponding overlay UVs are rendered separately. These values were checked against the 26.2 JAR's `PlayerHeadSpecialRenderer`, `SkullModel.createHumanoidHeadLayer`, and `ItemTransform` bytecode using `javap`, without running client code.

Blackstone and Observer use textured 16-unit cubes with the native block GUI rotation **[30,225,0]** and scale **[0.625,0.625,0.625]**. The visible top and two sides use their appropriate vanilla textures. This intentionally small CPU renderer approximates native GPU lighting with fixed per-face brightness; the PNGs are documentation renders, not client screenshots. Geometry, item identities, skin UVs, texture pixels, GUI and quantities come from the recorded sources.

## Source assets and attribution

`assets.json` records a SHA-256 checksum and original source for every bundled PNG/JSON input. Minecraft assets are from the official [26.2 client JAR](https://piston-data.mojang.com/v1/objects/2dc72797acbc1b63fc16a11c4ac393605f453754/client.jar), verified against SHA-1 **2dc72797acbc1b63fc16a11c4ac393605f453754**. Only the small textures/model/font definitions used by these recipes are retained; the client JAR is not included. The original font definition is retained for its ASCII provider; its other, unselected language providers are not renderer inputs.

Minecraft textures, GUI and font: **Mojang AB / Microsoft**. Custom skins are downloaded unchanged from their original `textures.minecraft.net` URLs recorded in `assets.json`; those exact URLs are referenced by the plugin. Individual skin authors are not identified in the plugin source. Original source PNGs/JSON are preserved without modification.

## Verification

Every regeneration checks all bundled source checksums, source asset inventory, ingredient references and quantities, rover slot positions, output amounts, head dimensions/base-face UV coverage, potion tint, and bitmap font character positions. Missing indirect inputs fail when the corresponding icon is rendered.

For the checked-in images, generation was run twice into separate directories and all six output files compared byte-for-byte. A contact sheet of all six outputs was visually inspected for item placement, head overlays, cube faces, label/arrow/borders and the ammunition count. No Minecraft client was launched.
