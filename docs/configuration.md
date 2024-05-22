# Configuration

**Pin Configuration:**
If you **didn't** use a relay to connect your 3DChameleon to your Raspberry Pi, make sure there's a `!` in front of the `host: gpioXX` in your `[output_pin]` configuration (`3dchameleon.cfg`) 

**Filament Sensor Configuration:**
This plugin relies on temporarily disabling the filament sensor behavior. Follow these steps to setup your filaments sensor with this plugin.
1. Set `pause_on_runout: False`
2. Change your `runout_gcode` and `insert_gcode` as follows. Example:
```
runout_gcode:
    M117 Filament Runout Detected!
    PAUSE
```
Turns into:
```
runout_gcode:
    {% set saved = printer.save_variables.variables %}
    {% if saved.efsensor %}
    M117 Filament Runout Detected!
    PAUSE
    {% endif %}
```


Example:
```
[output_pin 3dchameleon]
pin: host: gpio18
```
turns into 
```
[output_pin 3dchameleon]
pin: !host: gpio18 # <-- Notice the ! in front of host
```

**Configuration Options:**

*STABLE (in main branch):*

- `filament_sensor_name`: The name of the primary filament sensor in your printer. It should be located between the chameleon's splitter and your printer's extruder.
- `filament_sensor_type`: The type of filament sensor used. Usually a `filament_switch_sensor`
- `pin`: The name of the `output_pin` the relay is connected to. See [wiring]()
- `unload_time`: The time it takes for the Chameleon to unload the filament from the filament sensor to the tubes going into the splitter. This should be just long enough to get the filament out of the way for the next filament, with ~0.5s extra as buffer.
- `max_unload_time`: The maximum amount of time the Chameleon is allowed to try to unload the filament before the filament sensor triggers. Example: `max_unload_time: 5` If the Chameleon unloads for more than 5 seconds, and the filament sensor still reads filament present, the print is paused.
- `load_time`: The time it takes for the Chameleon to load the filament from the filament sensor to the extruder, plus ~1s extra to make sure it is engaged with the extruder gears.
- `max_load_time`: The maximum time the Chameleon is allowed to try to load the filament before the filament sensor triggers. Example: `max_load_time: 5` If the Chameleon loads for more than 5 seconds, and the filament sensor doesn't read any filament present, the print is paused.
- `pulse_time`: The time it takes to pulse the Chameleon (usually 0.5)

*EXPERIMENTAL (in dev branch):*

- `clippy`: Whether or not an Auto3DClippy is used. This will impact unloading behavior as described in [Utility G-Codes](utilitygcodes.md). This can be set to `true` or `false`
- `clippy_distance`: The distance filament should be loaded after running the Auto3DClippy to pull it in enough so that the filament sensor no longer detects filament.

**Default Configuration:**
```
[3dchameleon]
clippy: false
clippy_distance: 40
filament_sensor_name: fsensor
filament_sensor_type: filament_switch_sensor
pin: 3dchameleon
unload_time: 7.5
max_unload_time: 10
load_time: 0.5
max_load_time: 10.5
pulse_time: 0.5
```