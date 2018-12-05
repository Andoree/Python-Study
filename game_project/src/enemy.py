import random
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, ENEMY_SIZE

import pygame as pg


class Enemy(pg.sprite.Sprite):
    speed = 4
    images = []
    SPAWN_COOLDOWN = 4
    CROW_SOUND_COOLDOWN = 30

    def __init__(self):
        self.x = random.randrange(0, WINDOW_WIDTH, WINDOW_HEIGHT // 10)
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(self.x, 0))
        self.image = pg.transform.scale(self.image, ENEMY_SIZE)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= WINDOW_HEIGHT:
            self.kill()
