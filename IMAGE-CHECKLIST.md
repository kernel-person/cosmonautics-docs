# Image checklist

Add finished public screenshots to `docs/images/`. Capture real gameplay from the release candidate with the normal player HUD hidden where practical.

## Captured

- `artemis-launch-site.jpg`
- `space-program-advancements.png`
- `moon-earth.jpg`
- `station-eva.jpg`
- `moon-catacomb-entrance.jpg`
- `moon-base-pressure-gauge.jpg`
- `lunar-alloy-crafting.png`
- `lunar-alloy-brewing-poster.jpg`
- `lunar-rover-driving-poster.jpg`
- `lunar-rover-driving.gif` (marketplace driving loop)

Recommended framing:

1. Artemis: completed rocket and enough of the 10 × 10 pad to explain the site.
2. Moon: Earth visible above the lander or a finished habitat.
3. Advancements: the full Space Program tree at a readable GUI scale.
4. Survival: complete suit, Pressure Gauge in hand, sealed room visible.
5. Station: planet display, zero-gravity pose, RCS effect, and visible harness tether.
6. Catacomb: a distinctive corridor, laboratory, or loot room rather than a dark generic tunnel.

The core player-facing screenshot set is complete. Add future captures only when they explain a new released feature or materially improve an existing guide.

The two Cosmonautics branding images already in that directory are approved exports from the plugin repository.

## Gameplay recordings

User-supplied recordings captured on 17 October 2026:

- `docs/videos/lunar-alloy-brewing.mp4`: close crop of the powered brewing GUI, at native speed. Only the final capture-controls tail was removed.
- `docs/videos/lunar-rover-driving.mp4`: square crop retaining placement, refuelling, and the full drive, at native speed.
- `docs/images/lunar-rover-driving.gif`: a short looping excerpt of the driving portion for marketplace descriptions.

The wiki embeds MP4s with playback controls and matching posters. The crafting screenshot shows the shapeless two-Solution, two-iron recipe; its displayed arrangement is an example.

## Rendered crafting recipes

`docs/images/recipes/` contains the Solo Rover, Duo Rover, Lunar Alloy, Copper Gun, Rocket Launcher, and Homing Rocket Ammo diagrams. These are generated from the real GUI, vanilla textures, and custom head skins; they are not gameplay captures. See `tools/recipe-renderer/README.md` for provenance and regeneration.

Check the shaped rover slots, custom item identities, gray Solution tint, and four-ammo result count whenever regenerating. Shapeless recipes show one possible arrangement and must stay labelled as shapeless in the wiki.
