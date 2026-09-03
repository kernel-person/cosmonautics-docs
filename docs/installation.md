# Installation

## Requirements

- 64-bit Java 25
- Paper 26.2 experimental build 71
- PacketEvents 2.13.0 installed as a separate server plugin
- A valid Cosmonautics license and outbound HTTPS access to `app.lukittu.com`

Cosmonautics does not support Spigot, Folia, Purpur, Bedrock servers, proxies used as game servers, older Minecraft versions, or other Paper builds.

## Fresh installation

1. Stop Paper completely and back up the whole server directory.
2. Place PacketEvents 2.13.0 and the Cosmonautics JAR in `plugins/`.
3. Start Paper once to generate `plugins/SpacePlugin/config.yml`.
4. BuiltByBit downloads contain their license automatically. For a direct license, set `license-key` in the generated configuration or place the key alone in `plugins/SpacePlugin/license.key`.
5. Confirm the console reports a valid license and that SpacePlugin enabled for Paper 26.2.
6. Run `/cosmo diagnostics` as an operator.

The required datapack, structures, loot tables, recipes, and Artemis rocket definition are bundled in the plugin. WorldEdit and a separate resource pack are not required.

## Upgrading

Stop Paper and back up every world plus `plugins/SpacePlugin/` before replacing the JAR. Configuration migration creates a timestamped backup and adds missing defaults without overwriting configured values. Updates never regenerate or delete a world automatically.

!!! danger "Do not downgrade worlds"
    Paper 26.2 world data cannot safely be downgraded. Restore the matching complete server backup if an older Paper or Cosmonautics version must be recovered.

## Removing Cosmonautics

Stop Paper normally before removing the JAR. Keep `plugins/SpacePlugin/` if you may reinstall the plugin; delete it only after making a backup.

