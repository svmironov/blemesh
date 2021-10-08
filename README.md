# Ble Mesh Home Assistant Add-On for JDY-10

This module allows control JDY-10 microcontroller with 10M-V2.3 firmware. All devices in mesh network must have the same bluetooth name and mesh networks ID.

**Sample device configuration with AT commands**

    AT+NAMEStar Light 
    AT+MADDR01
    AT+RESET

## Features

Enable or disable power on pin E5 (OUT 1).           
   
## Installation

First install HACS if you don't have it yet. Add https://github.com/svmironov/blemesh to HACS as user repository.

## Configuration

    light:
     - platform: ble_mesh
       name: kerosene_lamp
       mac: '12:34:56:04:0F:0E'
       device_id: 0x01

## Parameters

### name
Any name for your device

### mac
Mac address of control device, any in mesh network devices. 

### device_id
HEX Short name device in mesh network. Default: Last byte of MAC address.