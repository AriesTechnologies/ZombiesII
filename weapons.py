def create(): #Call this after the display has been set otherwise there will be an error

    import sprites
    
    __weapons_img_dict = sprites.load_sprites("Weapons") #Returns dict
    __pistol = Weapon("P-77", "Handguns", 25, 5, 60, 10, __weapons_img_dict.get("P-77"))
    __shotgun = Weapon("SS-1", "Shotguns", 55, 3, 75, 15, __weapons_img_dict.get("SS-1"))
    __sniper = Weapon("Longshot", "Snipers", 100, 1, 100, 5, __weapons_img_dict.get("Longshot"))
    __machine_gun = Weapon("Atlas-27B", "Machine Guns", 15, 8, 180, 30, __weapons_img_dict.get("Atlas-27B"))
    __submachine_gun = Weapon("S-25", "SMGs", 10, 10, 200, 20, __weapons_img_dict.get("S-25"))
    __assault_rifle = Weapon("N47-C", "Assault Rifles", 20, 6, 150, 30, __weapons_img_dict.get("N47-C"))

    __weapons_list = (__assault_rifle, __submachine_gun, __machine_gun, __sniper, __shotgun, __pistol)
    __weapons_dict = (dict(enumerate(__weapons_list)))
    return  __weapons_list, __weapons_dict

# --- Weapons Class --- #

class Weapon(object):
    def __init__(self, name, type, damage, shooting_speed, max_ammo, clip_ammo, image):

        self.name = name
        self.type = type
        self.damage = damage
        self.shooting_speed = shooting_speed
        self.max_ammo = max_ammo #Holds maximum amount of ammo at anytime
        self.full_ammo = max_ammo #Holds amount of ammo left in 'bag'
        self.clip_ammo = clip_ammo #Holds maximum amount of ammo in clip
        self.current_ammo = clip_ammo #Holds amount of ammo in clip
        self.packed = False
        self.image = image

    def pack(self):

        if not self.packed:
            self.damage += self.damage*3
            self.shooting_speed += int(self.shooting_speed*1.5)
            self.packed = True

##    def upgradable(self):

