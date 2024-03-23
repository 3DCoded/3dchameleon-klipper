# 3dchameleon-klipper
### A highly configurable klipper extras module and configuration for the 3DChameleon
**NOTE: The limit switch should be connected to the Raspberry Pi running Klipper and the Chameleon via a relay**
It currently supports these commands:
- `PULSE_CHAMELEON PULSES=x`
- `PRESS_CHAMELEON DURATION=x` (seconds)
- `QUERY_CHAMELEON_SENSOR` This is used to make sure that the chameleon can properly read your filament sensor
- `LOAD_CHAMELEON` This will utilize the filament sensor to load the filament
- `UNLOAD_CHAMELEON` This will utilize the filament sensor to unload the filament
- `SET_CHAMELEON VAULE=x` This will set the 3DChameleon pin to 1 or 0

and these configuration options:
- `filament_sensor_name` (defualt `fsensor`)
- `filament_sensor_type` (default `filament_switch_sensor`)
- `pin` (default `3dchameleon`)
- `unload_time` How long to unload the filament after the filament sensor reads 0
- `max_unload_time` The maximum time attempting to unload without the filament sensor reading 0
- `load_time` How long to laod the filament after the filament sensor reads 1
- `max_load_time` The maximum time attempting to load without the filament sensor reading 1

The unload procedure is as follows:
1. Unload filament until the filament sensor reads 0
2. Unload filament `unload_distance`
3. If filament sensor hasn't read 0 for `max_unload_time`, then pause for the user

The load procedure is as follows:
1. Load filament until the filament sensor reads 1
2. Load filament `load_distance`
3. If filament sensor hasn't read 1 for `max_load_time`, then pause for the user

