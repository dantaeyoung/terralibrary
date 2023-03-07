from evdev import InputDevice, categorize, ecodes, list_devices
import tera
import time
import subprocess


devices = [InputDevice(path) for path in list_devices()]
for i, device in enumerate(devices):
    print(i, device.name, device)

device = InputDevice("/dev/input/event0")
device.grab()

def process_eventqueue(q):
    res = tera.events_to_str(q)
    print(res)
 
eventqueue = []
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if(event.code != tera.TERA_ENTER):
            eventqueue.append(event)
        else:
            if(len(eventqueue) > 0):
                process_eventqueue(eventqueue)
                eventqueue = []


device.ungrab()
