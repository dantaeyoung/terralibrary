import pygame
from tera import keycodes, to_key, events_to_str, TERA_ENTER
import time
from say import say
from barlanginterpreter import BarlangInterpreter

tbi = BarlangInterpreter()

tbi.interpret("help:ooga")
tbi.interpret("help:state")

