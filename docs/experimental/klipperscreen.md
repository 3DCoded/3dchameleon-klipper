# KlipperScreen

Follow this guide to setup 3DChameleon-klipper with KlipperScreen.

**This feature is still experimental and UNTESTED**

## Screenshots

![](klipperscreenmainmenu.png)
![](klipperscreenmain.png)
![](klipperscreenunload.png)

## Images

First, the 3DChameleon's image needs to be added to KlipperScreen. Run the following command to download it:
```
cd ~
wget https://3dcoded.github.io/3dchameleon-klipper/assets/images/3dchameleon.png
mv 3dchameleon.png ~/KlipperScreen/styles/YOUR-KLIPPERSCREEN-STYLE/images/
```

## Configuration

In `KlipperScreen.conf`, in the same folder as your `printer.cfg`, add the following before the commented section at the bottom, but after the printer section:

```
[menu __main chameleon]
name: 3DChameleon
icon: 3dchameleon

[menu __main chameleon seton]
name: Set On
icon: increase
method: printer.gcode.script
params: {"script": "SET_CHAMELEON VALUE=1"}

[menu __main chameleon setoff]
name: Set Off
icon: decrease
method: printer.gcode.script
params: {"script": "SET_CHAMELEON VALUE=0"}

[menu __main chameleon reset]
name: Reset
icon: ccw
method: printer.gcode.script
params: {"script": "RESET_CHAMELEON"}

[menu __main chameleon load]
name: Load
icon: extrude
method: printer.gcode.script
params: {"script": "LOAD_CHAMELEON"}

[menu __main chameleon unload]
name: Unload
icon: retract

[menu __main chameleon unload unloadt0]
name: Unload T0
icon: extruder-0
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=0"}

[menu __main chameleon unload unloadt1]
name: Unload T1
icon: extruder-1
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=1"}

[menu __main chameleon unload unloadt2]
name: Unload T2
icon: extruder-2
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=2"}

[menu __main chameleon unload unloadt3]
name: Unload T3
icon: extruder-3
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=3"}

[menu __print chameleon]
name: 3DChameleon
icon: 3dchameleon

[menu __print chameleon seton]
name: Set On
icon: increase
method: printer.gcode.script
params: {"script": "SET_CHAMELEON VALUE=1"}

[menu __print chameleon setoff]
name: Set Off
icon: decrease
method: printer.gcode.script
params: {"script": "SET_CHAMELEON VALUE=0"}

[menu __print chameleon reset]
name: Reset
icon: ccw
method: printer.gcode.script
params: {"script": "RESET_CHAMELEON"}

[menu __print chameleon load]
name: Load
icon: extrude
method: printer.gcode.script
params: {"script": "LOAD_CHAMELEON"}

[menu __print chameleon unload]
name: Unload
icon: retract

[menu __print chameleon unload unloadt0]
name: Unload T0
icon: extruder-0
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=0"}

[menu __print chameleon unload unloadt1]
name: Unload T1
icon: extruder-1
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=1"}

[menu __print chameleon unload unloadt2]
name: Unload T2
icon: extruder-2
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=2"}

[menu __print chameleon unload unloadt3]
name: Unload T3
icon: extruder-3
method: printer.gcode.script
params: {"script": "UNLOAD_CHAMELEON TOOL=3"}
```

## Restart KlipperScreen

After following the above steps, restart KlipperScreen:
```
sudo service KlipperScreen restart
```