import pygame as pg

from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SHOT_SIZE, SCREEN_RECT


class Player(pg.sprite.Sprite):
    speed = 12
    images = []
    gun_offset = 8

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH, WINDOW_HEIGHT))#screen_rect.midbottom)
        self.collideRect = pg.rect.Rect((0, 0), (12, 12))
        self.collideRect.midbottom = self.rect.midbottom

    def move(self, horiz_direction, vert_direction):
        self.rect.move_ip(horiz_direction * self.speed, vert_direction * self.speed)
        self.rect = self.rect.clamp(SCREEN_RECT)
        self.collideRect.move_ip(horiz_direction * self.speed, vert_direction * self.speed)
        self.collideRect = self.rect.clamp(SCREEN_RECT)

    def get_guns(self):
        pos1 = self.rect.centerx - self.gun_offset + PLAYER_SHOT_SIZE[0] / 2
        pos2 = self.rect.centerx + self.gun_offset + PLAYER_SHOT_SIZE[0] / 2
        return (pos1, self.rect.top), (pos2, self.rect.top)