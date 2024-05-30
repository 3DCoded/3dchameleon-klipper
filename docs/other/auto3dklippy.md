# Auto3DKlippy

The Auto3DKlippy (with a K) is a Klipperized Auto3DClippy implementation. It uses the same cutter mechanism, but is controlled via an Arduino, instead of the 3DChameleon's electronics. It is still only lightly tested and only recommended for advanced users.

## Note

Many of the tips shared in [Auto3DClippy](auto3dclippy.md) can be applied to the Auto3DKlippy

## Wiring

See [Auto3DClippy](auto3dclippy.md#wiring) for wiring details.

After that, a few changes need to be made. 

1. The Signal and GND wires need to be connected to an Arduino (In my case an Arduino Nano on a breadboard)
2. Plug the Arduino into your Raspberry Pi
3. Follow [this guide](https://www.klipper3d.org/Installation.html#building-and-flashing-the-micro-controller) to flash Klipper firmware onto your Arduino
4. Follow [this guide](https://www.klipper3d.org/Installation.html#configuring-klipper) to configure it as a Klipper MCU
    Make sure the MCU is called `arduino`. To do this, replace `[mcu]` with `[mcu arduino]`

## Configuration

The configuration for the Auto3DKlippy is available in the [`dev`](https://github.com/3DCoded/3dchameleon-klipper/tree/dev) branch. The relevant sections in `3dchameleon.cfg` are:

```
[mcu arduino]
serial: /dev/serial/your-arduino-id

[servo clippy]
pin: arduino: PD5
```

and

```
# Macros for Auto3DClippy:
[gcode_macro Clippy_Cut]
gcode:
  SET_SERVO SERVO=clippy ANGLE=0

[gcode_macro Clippy_Release]
gcode:
  SET_SERVO SERVO=clippy ANGLE=90

[gcode_macro Clippy_Run]
gcode:
  Clippy_Cut
  G4 P250
  Clippy_Release
```

Implementation in the `Toolchange` macro is still in development. To run the Auto3DKlippy, `Clippy_Run` will cut, wait 250ms, then release.