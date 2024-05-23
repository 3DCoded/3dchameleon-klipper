# Load Failed

If your printer pauses during a toolchange and displays a `Load Failed` message on your printer's display, follow this guide to recover the toolchange and to diagnose the cause of the failure.

## What the error means

A `Load Failed` message means that while the Chameleon was trying to load the filament, the printer's filament sensor didn't detect filament.

## How to recover it

1. Detach the Chameleon's PTFE tube from your printer's extruder
2. Check the Klipper console to see what the next tool is. For example, if `T0 -> T1` was the most recent toolchange message in the Klipper console, your printer was trying to unload `T0` and load `T1`
3. If necessary, unload the previous filament if it is still in the way of the new filament.
4. Load in the corresponding filament manually into your printer's extruer
5. Load the filament to your hotend using your printer controls
6. Reconnect the Chameleon's PTFE tube to your printer's extruder
7. Resume your print

Congratulations! You just recovered a failed toolchange.

## Why it failed

To prevent future load failures, here are some common causes and fixes for failed loads:

### Faulty filament sensor

If your printer's filament sensor is giving faulty readings, it can cause false alarms of failed loads and unloads. There are too many types and variations of filament sensors to cover them all, but here are some tips to diagnose the failure:

- Check filament sensor wiring
- If mechanical sensor, check the filament sensor for filament debris
- If optical sensor, the color of the filament may not work well with the sensor
- If optical sensor, lighting may also mess with detection reliability

### Previous filament failed to unload fully

If the previous filament failed to fully unload, it will be in the way of the next filament when trying to load. See [Unload Failed Troubleshooting](unloadfailed.md#why-it-failed) for common causes and fixes.

### 3DChameleon filament grip

If the 3DChameleon can't grip the filament properly, it won't be able to push it through the Y splitter into your printer's extruder. To fix this, print out and install [Tension Tuning Sliders](https://www.printables.com/model/872170-3dchameleon-mk4-pro-organized-models) for the problematic filament paths. Under `Files` -> `Tension Sliders`, pick the appropriate slider:

- The first value is the distance between the drive gear and the bearing. Smaller values here make them closer together.
- The second value is the tension of the springs pushing the bearing and the drive gear together. Larger values here make them pushed closer together with greater force.

### Tip Shaping

If your filament tip is improperly shaped, with a blob or string at the tip, it will require excessive force to load it through the tube. In extreme cases, you can get [the dreaded hook of death](https://forum.prusa3d.com/forum/postid/224374/). 

As a general rule of thumb, for `QUICK_TIP_SHAPING`, a larger `MOVES` value will result in cleaner tips. However, the most reliable method is to install an Auto3DClippy. See [Configuration](configuration.md) for config changes. Note that you will need to switch to the `dev` branch for Auto3DClippy support as of time of writing.