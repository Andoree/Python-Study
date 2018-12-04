import pygame as pg

from helper import load_sprite


class Shot(pg.sprite.Sprite):
    # An: image loading
    shot_img = load_sprite('spr_player_bullet_0.png')

    def __init__(self, pos, speed):
        pg.sprite.Sprite.__init__(self)
        self.image = Shot.shot_img
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 15:
            self.kill()

