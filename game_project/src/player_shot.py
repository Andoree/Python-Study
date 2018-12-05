import pygame as pg
from src.constants import PLAYER_SHOT_SIZE


class Player_shot(pg.sprite.Sprite):
    speed = -15
    images = []
    GUN_RELOAD = 5

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midtop=position)
        self.image = pg.transform.scale(self.image, PLAYER_SHOT_SIZE)
        self.collideRect = pg.rect.Rect((0, 0), (32, 32))
        self.collideRect.midbottom = self.rect.midbottom

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()
