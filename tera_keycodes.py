keycodes = {
    30: { "value": "a", "type": "key"},
    48: { "value": "b", "type": "key"},
    46: { "value": "c", "type": "key"},
    32: { "value": "d", "type": "key"},
    18: { "value": "e", "type": "key"},
    33: { "value": "f", "type": "key"},
    34: { "value": "g", "type": "key"},
    35: { "value": "h", "type": "key"},
    23: { "value": "i", "type": "key"},
    36: { "value": "j", "type": "key"},
    37: { "value": "k", "type": "key"},
    38: { "value": "l", "type": "key"},
    50: { "value": "m", "type": "key"},
    49: { "value": "n", "type": "key"},
    24: { "value": "o", "type": "key"},
    25: { "value": "p", "type": "key"},
    16: { "value": "q", "type": "key"},
    19: { "value": "r", "type": "key"},
    31: { "value": "s", "type": "key"},
    20: { "value": "t", "type": "key"},
    22: { "value": "u", "type": "key"},
    47: { "value": "v", "type": "key"},
    17: { "value": "w", "type": "key"},
    45: { "value": "x", "type": "key"},
    21: { "value": "y", "type": "key"},
    44: { "value": "z", "type": "key"},
    11: { "value": "0", "type": "key"},
    2: { "value": "1", "type": "key"},
    3: { "value": "2", "type": "key"},
    4: { "value": "3", "type": "key"},
    5: { "value": "4", "type": "key"},
    6: { "value": "5", "type": "key"},
    7: { "value": "6", "type": "key"},
    8: { "value": "7", "type": "key"},
    9: { "value": "8", "type": "key"},
    10: { "value": "9", "type": "key"},
    28: { "value": "ENTER", "type": "mod"},
    42: { "value": "LEFTSHIFT", "type": "mod"},
}

def to_key(keycode):
    if keycode in keycodes:
        return keycodes[keycode]
    else:
        return ""

#TODO make work for shift
def events_to_str(eventqueue): 

    shift = False
    s = ""
    for event in eventqueue:
        key = to_key(event.code)
        if(event.value == 1):
            #key pressed
            if(key['type'] == "mod"):
                if(key['value'] == "LEFTSHIFT"):
                    shift = True
            else:
                if(shift == True):
                    s += key['value'].upper()
                else:
                    s += key['value']
        else:
            # key unpressed
            if(key['type'] == "mod"):
                if(key['value'] == "LEFTSHIFT"):
                    shift = False
    return s
#    return ''.join([to_key(k)['value'] for k in keycodes])

TERA_ENTER = 28
