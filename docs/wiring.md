# Wiring

There are two main methods of connecting your 3DChameleon to your Raspberry pi. The 2-wire method is the recommended method, while the relay method allows for easier debugging with the limit switch. 

**NOTE** that there is a different pin configuration required for each method. See below for details. 

## 2-wire method

This is the simplest method of wiring your 3DChameleon to your Raspberry Pi.

**Steps:**

1. Unplug the limit switch from the 3DChameleon, taking note of which color wire was plugged into where.
2. Plug one dupont into the 3DChameleon, where the black wire of the limit switch used to be. To avoid confusion, use a black dupont here if possible.
3. Plug another dupont into the 3DChameleon, where the green wire of the limit switch used to be.
4. Connect the black dupont to a GND pin of your Raspberry Pi; see [pinout.xyz](https://pinout.xyz/) for where this pin is.
5. Connect the other dupont to a GPIO pin of your Raspberry Pi. The default config uses GPIO18, but you can use any other pin as long as it starts with "GPIO".

## Relay (shield) method

This method is more complex, and adds a clicking noise every time your Chameleon is triggered, but is helpful for debugging. Before wiring according to the tables below, use a zip tie to keep the limit switch pressed.

**Limit Switch to 3DChameleon**

| Limit Switch | 3DChameleon |
| - | - |
| + (Red) | Same (via Dupont) |
| - (Black) | Same (via Dupont) |

**Misc Wiring**

| Source | Destination |
| - | - |
| Limit Switch Data (Green) | Dupont (leave other end loose for now) |
| 3DChameleon Data (Last remaining limit switch pin on 3DChameleon board) | Another dupont (leave other end loose for now) | 


**Limit Switch to Relay**

| Limit Switch | Relay |
| - | - |
| Loose Data Dupont | COM (screw terminal) |

**3DChameleon to Relay**

| 3DChameleon | Relay |
| - | - |
| Loose Data Dupont | NO (screw terminal, Normally Open) |

**Raspberry Pi to Relay**

| Raspberry Pi | Relay |
| - | - |
| 5V | VCC | 
| GND | GND |
| GPIOxx | SIG (last remaining relay pin) | 

## Debugging with relay method

If you used the relay method, you can bypass the Raspberry Pi to control the Chameleon. 

**Steps:**

1. Run: `SET_CHAMELEON VALUE=1`
2. You can now press the limit switch to control your Chameleon directly
3. After debugging, run: `SET_CHAMELEON VALUE=0`

## Configuration

If you use the 2-wire method, your `[output_pin 3dchameleon]` section should look like:
```
[output_pin 3dchameleon]
pin: !host: gpio20 # Note the !
```

If you use the relay method, your `[output_pin 3dchameleon]` section should look like:
```
[output_pin 3dchameleon]
pin: host: gpio20 # Note that there is no !
```