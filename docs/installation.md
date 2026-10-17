# Installation

## Requirements

- 64-bit Java 25
- Paper 26.2 experimental build 71
- PacketEvents 2.13.0 installed as a separate server plugin
- A personalized Cosmonautics marketplace download, a valid license, and outbound HTTPS access to the RIC licensing service

Cosmonautics does not support Spigot, Folia, Purpur, Bedrock servers, proxies used as game servers, or older Minecraft versions. Compatibility with other Paper builds is not promised.

## Fresh installation

1. Stop Paper completely and back up the whole server directory.
2. Download your personalized JAR from the marketplace where you purchased Cosmonautics. For MCModels beta.7, use `SpacePlugin-0.1.0-beta.7-mcmodels.jar` from your account's library.
3. Place PacketEvents 2.13.0 and that Cosmonautics JAR in `plugins/`.
4. Allow outbound HTTPS to the RIC licensing service, then start Paper. The personalized download activates online on first use and generates `plugins/SpacePlugin/config.yml`. If support provides a manual key, put it alone in `plugins/SpacePlugin/license.key`; that file takes precedence. Licensing is not a `config.yml` setting.
5. Confirm the console reports a valid license and that SpacePlugin enabled for Paper 26.2.
6. Run `/cosmo diagnostics` as an operator.

The required datapack, structures, loot tables, recipes, and Artemis rocket definition are bundled in the plugin. WorldEdit and a separate resource pack are not required.

RIC authentication is required at startup. After the initial online activation, later starts can validate a current cached signed lease or activate online when needed. Mid-session renewal and six-hour expiry shutdown are disabled by default after startup succeeds. Licensing is checked again at the next startup.

## Upgrading

Stop Paper and back up every world plus `plugins/SpacePlugin/` before replacing the JAR. Configuration migration creates a timestamped backup and adds missing defaults without overwriting configured values. Updates never regenerate or delete a world automatically.

Keep the complete plugin data folder, including licensing state and `rovers.dat`, which stores rover identities, ownership, fuel, and deployment state.

### Upgrading to beta.7

- Secured Moon colony loot-room chests now provide **Lunar Scrap** when their contents are first generated. Existing chests whose contents have not yet generated are eligible; already-generated contents are not refilled. No world regeneration is needed.
- Refine Scrap at a powered Station brewing stand, then craft [Lunar Alloy](moon.md#make-lunar-alloy). Existing finished Alloy remains usable in equipment recipes.
- Use `/cosmo tutorial moon-workshop` for the new lesson covering alloy, rovers, and weapons.
- Release builds keep additional planets, moving Station voyages, Station thrusters, and solar-system Dynmap unavailable. Debug mode cannot enable the expansion. When replacing a development build, saved expansion records remain stored but inactive.

The known [high-ascent rocket visibility issue](rockets.md#flight-and-staging) remains unresolved in beta.7.

!!! danger "Do not downgrade worlds"
    Paper 26.2 world data cannot safely be downgraded. Restore the matching complete server backup if an older Paper or Cosmonautics version must be recovered.

## Removing Cosmonautics

Stop Paper normally before removing the JAR. Keep `plugins/SpacePlugin/` if you may reinstall the plugin; delete it only after making a backup.

