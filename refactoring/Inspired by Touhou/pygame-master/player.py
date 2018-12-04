import pygame as pg

from helper import load_sprite, SPRITE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, load_sound, FIELD_MARGIN
from shot import Shot


class Player(pg.sprite.Sprite):
    player_imgs = (
        load_sprite('spr_player.png'),
        load_sprite('spr_player_hit.png'),
    )
    player_sounds = (
        load_sound('player_shoot.wav'),
        load_sound('player_hit.wav')
    )

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = Player.player_imgs[0]
        self.rect = self.image.get_rect(center=pos)
        self.radius = 20
        self.rect.centerx =SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 5
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.width = SPRITE_SIZE  # Player size hardcode fixed
        self.height = SPRITE_SIZE  # Player size hardcode fixed
        self.speed = 3
        self.low_speed = 1
        self.cooldown = 75
        self.firing_speed = 8
        self.last_shot = pg.time.get_ticks()
        self.last_hit = pg.time.get_ticks()
        self.score = 0
        self.lives = 3
        self.snd_player_shoot = Player.player_sounds[0]  # An
        self.snd_player_hit = Player.player_sounds[1]  # An
        self.snd_player_shoot.set_volume(0.1)
        self.snd_player_hit.set_volume(0.5)
        self.iframes = [False, 500]

    def shoot(self, now, all_sprites, bullets):
        self.snd_player_shoot.play()
        self.last_shot = now
        new_shot1 = Shot((self.pos[0] + 8, self.pos[1]), self.firing_speed)
        new_shot2 = Shot((self.pos[0] + 24, self.pos[1]), self.firing_speed)
        all_sprites.add(new_shot1)
        all_sprites.add(new_shot2)
        bullets.add(new_shot1)
        bullets.add(new_shot2)

    # An : optimized sprite changing
    def hit(self):
        now = pg.time.get_ticks()
        if self.iframes[0] == False:
            self.snd_player_hit.play()
            self.iframes[0] = True
            self.lives -= 1
            self.image = Player.player_imgs[1]
            self.last_hit = now
        if now - self.last_hit >= self.iframes[1]:
            self.image = Player.player_imgs[0]
            self.last_hit = now
            pg.display.flip()
            self.iframes[0] = False

    # keys = {'right':False, 'down':False, 'left':False, 'up':False}
    def update(self):
        print(self.image)
        keys = pg.key.get_pressed()
        self.pos = (self.rect.x, self.rect.y)
        player_pos = self.pos
        # An: LOW_SPEED_THRESHOLD, changed get_height()
        # and get_width() to constants
        if keys[pg.K_LSHIFT]:
            if keys[pg.K_LEFT] and self.rect.x > FIELD_MARGIN:
                self.rect.x -= self.low_speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.low_speed
                elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT - self.height):
                    self.rect.y += self.low_speed
            elif keys[pg.K_RIGHT] and self.rect.x < (SCREEN_WIDTH - self.width):
                self.rect.x += self.low_speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.low_speed
                elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT  - self.height):
                    self.rect.y += self.low_speed
            elif keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                self.rect.y -= self.low_speed
            elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT - self.height):
                self.rect.y += self.low_speed
        else:
            if keys[pg.K_LEFT] and self.rect.x > FIELD_MARGIN:
                self.rect.x -= self.speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.speed
                elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT - self.height):
                    self.rect.y += self.speed
            elif keys[pg.K_RIGHT] and self.rect.x < (SCREEN_WIDTH - self.width):
                self.rect.x += self.speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.speed
                elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT - self.height):
                    self.rect.y += self.speed
            elif keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                self.rect.y -= self.speed
            elif keys[pg.K_DOWN] and self.rect.y < (SCREEN_HEIGHT - self.height):
                self.rect.y += self.speed
        if keys[pg.K_z]:
            now = pg.time.get_ticks()
            if now - self.last_shot >= self.cooldown:
                self.shoot(now)
