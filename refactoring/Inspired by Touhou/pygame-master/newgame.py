
import random
import time

import pygame as pg

from enemy import Enemy
from enemy_x import EnemyX
from helper import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_COLOR, load_sprite, load_sound, SPRITE_SIZE, fps
from player import Player

pg.init()

clock = pg.time.Clock()
win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

enemies_coordinates = [(606, 4), (572, 4), (538, 4)]
lives_image = load_sprite('heart.png')

snd_startup = load_sound('game_start.wav')
snd_startover = load_sound('start_over.wav')

snd_startover.set_volume(0.2)
bgm = pg.mixer.music.load('audio/Jakovich - Mood Swings.mp3')

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()
bad_bullets = pg.sprite.Group()
global difficulty


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
    player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT - 64))
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
        #player_pos = player.pos
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
            win.blit(lives_image, (enemies_coordinates[i][0], enemies_coordinates[i][1]))
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
