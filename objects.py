import pygame.sprite

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.x = hits[0].rect.left - sprite.hit_rect.width# / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.x = hits[0].rect.right# + sprite.hit_rect.width / 2
            sprite.hit_rect.x = sprite.x
    elif dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.y = hits[0].rect.top - sprite.hit_rect.height# / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.y = hits[0].rect.bottom# + sprite.hit_rect.height / 4
            sprite.hit_rect.y = sprite.y
    hits.clear()

def collide_with_object(sprite, group):
    hits = pg.sprite.spritecollide(sprite, group, True, collide_hit_rect)
    if hits:
        return True
    return False

def collide_with_NPC(sprite, group):
    hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    if hits:
        return True
    return False
