import pygame
import pytmx

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Maps:
    def __init__(self):

        self.__dict ={0 : "Plymouth", 1: "Lost City", 2 : "Mansion", 3 : "Chernobyl"}
        self.__info_dict = {"Plymouth" : ("Sometime in the 1620's", "Plymouth, The New World", "12:00:00")}
        self.__map = "Plymouth"

        self.get_map(0)
        self.name = lambda: self.__map
        self.map_info = lambda: self.__info

    def get_map(self, index):

        self.__map = self.__dict.get(index)
        self.__info = self.__info_dict.get(self.__map)


class TiledMap:
    def __init__(self, filename):
        
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.temp_surface = pg.Surface((self.width, self.height))

    def render(self, temp_surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        temp_surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

        return temp_surface

class Camera:
    def __init__(self, width, height):
        
        import pygame.Rect
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)
        
                        
