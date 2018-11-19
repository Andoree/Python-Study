import math
import random
import time

import pygame as pg

import helper

pg.init()
height = 480
width = 640
fps = 60
SPRITE_SIZE = 32  # An: sprite  size const
FIELD_MARGIN = 5  # An: const for low speed
FONT_COLOR = (0, 128, 0)  # An: FONT_COLOR const
clock = pg.time.Clock()
win = pg.display.set_mode((width, height))
pg.display.set_caption('TRIANGLE DX')

# An: FONT_COLOR const
font = pg.font.Font("Retroville NC.ttf", 40)
font_1 = pg.font.Font("Retroville NC.ttf", 15)
jap_font = pg.font.Font("glasstown_nbp.ttf", 45)
font_scores = pg.font.Font("Retroville NC.ttf", 15)
jap_text = jap_font.render("スッパ ツリアングル DX", True, FONT_COLOR)
text = font.render("SUPER TRIANGLE DX", True, FONT_COLOR)
text_to_play = font_1.render("press SPACE to play", True, FONT_COLOR)
text_dead = font.render("GAME OVER", True, FONT_COLOR)
text_to_play_again = font_1.render("press any key to play again", True, FONT_COLOR)

coordinates = [(606, 4), (572, 4), (538, 4)]
lives_image = helper.load_sprite('heart.png')

snd_startup = helper.load_sound('game_start.wav')
snd_startover = helper.load_sound('start_over.wav')

snd_startover.set_volume(0.2)
bgm = pg.mixer.music.load('audio/Jakovich - Mood Swings.mp3')

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()
bad_bullets = pg.sprite.Group()
global difficulty


class Player(pg.sprite.Sprite):
    player_imgs = (
        helper.load_sprite('spr_player.png'),
        helper.load_sprite('spr_player_hit.png'),
    )

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = Player.player_imgs[0]
        self.rect = self.image.get_rect(center=pos)
        self.radius = 20
        self.rect.centerx = width / 2
        self.rect.bottom = height - 5
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
        self.snd_player_shoot = helper.load_sound('player_shoot.wav')  # An
        self.snd_player_hit = helper.load_sound('player_hit.wav')  # An
        self.snd_player_shoot.set_volume(0.1)
        self.snd_player_hit.set_volume(0.5)
        self.iframes = [False, 500]

    def shoot(self, now):
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
        # An: LOW_SPEED_THRESHOLD
        if keys[pg.K_LSHIFT]:
            if keys[pg.K_LEFT] and self.rect.x > FIELD_MARGIN:
                self.rect.x -= self.low_speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.low_speed
                elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                    self.rect.y += self.low_speed
            elif keys[pg.K_RIGHT] and self.rect.x < (win.get_width() - self.width):
                self.rect.x += self.low_speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.low_speed
                elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                    self.rect.y += self.low_speed
            elif keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                self.rect.y -= self.low_speed
            elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                self.rect.y += self.low_speed
        else:
            if keys[pg.K_LEFT] and self.rect.x > FIELD_MARGIN:
                self.rect.x -= self.speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.speed
                elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                    self.rect.y += self.speed
            elif keys[pg.K_RIGHT] and self.rect.x < (win.get_width() - self.width):
                self.rect.x += self.speed
                if keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                    self.rect.y -= self.speed
                elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                    self.rect.y += self.speed
            elif keys[pg.K_UP] and self.rect.y > FIELD_MARGIN:
                self.rect.y -= self.speed
            elif keys[pg.K_DOWN] and self.rect.y < (win.get_height() - self.height):
                self.rect.y += self.speed
        if keys[pg.K_z]:
            now = pg.time.get_ticks()
            if now - self.last_shot >= self.cooldown:
                self.shoot(now)


class Enemy(pg.sprite.Sprite):
    enemy_img = helper.load_sprite('spr_enemy0.png') # An: sprite loading
    shoot_sound = helper.load_sound('enemy_shoot.wav')
    def __init__(self, pos, hp=1, speed=3):
        pg.sprite.Sprite.__init__(self)
        self.image = Enemy.enemy_img
        self.rect = self.image.get_rect()
        self.e_score = 25
        self.rect.x = random.randrange(width - self.rect.width)
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

    def shoot(self):
        self.snd_enemy_shoot.play()
        new_shot = BadGuyShot(self.pos)
        all_sprites.add(new_shot)
        bad_bullets.add(new_shot)

    def update(self):
        self.pos = (self.rect.x, self.rect.y)
        if self.rect.y > win.get_height():
            self.kill()
        if self.rect.x > win.get_width():
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
                self.shoot()
            self.can_shoot = False
            if now - self.start_time >= self.stop_time:
                self.distance = self.dist


class EnemyX(Enemy):
    # An : optimized sound and sprites
    enemy_x_img = helper.load_sprite('spr_enemy1.png')
    shoot_sound = helper.load_sound('enemy_shoot.wav')
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


class Shot(pg.sprite.Sprite):
    # An: image loading
    shot_img = helper.load_sprite('spr_player_bullet_0.png')

    def __init__(self, pos, speed):
        pg.sprite.Sprite.__init__(self)
        self.image = Shot.shot_img
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 15:
            self.kill()


class BadGuyShot(pg.sprite.Sprite):
    bad_guy_shot_img = helper.load_sprite('spr_enemy_bullet_0.png')

    def __init__(self, pos):
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
        if self.rect.y < -SPRITE_SIZE or self.rect.y > win.get_height() + SPRITE_SIZE:
            self.kill()
        if self.rect.x < -SPRITE_SIZE or self.rect.x > win.get_width() + SPRITE_SIZE:
            self.kill()


def start_screen():
    win.fill((10, 10, 30))
    win.blit(text, (320 - text.get_width() // 2, 200 - text.get_height() // 2))
    win.blit(jap_text, (310 - jap_text.get_width() // 2, 255 - jap_text.get_height() // 2))
    win.blit(text_to_play, (text_to_play.get_width(), 448 - text_to_play.get_height()))
    pg.display.flip()
    pg.display.update()
    quit_start = False
    while not quit_start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                quit_start = True
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                snd_startup.play()
                time.sleep(1)
                quit_start = True
                step()


def spawn_enemies(d, t_pos):
    for i in range(d):
        m = random.choice([EnemyX, Enemy])(t_pos)
        all_sprites.add(m)
        enemies.add(m)


def step():
    player = Player((width / 2, height - 64))
    global player_pos
    player_pos = player.pos
    player.lives = 3
    player.scores = 0
    difficulty = 1
    all_sprites.add(player)
    pg.mixer.music.play(-1)

    game_run = True
    spawn_enemies(difficulty, player.pos)
    while game_run:
        clock.tick(fps)
        player_pos = player.pos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        all_sprites.update()
        player.update()

        if len(enemies) == 0:
            spawn_enemies(random.randrange(4, 8), player.pos)

        bullets_hit_enemy = pg.sprite.groupcollide(enemies, bullets, True, True)
        for hit in bullets_hit_enemy:
            player.score += hit.e_score

        enemies_hit_player = pg.sprite.spritecollide(player, enemies, False, pg.sprite.collide_circle)
        if enemies_hit_player:
            player.hit()

        bullets_hit_player = pg.sprite.spritecollide(player, bad_bullets, False, pg.sprite.collide_circle)
        if bullets_hit_player:
            player.hit()

        if player.score // 1000 and player.lives > 3:
            player.lives += 1
        if player.score > difficulty * 50:
            difficulty += 1

        if player.lives == 0:
            pg.mixer.music.stop()
            gameover_screen(player.score)
        # An: FONT_COLOR const
        win.fill((10, 10, 30))
        win.blit(font_scores.render("scores : ", True, FONT_COLOR), (4, 4))
        # An: FONT_COLOR constant
        win.blit(font_scores.render("scores : " + str(player.score), True, FONT_COLOR), (4, 4))

        for i in range(player.lives):
            win.blit(lives_image, (coordinates[i][0], coordinates[i][1]))
        all_sprites.draw(win)
        pg.display.update()


def gameover_screen(score):
    font_scores = pg.font.Font("Retroville NC.ttf", 25)
    # An: FONT_COLOR constant
    text_scores = font_scores.render("scores : " + str(score), True, FONT_COLOR)

    win.fill((10, 10, 30))
    win.blit(text_dead, (320 - text_dead.get_width() // 2, 240 - text_dead.get_height() // 2))
    win.blit(text_to_play_again, (320 - text_to_play_again.get_width() // 2, 448 - text_to_play_again.get_height()))
    win.blit(text_scores, (320 - text_scores.get_width() // 2, text_scores.get_height() + 250))

    pg.display.flip()
    pg.display.update()

    for sprite in all_sprites:
        sprite.kill()
    quit_start = False
    while not quit_start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                quit_start = True
            if event.type == pg.KEYDOWN:
                snd_startover.play()
                quit_start = True
                time.sleep(2)
                step()


start_screen()
pg.quit()
