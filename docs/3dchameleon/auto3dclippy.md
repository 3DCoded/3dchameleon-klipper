# Auto3DClippy

The Auto3DClippy is the 3DChameleon's filament cutter designed for the MK4 Pro. It works by having a servo attached to a knife blade, and by moving the servo, it can cut the filament cleanly. It is controlled with the 3DChameleon via three pins. 

## Wiring

### Method 1

Use this method if you have a metal horn on your servo and/or want a cleaner wiring solution.

See [this post](https://www.3dchameleon.com/forum/main/comment/7a6f24b5-c81b-4a33-8065-4de228b41ace?postId=664bca7465d05500108fcb85) on the 3DChameleon forums.

### Method 2

Use this method if you're using an Auto3D**K**lippy, or if you already have the parts required for this method.

Wiring guide is available [here](https://www.tinkercad.com/things/bkdLnYCJRPw-auto3dclippy-wiring). The relevant 3DChameleon forum post is [here](https://www.3dchameleon.com/forum/getting-started/auto3dclippy-wiring).

## Recommendations

- Servo extension cable: [Amazon](https://a.co/d/39kKTmJ)
- Metal servo horn: [Amazon](https://a.co/d/e8D5AjG)

    NOTE that the metal servo horn requires a different Auto3DClippy design. See [this post](https://www.3dchameleon.com/forum/main/comment/7a6f24b5-c81b-4a33-8065-4de228b41ace?postId=664bca7465d05500108fcb85) for details.

## Configuration

This feature is only available in the [`dev`](https://github.com/3DCoded/3dchameleon-klipper/tree/dev) branch, as it is still experimental. To configure it, just add:

```
clippy: true
clippy_distance: 40
```

to your `[3dchameleon]` section in your `3dchameleon.cfg`. `clippy_distance` is detailed in [Configuration](configuration.md)