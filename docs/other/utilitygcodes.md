# Utility G-Codes

3dchameleon-klipper provides several utility G-Codes to assist in controlling your Chameleon.

## Utility G-Codes

- `SET_CHAMELEON VALUE=` Sets the relay pin to `VALUE`, where `1` is on, and `0` is off
- `UNLOAD_CHAMELEON TOOL=` Unloads the Chameleon at the provided `TOOL`, described more below, This is usually only used in the `TOOLCHANGE` macro
- `LOAD_CHAMELEON` Loads the Chameleon, described more below
- `PRESS_CHAMELEON DURATION=` Presses the chameleon pin for the provided `DURATION`
- `PULSE_CHAMELEON PULSES=` Pulses the chameleon pin for the duration `PULSES * pulse_time` (`pulse_time` was set in [Configuration](configuration.md))
- `RESET_CHAMELEON` Rapidly pulses the chameleon pin twice to reset the state to be ready for a toolchange (exits the load/unload filament stage of the Chameleon)
- `TIP_SHAPING TEMP= STAGES=` Runs tip shaping using the default 3DChameleon method, then heats to `TEMP`. See below for information on `STAGES`
- `MOVE_CHAMELEON_FILAMENT TOOL= IN=` Moves the filament `TOOL` `IN` inches. Alternatively, `MM=` can be passed to move the filament `TOOL` `MM` millimeters

## Debugging/Internal Use G-Codes

- `UPDATE_CHAMELEON_SENSOR` Updates the Chameleon's filament sensors and saves the value internally
- `QUERY_CHAMELEON_SENSOR` Queries the Chameleon's filament sensors, output in the form of `[x,x,x,x,x]`, where `x=1` means filament present, and `x=0` means filament not present. This returns a list in preparation for multiple filament sensor support.

## TIP_SHAPING STAGES=

- `STAGES=1` Cool to 180, do full tip shaping, then heat to `TEMP`
- `STAGES=2` Cool to 180, then 165, do tip shaping, then heat to `TEMP`
- `STAGES=3` Cool to 180, then 165, then 155, do tip shaping, then heat to `TEMP`
- `STAGES=4` Default behavior. Cool to 180, then 165, then 155, then 150, do tip shaping, then heat to `TEMP`

**NOTE** that smaller tip shaping moves may be executed between temperature increments.


## How UNLOAD_CHAMELEON works

### WITHOUT Auto3DClippy

1. "Press" the Chameleon pin
2. Check if filament detected for `TOOL`
3. Run `UPDATE_CHAMELEON_SENSOR`
4. Check if more than `max_unload_time` has elapsed. If so, skip remaining steps and unload failed
5. Wait 0.25s with `G4 P250`

EXPERIMENTAL: Step 5 will use `G1 E-10 F2400` instead of `G4 P250` to wait 0.25s

6. Repeat steps 2-5 until filament is not detected for `TOOL`
7. Wait another `unload_time` with `G4 P` with `unload_time * 1000`
8. "Release" the Chameleon pin

### WITH Auto3DClippy (Experimental in dev branch)

1. "Press" the Chameleon pin
2. Load filament `clippy_distance` at 40mm/s
3. Wait `unload_time` with `G4 P` with `unload_time * 1000`
3. "Release" the Chameleon pin

## How LOAD_CHAMELEON works

1. "Press" the Chameleon pin
2. Check if filament detected for `TOOL`
3. Run `UPDATE_CHAMELEON_SENSOR`
4. Check if more than `max_load_time` has elapsed. If so, skip remaining steps and load failed
5. Wait 0.25s with `G4 P250`
6. Repeat steps 2-5 until filament is detected
7. Wait another `load_time` with `G4 P` with `load_time * 1000`
8. "Release" the Chameleon pin

## On Unload/Load Failed

1. "Release" the Chameleon relay pin
2. Display Unload/Load Failed with `M117`
3. Pause with `PAUSE`