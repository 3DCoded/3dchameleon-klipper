# Relay Wiring

### To wire your relay to your 3DChameleon, follow this table:
#### NOTE that this requires a Relay SHIELD. You will have to use a different wiring scheme to connect a Relay without a shield.

**Limit Switch to 3DChameleon**

| Limit Switch | 3DChameleon |
| - | - |
| + (Red) | Same (via Dupont) |
| - (Black) | Same (via Dupont) |
| Data (Green) | Dupont (leave other end loose for now) |
| Another dupont (leave other end loose for now) | Data (Last remaining limit switch pin)

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