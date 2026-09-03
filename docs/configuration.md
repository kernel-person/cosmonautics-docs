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
- Station thrusters and personal docks
- Rocket countdowns, structure consumption, and fuel costs
- Crafting recipe availability

Invalid bounded numeric values are clamped and reported during startup. Duplicate or unsafe world names are refused when they could endanger world data.

## Production safety

Keep `debug.enabled: false` on production servers. It unlocks development laboratories, authoring tools, world regeneration, and unfinished destinations and is not needed for normal gameplay or administration.

## License activation

BuiltByBit buyer downloads contain a license key. Direct licenses may set `license-key` or store the key alone in `plugins/SpacePlugin/license.key`; the file is used only when the configuration value is blank. Startup activation fails closed after a ten-second network timeout. Later heartbeat failures produce warnings but do not stop a running server.

