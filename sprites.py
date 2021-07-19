from pygame.image import load
from os import getcwd, listdir
__doc__ = """Loads in sprites"""

def load_sprites(path=""):
    
    if path != "":
        path = getcwd()+"\\Images\\"+path
    else:
        path = getcwd()+"\\Images"
    dirs = listdir(path)
    List = []
    for thing in dirs:
        if thing[(len(thing)-4):] == ".png":
            image = load(path+"\\"+thing).convert_alpha()
            List.append(((thing[:-4]), image))

    List = dict(List)
    return List
        
