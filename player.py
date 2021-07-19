# --- Imports --- #

import pygame.event
import pygame.locals

# --- Player Class --- #

class User():
    def __init__(self):

        import weapons
        from os import path, getlogin

        self.__doc__ = """Creates a User"""
        
        self.name = getlogin()#GetUserName()
        self.save = Save(self)
        if path.exists(self.save._file):
            __file = open(self.save._file, "r")
            __data = __file.read().splitlines()
            __file.close()
        else:
            __data = (0, 0, 0, False, 8, 27, 273, 274, 276, 275, 303, 32, 0)
            __file = open(self.save._file, "w")
            self.save.write(__data)
            __file.close()

        self.__weapons_list, self.__weapons_dict = weapons.create()

        self.__load_save(__data)
        self.get_character(self.__character_int)

        self.weapons_list = lambda: self.__weapons_list
        self.characters_dict = lambda: self.__characters_dict
        self.level = lambda: self.__level

    def __create_characters(self):

        self.__characters_dict = {}
        __character_names = ["Athlete", "Nerd", "Rapp", "ValleyGirl", "Gangster"]
        __i = 0
        for __image in self.__char_list:
            self.__characters_dict[__i] = (type("Character", (object, ), {"name" : __character_names[__i], "image" : self.__char_list[__character_names[__i]], "index" : __i}))
            __i += 1
            
    def __load_save(self, data):
        
        import sprites
        from ast import literal_eval
        
        self.__character_int = int(data[0])
        self.__level = int(data[1]) #Player Level
        self.__weapon_int = int(data[2])
        self.__weapon = (self.__weapons_dict.get(self.__weapon_int).name)
        self.joystick = literal_eval(data[3])
        self.__char_list = sprites.load_sprites("\\Characters") #Returns a dict
        self.__create_characters()
        self.character = self.__characters_dict[self.__character_int]

        __back = int(data[4])
        __quit_ = int(data[5])
        __up = int(data[6])
        __down = int(data[7])
        __left = int(data[8])
        __right = int(data[9])
        __aim = int(data[10])
        __shoot = int(data[11])

        __nerd_special = int(data[12])
        self.special = [__nerd_special]

        self.keys_list = (__back, __quit_, __up, __down, __left, __right, __aim, __shoot)
        
    def __earned_new_character(self):

        __special = self.special[self.__character_int]
##        if __character == "Athlete":
##            __special = "Boxer"
##        elif __character == "Nerd":
##            __special = "Programmed"
##        elif __character == "Rapp":
##            __special = "Coach"
##        elif __character == "ValleyGirl":
##            __special = "BeachGirl"
##        elif __character == "Gangster":
##            __special = "Kingpin"
##        self.characters_dict[(len(self.characters_dict.keys()))] = special

    def get_character(self, index):

        self.__character_int = index
        __character = self.__characters_dict[self.__character_int]
        self.character = __character.name
        self.image = __character.image
        return __character

    def check_save(self):

        self.save_list = ((self.__character_int, self.__level, self.__weapon_int, self.joystick,)+self.keys_list+tuple(self.special))


class Player(User):
    def __init__(self, keys):

        super().__init__()
        self.keys = keys

##        self.get_character()

    def get_weapon(self):

        self.weapon = self.__weapons_dict.get(self.__weapon_int)
##        self.image = self.char_list[self.]

    def update(self):
        
        #This will be for when the player changes weapons and 'recreates' the character model
        pass

    def __main__(self):

        for event in pygame.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == self.keys.escape:
                    pass
                if event.key == self.keys.up:
                    pass
                if event.key == sef.keys.down:
                    pass
                if event.key == self.keys.left:
                    pass
                if event.key == self.keys.right:
                    pass
            
        
# --- Save Class --- #

class Save:
    def __init__(self, user):

        from os import getcwd
        self.__user = user
        self._file = (getcwd()+"\\Files\\"+user.name+".sgf")

    def write(self):

        self.__user.check_save()

        file = open(self._file, "w")
        for data in self.__user.save_list:
            file.write(str(data)+"\n")
            
        file.close()
