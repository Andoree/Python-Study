import random

from enemy import Enemy
from helper import SPRITE_SIZE, load_sprite, load_sound
import pygame as pg

class EnemyX(Enemy):
    # An : optimized sound and sprites
    enemy_x_img = load_sprite('spr_enemy1.png')
    shoot_sound = load_sound('enemy_shoot.wav')

    def __init__(self, pos, hp=1, speed=5):
        pg.sprite.Sprite.__init__(self)
        self.image = EnemyX.enemy_x_img
        self.rect = self.image.get_rect()
        self.e_score = 50
        # self.rect.x = random.choice([0, 640])
        self.rect.y = random.randrange(50, 200, 40)
        self.radius = int(self.rect.width * .85 / 2)
        # vars for movement_pattern 1
        self.start_time = pg.time.get_ticks()
        # An: SPRITE_SIZE
        self.distance = random.randint(SPRITE_SIZE // 2, SPRITE_SIZE)
        self.dist = self.distance
        self.stop_time = 750

        self.speed = speed
        self.hp = hp
        self.can_shoot = True
        self.cooldown = 500
        self.last_shot = pg.time.get_ticks()
        self.player_pos = pos
        self.pos = pos
        self.movement_pattern = 1  # random.randint(1,3)
        self.snd_enemy_shoot = EnemyX.shoot_sound
        self.snd_enemy_shoot.set_volume(0.1)
        self.type = random.choice([1, 2])
        if self.type == 1:
            self.rect.x = 0
        else:
            self.rect.x = 640

    def movement_pattern_1(self):
        now = pg.time.get_ticks()
        if self.type == 1:
            self.rect.x += 2
        else:
            self.rect.x -= 2
        if now - self.last_shot >= self.cooldown:
            self.last_shot = now
            self.shoot()