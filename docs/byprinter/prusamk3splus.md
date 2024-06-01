# Prusa MK3S+

This guide will go through the modifications I did/am doing to get the 3DChameleon to work properly. 

**This is still a work in progress! Feedback is greatly appreciated.**

## Firmware

Klipper firmware will need to be installed via [this guide](https://github.com/dz0ny/klipper-prusa-mk3s)

## Hardware

I am currently in the process of figuring out the optimal hardware for the 3DChameleon with Prusa MK3S+. So far, the modifications that have worked for me:

- [Auto3DKlippy](auto3dklippy.md)

    This is an [Auto3DClippy](auto3dclippy.md) controlled via Klipper. It eliminates the need for tip shpaing.

- [MMU3 IR Sensor](https://www.printables.com/model/531604-mmu3-printable-parts)

    The IR sensor from the MMU3 has given me more success so far. To use it, you will have to use the `dev` branch, as it requires slightly different loading logic.