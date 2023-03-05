from say import say
from firebase import firebase
import time

firebase = firebase.FirebaseApplication('https://terralibrary-a9249-default-rtdb.firebaseio.com', None)

def ooga(bloop):
    say("Ooooga booga")


def stackstring(stack):
    if(len(stack) == 0):
        s = "Stack is empty."
    else:
        s = "Stack is: " + ", ".join(stack)
    return s

def excl_status(s):
    m = ""
    m += "Mode is: " + s['mode'] + ". \n"
    m += stackstring(s['stack'])
    say(m)
    return s

def excl_clearstack(state):
    state['stack'] = []
    say("Clearing stack")
    return state

def runstack(s):
    if(len(s['stack']) == 0):
        say("No stack to run")
    else:
        say("runstack")
        print(s)
    return

def add(s):
    data = {
        'value': s,
        'timestamp': time.time()
    }
    result = firebase.post('/list', data=data)
    say("add " + str(s['param']))
    return

def remove(s):
    say("remove " + str(s['param']))
    return
