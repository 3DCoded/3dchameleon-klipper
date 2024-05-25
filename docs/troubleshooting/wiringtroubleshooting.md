# Wiring Troubleshooting

If your Chameleon is behaving strangely after connecting it to your Raspberry Pi, follow this guide for some common problems and solutions.

## For [2-wire method](wiring.md#2-wire-method)

If you used the 2-wire method of wiring your Chameleon to your Raspberry Pi, the following are a few common wiring problems, and some solutions.

### GND and Data switched: Chameleon always pulsing

If your Ground and Data wires are swapped, the Chameleon pin will be inverted. To test for this, use:
```
SET_CHAMELEON VALUE=1
```
If the Chameleon stops pulsing after this, then your Ground and Data wires are swapped. To fix it, just switch them. After you do this, the pulsing should start again. Run:
```
SET_CHAMELEON VALUE=0
```
and verify that pulsing stops now. If so, your Chameleon is now working properly with your Raspberry Pi.

### Wrong pins plugged into Chameleon: No pulsing

There are three pins for the limit switch: V+, GND, and Data. The two wires should go into the GND and Data pins. Make sure to follow [Wiring](wiring.md) carefully to plug the wires into the correct pins.

## For [Relay method](wiring.md#relay-shield-method)

### NC and NO swapped on the Relay Shield: No pulsing or Always pulsing

Make sure that you followed [Wiring](wiring.md) correctly to ensure that you are using the COM and NO pins, not COM and NC pins on the relay shield.

### Limit Switch not pressed

Make sure that your limit switch is securely closed (mechanically) using a zip tie.