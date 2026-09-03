# Permissions

Cosmonautics keeps ordinary player commands broadly available while separating administrative and development capabilities.

| Permission | Default | Purpose |
| --- | --- | --- |
| `spaceplugin.tutorial` | Everyone | View private client-side tutorials. |
| `spaceplugin.soyuz.launch` | Everyone | Board and launch Soyuz passenger transports. |
| `spaceplugin.sputnik.launch` | Everyone | Target and launch Sputnik reconnaissance rockets. |
| `spaceplugin.admin` | Operators | Reload, diagnostics, and protected administration. |
| `spaceplugin.give` | Operators | Give custom Cosmonautics items. |
| `spaceplugin.travel.debug` | Operators | Direct debug travel. |
| `spaceplugin.debug.showcase` | Operators | Run developer showcases when debug mode is enabled. |
| `spaceplugin.ballistic.launch` | Operators | Target and launch ballistic rockets. |

!!! warning "Production servers"
    Developer permissions alone do not expose development commands: `debug.enabled` must also be true. Keep that configuration switch off in production.

