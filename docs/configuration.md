# Configuration

Cosmonautics generates `plugins/SpacePlugin/config.yml`. Stop Paper before editing it, or apply supported changes with `/cosmo reload`. Older configurations receive a timestamped backup before migration.

## Worlds and ownership

Each destination maps to a unique world name. Its `world-modes` value determines ownership:

- `generated`: Cosmonautics owns the generator and settings.
- `existing`: another provider owns and loads the world; Cosmonautics will not create, delete, or replace it.

!!! danger "Protect imported worlds"
    Never mark an irreplaceable imported world as `generated`. Back up the server before changing world ownership.

## Gameplay settings

The main configuration groups cover:

- Gravity and zero-gravity RCS movement
- Oxygen reserves, breathing, and vacuum damage
- Sealed-room pressure, air quality, and decompression
- Planetary environmental processing
- Station power, processing, and personal docks
- Rocket countdowns, structure consumption, and fuel costs
- Crafting recipe availability

Invalid bounded numeric values are clamped and reported during startup. Duplicate or unsafe world names are refused when they could endanger world data.

## Production safety

Keep `debug.enabled: false` on production servers. It exposes support/developer tools and is not needed for normal gameplay. Release builds independently disable additional planets, moving Station voyages, Station thrusters, and solar-system Dynmap; configuration, debug mode, and administrator permissions cannot enable them.

## License activation

Licensing is not configured in `config.yml`. Use the personalized JAR from your marketplace account. It activates online through RIC on first use. If support supplies a manual key, put it alone in `plugins/SpacePlugin/license.key`; this takes precedence over the embedded marketplace activation.

RIC authentication is required at startup. Later starts can validate a current cached signed lease or activate online when needed. Mid-session renewal and six-hour expiry shutdown are disabled by default after startup succeeds; the next startup checks licensing again. Preserve the plugin-managed licensing state when backing up or moving the installation.

## Lunar progression and external worlds

The [Lunar Alloy process](moon.md#make-lunar-alloy) needs a powered Station brewing stand and Lunar Scrap from secured colony loot rooms. An external Moon retains its provider's terrain and structures, so adopting it does not generate Cosmonautics catacombs or create a Scrap supply. The server owner must provide suitable loot or another source if the provider does not supply it.

## Rovers

Beta.7 adds no rover-specific configuration settings. One Hydrogen bottle provides up to ten minutes of powered driving at normal server speed, and a full tank holds four bottles. Parked rovers use no fuel. Preserve `rovers.dat` with the rest of the plugin data. See [Lunar Rovers](rovers.md) for recipes and controls.

