# Commands

The main command is `/cosmo`.

## Player commands

| Command | Purpose |
| --- | --- |
| `/cosmo guide` | Show the core progression guide. |
| `/cosmo status` | Show destination, suit, oxygen, canisters, and fuel. |
| `/cosmo planets` | Browse destinations and their release status. |
| `/cosmo route <destination>` | Show launch requirements and the next action. |
| `/cosmo launch <destination>` | Launch when route requirements are met. |
| `/cosmo return` | Show the correct return method for your location. |
| `/cosmo rocket` | Open the Earth rocket and launch-site guide. |
| `/cosmo tutorial` | Open the interactive tutorial catalog. |
| `/cosmo tutorial <tutorial-id>` | Start `launch-site`, `survive-space`, or `space-station`. |
| `/cosmo tutorial stop` | Stop your current private tutorial. |
| `/cosmo ship guide` | Show Station controller and voyage guidance. |
| `/cosmo ship status` | Show the Station ship's current state. |
| `/cosmo ship travel <destination>` | Begin a supported Station voyage. |

## Administrator commands

| Command | Purpose |
| --- | --- |
| `/cosmo give [player] <item> [count]` | Give a custom Cosmonautics item; count must be from 1 to 1,000. |
| `/cosmo diagnostics` | Show operational diagnostics. |
| `/cosmo diagnostics report` | Write a sanitized local support report. |
| `/cosmo reload` | Reload supported plugin configuration. |
| `/cosmo reload rocketdesigns` | Reload rocket definitions. |

Support reports are written under `plugins/SpacePlugin/support-reports/` and exclude inventories, player data, and raw configuration contents.

See [Interactive Tutorials](tutorials.md) for lesson contents and controls.
