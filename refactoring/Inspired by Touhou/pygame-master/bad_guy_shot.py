import math

from helper import SPRITE_SIZE, load_sprite, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame as pg


class BadGuyShot(pg.sprite.Sprite):
    bad_guy_shot_img = load_sprite('spr_enemy_bullet_0.png')

    def __init__(self, pos, player_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = BadGuyShot.bad_guy_shot_img
        self.rect = self.image.get_rect(center=pos)
        self.speed = 4
        self.target_pos = player_pos
        self.pos = pos
        self.vec = (self.target_pos[0] - self.pos[0], self.target_pos[1] - self.pos[1])
        self.distance = math.sqrt((self.vec[0]) ** 2 + (self.vec[1]) ** 2)
        self.normal = (self.vec[0] / round(self.distance), self.vec[1] / round(self.distance))
        self.speed_x = round(self.normal[0] * self.speed)
        self.speed_y = round(self.normal[1] * self.speed)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # An: SPRITE_SIZE instead of hardcode
        if self.rect.y < -SPRITE_SIZE or self.rect.y > SCREEN_HEIGHT + SPRITE_SIZE:
            self.kill()
        if self.rect.x < -SPRITE_SIZE or self.rect.x > SCREEN_WIDTH + SPRITE_SIZE:
            self.kill()
