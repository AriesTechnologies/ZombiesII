# --- Imports --- #
import pygame as pg
from pygame.locals import *
import player #My Module
import enemy #My Module
import maps #My Module
from sys import exit, exc_info
pg.init()

# --- Version Class --- #

class Version(object):
    def __init__(self):
        
        self.__dict = {
            "0.0.1": "Created basic code to get to title menu",
            "0.0.2": "Added graphics module to help create the menus",
            "0.0.3": "Improved graphics module, runs at 60 fps",
            "0.1.0": "Added in weapons module, loadout menu, improved graphics module",
            "0.1.1": "Added in Stats Menu, changed a graphics module argument slightly",
            "0.1.2": "Improved how the menus load in and draw to the display",
            "0.1.3": "Removed stats from the Stats Menu do to them causing frame drop issues",
            "0.1.4": "Added stats from the Stats Menu back, improved frame drop issue, runs between 55 and 60",
            "0.1.5": "Improved game and graphics module code slightly, runs between 57 to 60 FPS, 59 on average",
            "0.1.6": "Changed how the game gets coordinates, improved FPS, 58 to 60 on average",
            "0.1.7": "Changed how the game receives button activation, FPS 58 to 60 average",
            "0.2.0": "Added in the ability to change the gamma for colors and the type of display",
            "0.2.1": "Added in the ability to change the keys used for the game",
            "0.2.2": "Added in the intros (can be skipped with any key), added ability to change character in loadout",
            "0.2.3": "Added in new characters menu and weapons menu in loadout menu",
            "0.3.0": "Improved game code, added in save file (old save files will not work), controls now based on user",
            "0.3.1": "Improved the graphics module, FPS 59 to 60 on average",
            "0.3.2": "Added in a basic weapons menu to keep it from crashing when you click the button ,)",
            "0.3.3": "Added some new graphics, still adding graphics in the next couple updates",
            "0.3.4": "Changed how graphics module works slightly (again), no graphic changes",
            "0.3.5": "Bug fixes, changed how the game runs slightly (not noticable), graphic changes to characters",
            "0.3.6": "Added enemy classes as well as more player classes, changed how game compiles, bug fixes",
            "0.3.7": "Changed how the graphics class text works, fixed bug that was giving the wrong FPS status",
            "0.3.8": "Added basic weapons menu, changed how game loads the display and menus, runs at 60 FPS",
            "0.3.9": "Changed how the pause menu gets displayed, bug fixes with 'menu paths'",
            "0.3.10": "Changed how the moving back in the menu screen works, runs slightly faster",
            "0.3.11": "Improved overall game code, runs 58-60 FPS on average, fixed bug with the loadout menus",
            "0.4.0": "Added new characters, 1 regular and 1 secret, changed save files (old save files will not work)",
            "0.4.1": "Added new animations for characters, improved game code slightly",
            "0.4.2": "Improved game code, as well as graphics module, runs 59-60 with possible lag to 56-58",
            "0.4.3": "Improved game code, runs 59-60 unless on low battery mode which can lag to 53-55 at times",
            "0.4.4": "Improved game code to make it more secure, changed how versions are created",
            "0.4.5": "Changed some game code security, to make it run faster",
            "0.4.6": "Added new running graphics from some characters",
            "0.4.7": "Greatly improved graphics module, fixed bugs with running graphics, runs 59-60 FPS at all times",
            "0.4.8": "Fixed bugs with solid colored backgrounds in the graphics module",
            "0.4.9": "Added security updates to the \"display info\" module and the game in general",
            "0.4.10": "Added security to \"display_info\" module, added new menu graphics, fixed bug with saving the game state",
            "0.4.11": "Added security updates to \"player\" module, fixed bug with intro screen never ending",
            "0.4.12": "Added gameplay menu under options, fixed bug with the options menu, and gameplay menu",
            "0.4.13": "Added maps under loadout menu, added maps module, added objects module",
            "0.4.14": "Added all running graphics and player name on title menu, fixed some errors in the character graphics",
            "0.4.15": "Added some character shooting graphics, fixed couple errors with some other character graphics",
            "0.5.0": "Added the Zombies II Icon, changed the module startup order",
            "0.5.1": "Added the rest of the character shooting graphics, fixed a couple errors with other graphics",
            "0.5.2": "Changed how the menus work by adding a submenu list inside the menu, fixed a bug with menu paths",
            "0.5.3": "Changed how the game gets versions, improved code security, fixed some FPS lag",
            "0.5.4": "Added a new type of menu (StaticMenu) to the graphics module",
            "0.5.5": "Changed how 'menu paths' work, fixed several bugs with menus",
            "0.5.6": "Changed how menus are loaded in, improved speed slightly, fixed bugs with several menus",
            "0.5.7": "Changed how the display class 'talks' to the app class, fixed bugs with menus",
            "0.5.8": "Removed several 'behind the scenes' menus, improved FPS (30 FPS is still recommended)",
            "0.5.9": "Changed how buttons work slightly due to a bug in the characters menu and weapons menu",
            "0.5.10": "Changed how the menus work (they run much faster overall), fixed a couple bugs with menus",
            "0.6.0": "Changed how some menus communicate by using a different function type, improved FPS slightly",
            "0.6.1": "Changed how modules are loaded into certain areas of the program, fixed with gamma menu",
            "0.6.2": "Added SS-1 (shotgun) graphics, fixed couple errors with the player graphics",
            "0.6.3": "Changed how buttons work in the graphics module, improved speed slightly",
            "0.6.4": "Added all the weapon graphics to the loadout menu",
            "0.6.5": "Changed how menu objects were loaded in, improved speed (60 FPS now recommended)",
            "0.6.6": "Changed how the controls menu works internally (since there were problems), improved speed",
            "0.6.7": "Changed what the \"display info\" module receives from the application to improve speed",
            "0.6.8": "Removed some fairly useless information variables",
            "0.6.9": "Changed how the menu buttons were loaded in to the menus",
            "0.6.10": "Removed some repetitive menu instances and changed version numbers on all versions",
            "0.6.11": "Changed how buttons active events were received, fixed a bug with controls loop",
            "0.6.12": "Changed how characters menu and weapons menu grab character and weapon information",
            "0.7.0": "Changed the game API from Python 3.6 to Python 3.7 (made game run at 60 FPS with possible lag to 59)",
            "0.7.1": "Added map intro menu, changed how modules were loaded, changed graphics module message arguments",
            "0.7.2": "Added map info to create the map intro quicker and more efficiently",
            "0.7.3": "Added the ability to choose which map you want in the Maps Menu, changed how map intro was loaded in",
            "0.7.4": "Changed how map info was loaded in, added in game class",
            "0.7.5": "Fixed bugs with menus after I broke the graphics file",
            }
        
        #Newest version needs to be published but cx_Freeze doesn't support Python 3.7 yet
        
        self.__tuple = (tuple(self.__dict.items()))
        self.version = (tuple(self.__dict.keys())[-1])
        self.version_type = "Gamma"

        self.versions = lambda: self.__dict
        self.get_tuple = lambda: self.__tuple

# --- Application Class --- #

class Application():
    def __init__(self):
        """Starts the game and stores settings"""

        import sprites#My Module
        import menus#My Module
        import display_info#My Module
        import events #My Module

        self.__name__ = """Zombies II"""
        self.__repr__ = """main.Application.__main__()"""
        self.__module__ = """pygame, sys"""
        self._license = """Open sourced CC0 License"""
        self._copyright = """©2018 AtlasCorporations LLC/AtlasStudios"""

        self.__in_game = False
        self._version = Version()
        
        #Starts Clock
        self.clock = pg.time.Clock()
        self._fps = 60

        #Quick Functions (basically definitions but in one line)                
        self.save = lambda: self.player.save.write()
        self.__draw = lambda: self.__menu.draw()
        self.__append_menu = lambda: self.__path_list.append(self.__menu)
        pg.register_quit(self.save)

        #Display Information/Load Sprites
        pg.display.set_caption(self.__name__)
        self.display_info = display_info.DisplayInfo(self._quit)
        self.sprites_dict = sprites.load_sprites("Backgrounds")
        pg.display.set_icon(self.sprites_dict["Icon"])
        self.__developer_logos = (self.sprites_dict["AtlasStudios"], )

        self.__display = self.display_info.display()
                
        #Load Player Data
        self.player = player.User() #Player Class calls weapons class 'setup' otherwise there will be an error        
        self._weapons_list = self.player.weapons_list()
        self.events = events.Keys(self.player.keys_list)
##        if self.player.joystick:
##            self.events.__set_events(JOYSTICK)

        self.map = maps.Maps()
        __menus_list = menus.create(self)

        self.__title_menu = __menus_list[0]
        self.__character_menu = __menus_list[1]
        self.__weapons_menu = __menus_list[2]
        self.__maps_menu = __menus_list[3]
        self.__controls_menu = __menus_list[4]
        self.__gameplay_menu = __menus_list[5]
        self.__gamma_menu = __menus_list[6]
        self.__paused_menu = __menus_list[7]
        self.__map_intro_menu = __menus_list[8]

        self.__reset_menus()

    def __reset_menus(self):
        
        self.__menu = self.__title_menu
        self.__path_list = [self.__menu]

    def __loading(self):

        self.__game = Game()
        self.__intro(175, self.__menu.draw())
        self.__reset_menus()
##        self.__in_game = 1
            
    def __intro(self, __time, __bg):

        __i = 0
        self.__display.blit(__bg, (0,0))
        pg.display.flip()       
        while __i < __time:
            for event in pg.event.get():
                if event.type == QUIT:
                    self._quit()
                elif event.type in (KEYDOWN, MOUSEBUTTONDOWN):
                    __i = __time

            __i += 1
            self.clock.tick(self._fps)

    def __recreate_menu(self, __button):

        if (self.__menu == self.__character_menu and __button in self.__character_menu.buttons) or (self.__menu == self.__weapons_menu and __button in self.__weapons_menu.buttons):
            if self.__menu == self.__character_menu:
                __change_obj = self.player.get_character(__button.index)
            else:
                __change_obj = self._weapons_list[__button.index]
                
            self.__menu.change_msg(2, __change_obj.name)
            self.__menu.change_img(1, __change_obj.image)

        elif self.__menu == self.__controls_menu:
            while True:
                for event in pg.event.get():
                    if event.type == QUIT:
                        self._quit()
                    elif event.type == KEYDOWN:
                        if event.key == self.events.back:
                            self.__back()
                            return
                    elif event.type == MOUSEBUTTONDOWN:
                        __button = self.__menu.get_button()
                        if __button != None:
                            self.events.new_keys(__button)
                self.__draw()

        elif self.__menu == self.__gameplay_menu and __button.index == 0:
            if self._fps == 60:
                self._fps = 30
            else:
                self._fps = 60
            
            __button.recreate((f"FPS: {self._fps}"))
                
        elif self.__menu == self.__gamma_menu:
            self.__draw()
            self.display_info.change_gamma()
            self.__back()

        elif self.__menu == self.__paused_menu and __button.index == 1:
            self._quit()

        elif self.__menu == self.__maps_menu:
            __button = self.__menu.get_button()
            if __button != None:
                self.map.get_map(__button.index)
                __info = self.map.map_info()
                self.__menu.change_msg(2, self.map.name())
                for index, msg in (enumerate(self.__map_intro_menu.messages)):
                    msg.text = __info[index]

        elif self.__menu == self.__map_intro_menu:
            self._in_game = True

    def change_loadout(self, __button):
        
        __button = self.__menu.get_button()
        if self.__menu == self.__character_menu:
            __change_obj = self.player.get_character(__button.index)
        else:
            __change_obj = self._weapons_list[__button.index]
            
        self.__menu.change_msg(2, __change_obj.name)
        self.__menu.change_img(1, __change_obj.image)        

    def controls_loop(self):

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    self._quit()
                elif event.type == KEYDOWN:
                    if event.key == self.events.back:
                        self.__back()
                        return
                elif event.type == MOUSEBUTTONDOWN:
                    __button = self.__menu.get_button()
                    if __button != None:
                        self.events.new_keys(__button)
            self.__draw()
        

    def change_fps(self, __button):
        
        if self._fps == 60:
            self._fps = 30
        else:
            self._fps = 60
        
        __button.recreate(("FPS: "+str(self._fps)))

    def change_gamma(self):
        
        self.__draw()
        self.display_info.change_gamma()
        self.__back()

    def change_map(self, __button):

##        __button = self.__menu.get_button()
        if __button != None:
            self.map.get_map(__button.index)
            __info = self.map.map_info()
            self.__menu.change_msg(2, self.map.name())
            for index, msg in (enumerate(self.__map_intro_menu.messages)):
                msg.text = __info[index]

    def start(self):
        
        self.__in_game = True

    def __back(self):

        if self.__menu != self.__path_list[0]:
            self.__path_list.pop()
            self.__menu = self.__path_list[-1]
            
    def __get_menu(self):

        __button = self.__menu.get_button()
        if __button != None:
            self.__menu = (self.__menu.submenus[__button.index])
            if self.__menu != self.__path_list[-1]:
                self.__append_menu()
        
            self.__recreate_menu(__button)

    def _quit(self):

        pg.quit()
        exit()

    def __title_main(self):
        
        for __event in pg.event.get():
            if __event.type == QUIT:
                self._quit()
            elif __event.type == KEYDOWN:
                if __event.key == self.events.back:
                    self.__back()
##                    elif __event.key == K_ESCAPE: #For testing purposes
##                        self.__menu = self.__paused_menu
##                        self.__append_menu()
            elif __event.type == MOUSEBUTTONDOWN:
                self.__get_menu()

        self.__draw()
        pg.display.set_caption(f"{self.__name__} {round(self.clock.get_fps(), 2)}")
        self.clock.tick(self._fps)            

    def __main__(self):

        for logo in self.__developer_logos:
            self.__intro(100, logo)

        while True:
            while not self.__in_game:
                self.__title_main()
            while self.__in_game:
                self.__loading()
                self.__game.__main__()

class Game(Application):
    def __init__(self):
        
        from os import getcwd
        super().__init__()
        
        self.__player = player.Player(self.player.keys_list)
        self.__tile_map = maps.TiledMap((f"{getcwd()}\\Maps\\{self.map.name()}.tmx"))

    def __get_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self._quit()
            elif event.type == MOUSEBUTTONDOWN:
                self.__alive = False

    def update(self):
        
        pass

    def draw(self):

        self.__menu.blit()
        self.clock.tick(self._fps)

    def __main__(self):

        self.__alive = True
        while self.__alive:
            self.__get_events()
##            self.update()
            self.draw()

        self.save()
        return self.__alive
            
        
        
if __name__ == "__main__":
    """Starts Application"""
    
    Application().__main__()
