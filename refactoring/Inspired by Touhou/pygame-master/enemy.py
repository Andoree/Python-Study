import random

import pygame as pg

from bad_guy_shot import BadGuyShot
from helper import load_sprite, load_sound, SCREEN_WIDTH, SPRITE_SIZE, SCREEN_HEIGHT


class Enemy(pg.sprite.Sprite):
    enemy_img = load_sprite('spr_enemy0.png')  # An: sprite loading
    shoot_sound = load_sound('enemy_shoot.wav')

    def __init__(self,all_sprites, bad_bullets, pos, hp=1, speed=3):
        pg.sprite.Sprite.__init__(self)
        self.image = Enemy.enemy_img
        self.rect = self.image.get_rect()
        self.e_score = 25
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = -5
        self.radius = int(self.rect.width * .85 / 2)
        self.start_time = pg.time.get_ticks()
        # An: SPRITE_SIZE
        self.distance = random.randint(SPRITE_SIZE // 2, SPRITE_SIZE)
        self.dist = self.distance
        self.stop_time = 750
        self.speed = speed
        self.hp = hp
        self.can_shoot = True
        self.player_pos = pos
        self.pos = pos
        self.movement_pattern = 1  # random.randint(1,3)
        self.snd_enemy_shoot = Enemy.shoot_sound
        self.snd_enemy_shoot.set_volume(0.1)
        self.all_sprites = all_sprites
        self.bad_bullets = bad_bullets

    def shoot(self, all_sprites, bad_bullets):
        self.snd_enemy_shoot.play()
        new_shot = BadGuyShot(self.pos, self.player_pos)
        all_sprites.add(new_shot)
        bad_bullets.add(new_shot)

    def update(self):
        self.pos = (self.rect.x, self.rect.y)
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
        if self.rect.x < - 5:
            self.kill()
        if self.movement_pattern == 1:
            self.movement_pattern_1()
        elif self.movement_pattern == 2:
            self.movement_pattern_2()

    def movement_pattern_1(self):
        now = pg.time.get_ticks()
        if self.distance > 0:
            self.rect.y += self.speed
            self.distance -= 1
        if self.distance == 0:
            if self.can_shoot:
                self.shoot(self.all_sprites, self.bad_bullets)
            self.can_shoot = False
            if now - self.start_time >= self.stop_time:
                self.distance = self.dist

