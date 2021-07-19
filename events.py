# --- Imports --- #

import pygame.event
from pygame.locals import *
from sys import exit as shutdown

# --- Pygame Event Tuples --- #

VIDEO = (VIDEORESIZE,)
JOYSTICK = (JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION)
KEYS = (KEYUP, KEYDOWN)
MOUSE = (MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION)
OTHER = (USEREVENT,)

# --- Events Class --- #

class Events:
    def __init__(self):

        #Blocks Useless Events and Allows Important Events
        self.__set_events((VIDEO+JOYSTICK+OTHER), block=True)
        self.__set_events((KEYS+MOUSE))

    def __set_events(self, events, block=False):

        if block:
            command = pygame.event.set_blocked
        else:
            command = pygame.event.set_allowed
            
        for event in events:
            command(event)
        
# --- Key Class --- #

class Keys(Events):
    def __init__(self, tuple_keys):

        import pygame.key

        super().__init__()

        self.keys = pygame.key
        self.list = tuple_keys

        self.back = tuple_keys[0]
        self.escape = tuple_keys[1]
        self.up = tuple_keys[2]
        self.down = tuple_keys[3]
        self.left = tuple_keys[4]
        self.right = tuple_keys[5]
        self.aim = tuple_keys[6]
        self.shoot = tuple_keys[7]
        
        self.dict = {self.back : "Go Back: ", self.up : "Move Up: ", self.down : "Move Down: ", self.left : "Move Left: ", self.right : "Move Right: ",
                     self.aim : "Aim: ", self.shoot : "Shoot: "}

    def new_keys(self, __button):

        __loop = True

        while __loop:
            for __event in pygame.event.get():
                if __event.type == KEYDOWN:
                    __loop = False
                    if __event.key == self.escape:
                        return self.escape

        self.__reset_key(__button, __event.key)
        __button.recreate(self.get_str(__event.key))

    def __reset_key(self, __button, __new):

        __button_index = __button.index
        if __button_index == 0:
            self.back = __new
        elif __button_index == 1:
            self.up = __new
        elif __button_index == 2:
            self.down = __new
        elif __button_index == 3:
            self.left = __new
        elif __button_index == 4:
            self.right = __new
        elif __button_index == 5:
            self.aim = __new
        elif __button_index == 6:
            self.shoot = __new

        self.dict = {self.back : "Go Back: ", self.up : "Move Up: ", self.down : "Move Down: ", self.left : "Move Left: ", self.right : "Move Right: ",
                     self.aim : "Aim: ", self.shoot : "Shoot: "}

    def get_str(self, key_):

        return (self.dict.get(key_)+(self.keys.name(key_).title()))
