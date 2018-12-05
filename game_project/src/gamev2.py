import pygame as pg
from pygame.locals import *

from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_RECT, BACKGROUND_COLOR
from src.enemy import Enemy
from src.resources_loader import load_image, load_sound
from src.player import Player
from src.player_shot import Player_shot
from src.score import Score


def main():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('My_game')
    clock = pg.time.Clock()

    # sprites
    img = load_image('player.png')
    Player.images = [img]
    img = load_image('player_shot.png')
    Player_shot.images = [img]
    img = load_image('enemy_new.png')
    Enemy.images = [img]

    # sounds
    crow_sound = load_sound('crow.wav')
    shot_sound = load_sound('shot.wav')
    shot_sound.set_volume(0.1)

    background = pg.Surface(SCREEN_RECT.size)
    background.fill(BACKGROUND_COLOR)
    screen.blit(background, (0, 0))

    pg.display.flip()

    # Создание контейнеров
    all = pg.sprite.RenderUpdates()
    shots = pg.sprite.Group()
    enemies = pg.sprite.Group()

    # Присвоение контейнеров
    Player.containers = all
    Player_shot.containers = all, shots
    Enemy.containers = all, enemies

    player = Player()
    # Таймеры появлений объектов
    gun_timer = 0
    enemy_spawn_timer = 0
    crow_sound_timer = 0
    score_delta = 0
    score = Score()
    game_over = False

    def check_quit_keys():
        for event in pg.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True

    if pg.font:
        all.add(score)

    # initialiaing fonts
    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 40)
    my_font_bot = pg.font.SysFont('Comic Sans MS', 20)
    text_over = my_font.render('Game over', False, (0, 0, 0))
    text_score = my_font.render('Score: ' + str(score.score), False, (0, 0, 0))
    instruction = my_font_bot.render('Press S to start a new game ', False, (0, 0, 0))

    while player.alive():
        if check_quit_keys():
            break

        key_state = pg.key.get_pressed()
        horiz_direction = key_state[K_RIGHT] - key_state[K_LEFT]
        vert_direction = key_state[K_DOWN] - key_state[K_UP]
        player.move(horiz_direction, vert_direction)

        score_delta = 0

        for shot in shots:
            enemies_hit_list = pg.sprite.spritecollide(shot, enemies, True)
            if len(enemies_hit_list) > 0:
                if crow_sound_timer <= 0:
                    crow_sound.play()
                    crow_sound_timer = Enemy.CROW_SOUND_COOLDOWN
                shot.kill()
                score_delta += len(enemies_hit_list)
        crow_sound_timer -= 1

        if score_delta > 0:
            score.set_score_delta(score_delta)

        d = pg.sprite.spritecollide(player, enemies, True)
        if len(d) > 0:
            player.kill()
            text_score = my_font.render('Score: ' + str(score.score), False, (0, 0, 0))
            game_over = True

        if key_state[K_x]:
            if gun_timer != 0:
                gun_timer = gun_timer - 1
            else:
                Player_shot(player.get_guns()[0])
                Player_shot(player.get_guns()[1])
                shot_sound.play()
                gun_timer = Player_shot.GUN_RELOAD

        if enemy_spawn_timer != 0:
            enemy_spawn_timer = enemy_spawn_timer - 1
        else:
            Enemy()
            enemy_spawn_timer = Enemy.SPAWN_COOLDOWN

        all.clear(screen, background)
        all.update()
        pg.display.update(all.draw(screen))
        clock.tick(60)
    while game_over:
        if check_quit_keys():
            break

        key_state = pg.key.get_pressed()
        if key_state[K_s]:
            main()
            break
        screen.blit(background, (0, 0))
        screen.blit(text_over, (100, 0))
        screen.blit(text_score, (125, 100))
        screen.blit(instruction, (50, 600))
        pg.display.update()
        clock.tick(60)
    pg.quit()


if __name__ == '__main__': main()
