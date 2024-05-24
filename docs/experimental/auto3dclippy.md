# Auto3DClippy

The Auto3DClippy is the 3DChameleon's filament cutter designed for the MK4 Pro. It works by having a servo attached to a knife blade, and by moving the servo, it can cut the filament cleanly. It is controlled with the 3DChameleon via three pins. 

## Wiring

Wiring guide is available [here](https://www.tinkercad.com/things/bkdLnYCJRPw-auto3dclippy-wiring). The relevant 3DChameleon forum post is [here](https://www.3dchameleon.com/forum/getting-started/auto3dclippy-wiring)

## Configuration

This feature is only available in the [`dev`](https://github.com/3DCoded/3dchameleon-klipper/tree/dev) branch, as it is still experimental. To configure it, just add:

```
clippy: true
clippy_distance: 40
```

to your `[3dchameleon]` section in your `3dchameleon.cfg`. `clippy_distance` is detailed in [Configuration](configuration.md)