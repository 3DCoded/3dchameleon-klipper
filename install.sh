#!/bin/bash
cp 3dchameleon.cfg ~/printer_data/config/3dchameleon.cfg
echo Installed Configuration
echo "[include 3dchameleon.cfg]" >> ~/printer_data/config/printer.cfg
echo Added Configuration to printer.cfg
sh ./update.sh
echo Installed 3dchameleon.py