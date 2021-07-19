# --- Imports --- #

##import graphics
from pygame import Surface

##Colors
__colors_dict = {
"black" : (0,0,0),
"red" : (150,0,0),
"green" : (50,140,0),
"dark_green" : (50,100,0),
"white" : (255,255,255),
"dark_grey" : (30,30,30),
"grey" : (130,130,130)}

def __updates_msg(menu, info, spacing=[]):

    menu.add_messages([("Updates", "dark_green", (0,-315), "large"), ("Updates", "green", (-5,-315), "large")])
    y = spacing[0]

##    info = app._version.get_tuple()

    for version in info[len(info)-24:]:
    
        menu.add_messages([(("Update "+version[0]+" Gamma: "+version[1]), "white", (0,y), "small")])
        y += spacing[1]

def __button_cords(__list, __subvar=None, __x=0, __y=0, __x_change=0, __y_change=0):

    __List = []
    
    for __name in __list:
        if __subvar == None:
            __List.append((__name, (__x, __y)))
        else:
            __name = getattr(__name, __subvar)
            __List.append((__name, (__x, __y)))
        if __x_change != 0:
            __x += __x_change
        if __y_change != 0:
            __y += __y_change
    return __List        

def __create_menu(menu, messages, buttons=[], images=[]):

    menu.add_messages(messages)
    menu.add_buttons(buttons)
    menu.add_images(images)

##    for thing in messages:
##        if len(thing) == 4:
##            menu.add_messages(thing[0], thing[1], thing[2], thing[3])
##        else:
##            menu.add_messages(thing[0], thing[1], thing[2], thing[3], Changing=thing[4])
##
##    for thing in buttons:
##        if len(thing) == 2:
##            menu.add_buttons([thing[0], thing[1]])
##        else:
##            menu.add_buttons([thing[0], thing[1], thing[2]])
##
##    for thing in images:
##        menu.add_images(thing[0], thing[1])
##
##    for thing in commands:
##        menu.add_commands(thing[0])

def create(app):

    __plymouth_bg = (app.sprites_dict.get("Plymouth"))
    __window_bg = (app.sprites_dict.get("Window"))

    __cords = app.display_info.cords

    
    #Weapons Menu Outline
    __List = __button_cords(app._weapons_list, "type", -535, -225, 215, 0)
        
    __weapons_menu = graphics.StaticMenu(__window_bg, __colors_dict, [], name="Weapons Menu")
    __create_menu(__weapons_menu, [("Weapons", "dark_green", (0,-315), "large"), ("Weapons", "green", (-5,-315), "large"), ((app._weapons_list[0].name), "white", (0, -150), "medium"),],
                    __List,
                  [(app._weapons_list[0].image, (((__cords[0]/2)-(app._weapons_list[-1].image.get_width()/2)),((__cords[1]/2)-(app._weapons_list[-1].image.get_height()/2))))])
    __weapons_menu.init()


    #Map Menu
    __name = app.map.name()
    __maps_menu = graphics.StaticMenu(__window_bg, __colors_dict, [], name="Maps Menu")
    __create_menu(__maps_menu, [("Maps", "dark_green", (0,-315), "large"), ("Maps", "green", (-5,-315), "large"), (__name, "white", (0,-250), "medium")], [("Plymouth", (0,-75))], [])
    __maps_menu.init()
    

    #Character Menu
    __characters = app.player.characters_dict().values()
    __List = __button_cords(__characters, "name", -535, -200, 0, 70)

    __character_menu = graphics.StaticMenu(__window_bg, __colors_dict, name="Character Menu")    
    __create_menu(__character_menu, [("Characters", "dark_green", (0,-315), "large"), ("Characters", "green", (-5,-315), "large"), (app.player.character, "white", (0,-200), "medium"),
                  (("Level: "+str(app.player.level())), "white", (535,-315), "medium")],
                  __List,
                  [(app.player.image, (((__cords[0]/2)-(app.player.image.get_width()/2)),((__cords[1]/2)-(app.player.image.get_height()/2))))])
    __character_menu.init()


    #Loadout Menu
    __loadout_menu = graphics.Menu(__plymouth_bg, __colors_dict, submenus=[__character_menu, __weapons_menu, __maps_menu], name="Loadout Menu")
    __create_menu(__loadout_menu,
                  [("Loadout", "dark_green", (0,-315), "large"), ("Loadout", "green", (-5,-315), "large")],
                  [("Characters", (0,-75), "Choose your character!"), ("Weapons", (0,0), "Customize your weapons!"), ("Choose Map", (0,75), "Choose the map!")])


    #Controls Menu
    __List = __button_cords([(app.events.get_str(app.events.back)), (app.events.get_str(app.events.up)), (app.events.get_str(app.events.down)),
                                        (app.events.get_str(app.events.left)), (app.events.get_str(app.events.right)), (app.events.get_str(app.events.aim)),
                                        (app.events.get_str(app.events.shoot))], None, 0, -200, 0, 75)
    
    __controls_menu = graphics.StaticMenu(__plymouth_bg, __colors_dict, [], name="Controls Menu")    
    __create_menu(__controls_menu, [("Controls", "dark_green", (0,-315), "large"), ("Controls", "green", (-5,-315), "large")],
                  __List)
    __controls_menu.init()

        
    #Gamma Menu
    __gamma_bg = Surface(__cords)
    __gamma_bg.fill(__colors_dict.get("black"))
    
    __gamma_menu = graphics.Menu(__gamma_bg, __colors_dict, name="Gamma Menu")    
    __create_menu(__gamma_menu, [("Change Gamma: ", "dark_green", (0, -315), "large"), ("Change Gamma: ", "green", (-5, -315), "large"), ("Dark Grey", "white", (-300, -100), "medium"),
                                 ("Grey", "white", (0, -100), "medium"), ("White", "white", (300, -100), "medium"), ("Zombies", "dark_grey", (-300, 0), "medium"), ("Zombies", "grey", (0,0), "medium"),
                                 ("Zombies", "white", (300, 0), "medium"), ("Use the up and down arrow keys to change the gamma", "white", (0,200), "medium"),
                                 ("The messages should look like the color stated above them", "white", (0,255), "medium")])
    

    
    #Gameplay Menu
    __gameplay_menu = graphics.Menu(__plymouth_bg, __colors_dict, [__gamma_menu], name="Gameplay Menu")    
    __create_menu(__gameplay_menu, [("Gameplay", "dark_green", (0,-315), "large"), ("Gameplay", "green", (-5,-315), "large")],
                  [(("FPS: "+str(app._fps)), (0,-75), "Adjust the Frames Per Second!"), ("Change Gamma", (0, 0), "Change the difference between colors!")])
    __gameplay_menu.add_submenu(__gameplay_menu, 0)


    #Stats For Programmers Menu
    __backend = app.display_info.backend()
    __stats_menu = graphics.Menu(__plymouth_bg, __colors_dict, clock=app.clock, name="Stats Menu")    
    __create_menu(__stats_menu, [("Stats for Programmers", "dark_green", (0,-315), "large"), ("Stats for Programmers", "green", (-5,-315), "large"),
                                 (("Running: "+app.__repr__), "white", (0, -235), "medium"), (("Modules: "+app.__module__), "white", (0,-190), "medium"),
                                 (("Display Backend: "+__backend), "white", (0,-145), "medium"), (("Window Type: "+app.display_info.__str__), "white", (0,-100), "medium"),
                                 (("Display Size: {0}".format(__cords)),"white", (0,-55), "medium"), (("License: "+app._license), "white", (0,265), "small"),
                                 (("Copyright: "+app._copyright), "white", (0,300), "small"),])


    #Credits Menu
    __credits_menu = graphics.Menu(__plymouth_bg, __colors_dict, name="Credits Menu")    
    __create_menu(__credits_menu, [("Credits", "dark_green", (0,-315), "large"), ("Credits", "green", (-5,-315), "large"), ("Programmed By: Brendan Beard", "white", (0,-235), "medium"),
                                   ("Graphics By: Brendan Beard", "white", (0,-190), "medium"), ("Published By: AtlasCorporations LLC", "white", (0,-145), "medium"), (app._copyright, "white", (0, 300), "small"),
                                   ("Additional Credits: Pygame (Graphics)", "white", (0,-100), "medium")])

    
    #Options Menu
    __options_menu = graphics.Menu(__plymouth_bg, __colors_dict, [__controls_menu, __gameplay_menu, __stats_menu, __credits_menu], name="Options Menu")
    __create_menu(__options_menu, [("Options", "dark_green", (0,-315), "large"), ("Options", "green", (-5,-315), "large")],
                  [("Controls", (0, -75), "Customize your controls!"), ("Gameplay", (0,0), "Customize your gameplay!"), ("Statistics", (0,75), "Stats for programming and issues!"),
                   ("Credits", (0,150), "Check out the creators!")])


    #Updates Menu
    __updates = app._version.get_tuple()
    __updates_menu = graphics.Menu(__plymouth_bg, __colors_dict, name="Updates Menu")
    __updates_msg(__updates_menu, __updates, (-265, 25))


        #Map Intro
    __info = app.map.map_info()
    __map_intro_menu = graphics.StaticMenu(__gamma_bg, __colors_dict, [], name="Map Intro Menu")
    __create_menu(__map_intro_menu, [(__info[0], "white", (-700,250), "small"), (__info[1], "white", (-700,275), "small"),
                                     (__info[2], "white", (-700,300), "small")])
    for msg in __map_intro_menu.messages:
        msg.get_text_outline(None, 0)
    

    #Title Screen Menu
    __username = app.player.name
    __title_menu = graphics.Menu(__plymouth_bg, __colors_dict, [__loadout_menu, __options_menu, __updates_menu], name="Title Menu")    
    __create_menu(__title_menu, [(app.__name__, "dark_green", (0,-300), "xlarge"), (app.__name__, "green", (-5,-300), "xlarge"), (__username, "white", (-550,300), "small"),
                                 (app._version.version, "white", (550,300), "small"), (app._copyright, "white", (0, 300), "small")],
                  [("Play", (0, -75), "Fight the swarm alone!"), ("Loadout", (0,0), "Customize your character and weapons!"), ("Options", (0, 75), "Change your settings!"),
                   ("Updates", (0,150), "Check out the new features!")])
    __title_menu.add_submenu(__map_intro_menu, 0)


    #Pause Menu    
    __paused_menu = graphics.Menu(__gamma_bg, __colors_dict, [__gamma_menu], name="Pause Menu")    
    __create_menu(__paused_menu, [("Paused", "red", (0,-315), "large")], [("Change Gamma", (0,-75), "Change the difference between colors!"),
                                                                          ("Quit", (0,0), "Save and Quit Game?")])
    __paused_menu.add_submenu(__paused_menu)


    __List = (__title_menu, __character_menu, __weapons_menu, __maps_menu,#__loadout_menu
           __controls_menu, __gameplay_menu, __gamma_menu, __paused_menu, __map_intro_menu)#__options_menu, __stats_menu, __credits_menu, __updates_menu,

    return __List

