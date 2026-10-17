# Permissions

Cosmonautics keeps ordinary player commands broadly available while separating administrative and development capabilities.

| Permission | Default | Purpose |
| --- | --- | --- |
| `spaceplugin.tutorial` | Everyone | View private client-side tutorials. |
| `spaceplugin.soyuz.launch` | Everyone | Board and launch Soyuz passenger transports. |
| `spaceplugin.sputnik.launch` | Everyone | Target and launch Sputnik reconnaissance rockets. |
| `spaceplugin.admin` | Operators | Reload, diagnostics, and protected administration. |
| `spaceplugin.station.admin` | Operators | Station archive administration; included by `spaceplugin.admin`. |
| `spaceplugin.give` | Operators | Give custom Cosmonautics items. |
| `spaceplugin.ballistic.launch` | Operators | Target and launch ballistic rockets. |

!!! warning "Production servers"
    Keep `debug.enabled` off in production. Administrator permissions and debug mode cannot unlock additional planets, Station voyages, Station thrusters, or solar-system Dynmap in a release build.

