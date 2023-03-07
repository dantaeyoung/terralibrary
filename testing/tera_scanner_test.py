import pygame
from evdev import InputDevice, categorize, ecodes, list_devices
from firebase import firebase
import time
import subprocess


devices = [InputDevice(path) for path in list_devices()]
for i, device in enumerate(devices):
    print(i, device.name, device)

device = InputDevice("/dev/input/event0")
device.grab()

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        print(event)


device.ungrab()
