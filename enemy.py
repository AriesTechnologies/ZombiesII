# --- Imports --- #

#import pygame as pg
#from pygame.locals import *

class Enemy(object):
    def __init__(self):

        import sprites #My Module
        
        self.char_list = sprites.load_sprites("Zombies")
        

class Zombie(Enemy):
    def __init__(self):

        super().__init__()

        self.image = self.char_list["Zombie"]
