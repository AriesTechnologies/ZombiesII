# --- Imports --- #
import pygame.display as pg_display
from pygame.locals import *
from sys import exit as shutdown

# --- DisplayInfo Class --- #

class DisplayInfo(object):
    def __init__(self, __quit):

        self.__quit = __quit

        self.__display_dict = {
            FULLSCREEN : "Fullscreen",
            DOUBLEBUF : "Doublebuffered",
            RESIZABLE : "Resizable",
            NOFRAME : "No Frame",
            HWSURFACE : "Hardware Accelerated",
##            OPENGL : "OpenGL",
            }

        self.__cords = (1284,720)#(GetSystemMetrics(0), GetSystemMetrics(1))
        self.__backend = (pg_display.get_driver().title())
        self.__info = pg_display.Info()
        
        self.__get_type()
        self.__set_display()
        
##        __main_window = GetForegroundWindow()
##        ShowWindow(__main_window, SW_MAXIMIZE)

        self.__gamma = 1.0

        self.gamma = lambda: self.__gamma
        self.display = lambda: self.__display
        self.backend = lambda: self.__backend

    @property
    def cords(self):

        return self.__cords
    
    def change_gamma(self):

        from pygame.event import get

        __loop = True
        __difference = 0.0
        
        while __loop:
            for __event in get():
                if __event.type == QUIT:
                    self.__quit()
                elif __event.type == KEYDOWN:
                    if __event.key == K_BACKSPACE:
                        __loop = False
                    elif __event.key == K_UP:
                        if self.__gamma < 2.0:
                            __difference = 0.1
                    elif __event.key == K_DOWN:
                        if self.__gamma > 0.3:
                            __difference = -0.1

                    self.__gamma += __difference
                    pg_display.set_gamma(round(self.__gamma, 1))
                    
            pg_display.flip()

    def __get_type(self, new_type=(RESIZABLE, DOUBLEBUF)):

        self.__subtype = new_type
        self.__type = (self.__subtype[0] | self.__subtype[1])
        self.__str__ = (self.__display_dict.get(self.__subtype[0])+", "+self.__display_dict.get(self.__subtype[1]))

    def __set_display(self):

        self.__display = pg_display.set_mode(self.__cords, self.__type)


if __name__ == "__main__":

    di = DisplayInfo("")

        
