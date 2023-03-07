keycodes = {
    30: { "value": "a","upper": "A",  "type": "key"},
    48: { "value": "b","upper": "B",  "type": "key"},
    46: { "value": "c","upper": "C",  "type": "key"},
    32: { "value": "d","upper": "D",  "type": "key"},
    18: { "value": "e","upper": "E",  "type": "key"},
    33: { "value": "f","upper": "F",  "type": "key"},
    34: { "value": "g","upper": "G",  "type": "key"},
    35: { "value": "h","upper": "H",  "type": "key"},
    23: { "value": "i","upper": "I",  "type": "key"},
    36: { "value": "j","upper": "J",  "type": "key"},
    37: { "value": "k","upper": "K",  "type": "key"},
    38: { "value": "l","upper": "L",  "type": "key"},
    50: { "value": "m","upper": "M",  "type": "key"},
    49: { "value": "n","upper": "N",  "type": "key"},
    24: { "value": "o","upper": "O",  "type": "key"},
    25: { "value": "p","upper": "P",  "type": "key"},
    16: { "value": "q","upper": "Q",  "type": "key"},
    19: { "value": "r","upper": "R",  "type": "key"},
    31: { "value": "s","upper": "S",  "type": "key"},
    20: { "value": "t","upper": "T",  "type": "key"},
    22: { "value": "u","upper": "U",  "type": "key"},
    47: { "value": "v","upper": "V",  "type": "key"},
    17: { "value": "w","upper": "W",  "type": "key"},
    45: { "value": "x","upper": "X",  "type": "key"},
    21: { "value": "y","upper": "Y",  "type": "key"},
    44: { "value": "z","upper": "Z",  "type": "key"},
    11: { "value": "0","upper": ")",  "type": "key"},
    2: { "value": "1", "upper": "!", "type": "key"},
    3: { "value": "2","upper": "@",  "type": "key"},
    4: { "value": "3","upper": "#",  "type": "key"},
    5: { "value": "4","upper": "$",  "type": "key"},
    6: { "value": "5","upper": "%",  "type": "key"},
    7: { "value": "6","upper": "^",  "type": "key"},
    8: { "value": "7","upper": "&",  "type": "key"},
    9: { "value": "8","upper": "*",  "type": "key"},
    10: { "value": "9","upper": "(",  "type": "key"},
    41: { "value": "`","upper": "~",  "type": "key"},
    12: { "value": "-","upper": "_",  "type": "key"},
    13: { "value": "=","upper": "+",  "type": "key"},
    26: { "value": "[","upper": "{",  "type": "key"},
    27: { "value": "]","upper": "}",  "type": "key"},
    43: { "value": "\\","upper": "|",  "type": "key"},
    39: { "value": ";","upper": ":",  "type": "key"},
    40: { "value": "\'","upper": "\"",  "type": "key"},
    51: { "value": ",","upper": "<",  "type": "key"},
    52: { "value": ".","upper": ">",  "type": "key"},
    57: { "value": " ","upper": " ",  "type": "key"},
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
                    s += key['upper']
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
