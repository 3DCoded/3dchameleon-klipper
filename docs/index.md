# Home

## About

**3dchameleon-klipper** is a highly configuration klipper plugin for the [3DChameleon](https://3dchameleon.com)

## Features

- Many configuration options
- Using the filament sensor to allow for more reliable loads and unloads
- Many helpful macros and G-Code commands
- Saving the state of the 3DChameleon to reduce the guesswork
- Helping in tip shaping with a flexible macro
- Assigning different tip shaping parameters for each filament
- Detailed documentation to diagnose common issues
- KlipperScreen control panel for the Chameleon
- Support for Klipperized Auto3DClippy
- Support for normal Auto3DClippy

## Planned Features

- Support for multiple filament sensors to reduce failed unloads (See [#4](https://github.com/3DCoded/3dchameleon-klipper/issues/4))
- Support for "telling" the Chameleon what tool is loaded based on the filament sensors
- Ability to assist with initially loading the Chameleon (see [#5](https://github.com/3DCoded/3dchameleon-klipper/issues/5))
- LCD control panel for the Chameleon (see [#9](https://github.com/3DCoded/3dchameleon-klipper/issues/9))

## "Quick"-start

### Wiring

To begin setting up **3dchameleon-klipper**, see [Wiring](wiring.md) to connect your 3DChameleon to your Raspberry Pi.

### Install

Install **3dchameleon-klipper**. Run the following on your Raspberry Pi:

    `cd ~ && git clone https://github.com/3DCoded/3dchameleon-klipper && cd 3dchameleon-klipper && ./install.sh`

### Configuration

Follow [Configuration](configuration.md) to configure your 3DChameleon to your specific setup.

### Slicer Setup

Follow [Slicer Setup](slicersetup.md) to setup PrusaSlier for this plugin and your 3DChameleon. OrcaSlicer support is coming soon.