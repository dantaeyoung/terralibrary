import pygame
from evdev import InputDevice, categorize, ecodes
from tera import keycodes, to_key, events_to_str, TERA_ENTER
from firebase import firebase
import time
from say import say
import barlanginterpreter
import importlib

device = InputDevice("/dev/input/event2")
device.grab()


pygame.mixer.init()
bowl= pygame.mixer.Sound("bowl.mp3")

#say.say("Terra-library is ready.")
say("Ready.")

firebase = firebase.FirebaseApplication('https://terralibrary-a9249-default-rtdb.firebaseio.com', None)


tbi = barlanginterpreter.BarlangInterpreter()


def process_eventqueue(q):
    s = events_to_str(q)

    data = {
        'value': s,
        'timestamp': time.time()
    }

#    result = firebase.post('/scans', data=data)
#    print(s, result)

    print(s)

    if(s.startswith("#reloadbarlanginterpreter")):
        say("reloading barlang interpreter")
        importlib.reload(barlanginterpreter)
        global tbi
        tbi = barlanginterpreter.BarlangInterpreter()
        tbi.reload()
        return

    tbi.interpret(s)


    #say.say(res)

#    if(res == "P1980"):
#        bowl.play()

## read events, add to queue




eventqueue = []
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
#        print(event)
        if(event.code != TERA_ENTER):
            eventqueue.append(event)
        else:
            if(len(eventqueue) > 0):
                process_eventqueue(eventqueue)
                eventqueue = []


device.ungrab()
