import pygame
from evdev import InputDevice, categorize, ecodes
from tera_keycodes import keycodes, to_key, events_to_str, TERA_ENTER
from firebase import firebase
import time
import subprocess

device = InputDevice("/dev/input/event2")
device.grab()



pygame.mixer.init()
pygame.mixer.music.load("/home/pi/github/intralocution/synth.mp3")
synth = pygame.mixer.Sound("/home/pi/github/intralocution/synth.mp3")
synth.play()


subprocess.call('espeak -s 5 "yello"', shell=True)

firebase = firebase.FirebaseApplication('https://terralibrary-a9249-default-rtdb.firebaseio.com', None)

def process_eventqueue(q):
    res = events_to_str(q)

    data = {
        'value': res,
        'timestamp': time.time()
    }

    result = firebase.post('/scans', data=data)
    print(res, result)

    if(res == "P1980"):
        pygame.mixer.music.play()

## read events, add to queue

eventqueue = []
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if(event.code != TERA_ENTER):
            eventqueue.append(event)
        else:
            if(len(eventqueue) > 0):
                process_eventqueue(eventqueue)
                eventqueue = []


device.ungrab()
