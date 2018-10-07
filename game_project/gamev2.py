import os
import random

import pygame as pg
from pygame.locals import *

# todo: Создать врагов
# todo: Детектить колиизии
# todo: апдейтить перемещения врагов
window_width = 400
window_height = 680
BACKGROUND_COLOR = (78, 167, 187)
enemy_size = (30, 30)

player_shot_size = (17, 35)
screen_rect = Rect(0, 0, window_width, window_height)

game_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(game_dir, 'sprites', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('image loading error')
    return surface.convert()


class Player(pg.sprite.Sprite):
    speed = 12
    images = []
    gun_offset = 8

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        # self.image = pg.transform.scale(self.image, player_size)
        self.rect = self.image.get_rect(midbottom=screen_rect.midbottom)
        self.collideRect = pg.rect.Rect((0, 0), (12, 12))
        self.collideRect.midbottom = self.rect.midbottom



    def move(self, horiz_direction, vert_direction):
        self.rect.move_ip(horiz_direction * self.speed, vert_direction * self.speed)
        self.rect = self.rect.clamp(screen_rect)
        self.collideRect.move_ip(horiz_direction * self.speed, vert_direction * self.speed)
        self.collideRect = self.rect.clamp(screen_rect)


    def left_gun_pos(self):
        pos = self.rect.centerx - self.gun_offset + player_shot_size[0] / 2
        return pos, self.rect.top

    def right_gun_pos(self):
        pos = self.rect.centerx + self.gun_offset + player_shot_size[0] / 2
        return pos, self.rect.top

    '''def checkCollision(self, a):
        if self.collideRect.collidepoint(a[0], a[1]) == True:
            print("You clicked on me!")
    '''

class Player_shot(pg.sprite.Sprite):
    speed = -15
    images = []
    GUN_RELOAD = 5

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midtop = position)
        self.image = pg.transform.scale(self.image, player_shot_size)
        self.collideRect = pg.rect.Rect((0, 0), (32, 32))
        self.collideRect.midbottom = self.rect.midbottom


    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()



class Enemy(pg.sprite.Sprite):
    speed = 4
    images = []
    SPAWN_COOLDOWN = 4
    CROW_SOUND_COOLDOWN = 30

    def __init__(self):
        self.x = random.randrange(0, 10) * 40
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(self.x, 0))
        self.image = pg.transform.scale(self.image, enemy_size)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= window_height:
            self.kill()


class dummysound:
    def play(self): pass

def load_sound(file):
    if not pg.mixer: return dummysound()
    file = os.path.join(game_dir, 'sounds', file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()


def main():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((window_width, window_height))
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

    background = pg.Surface(screen_rect.size)
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



    while (player.alive()):
        for event in pg.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            '''if event.type == pg.KEYUP:
                if event.key == pg.K_x:
                    gun_timer = 0'''

        key_state = pg.key.get_pressed()
        horiz_direction = key_state[K_RIGHT] - key_state[K_LEFT]
        vert_direction = key_state[K_DOWN] - key_state[K_UP]
        player.move(horiz_direction, vert_direction)



        # Проверка на то, что враг коснулся нашего
        # blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)

        # Проверка на попадание по врагу. UPD: уничтожает и снаряд

        for shot in shots:
            enemies_hit_list = pg.sprite.spritecollide(shot, enemies, True)
            if len(enemies_hit_list) > 0:
                if crow_sound_timer <= 0:
                    crow_sound.play()
                    crow_sound_timer = Enemy.CROW_SOUND_COOLDOWN
                shot.kill()
        crow_sound_timer -= 1
        '''
        for alien in pg.sprite.groupcollide(shots, enemies, 1, 1).keys():
            crow_sound.play()
'''
        for enemy in pg.sprite.spritecollide(player, enemies, 1):
            player.kill()



        if key_state[K_x]:
            if gun_timer != 0:
                gun_timer = gun_timer - 1
            else:
                Player_shot(player.left_gun_pos())
                Player_shot(player.right_gun_pos())
                shot_sound.play()
                gun_timer = Player_shot.GUN_RELOAD

        if enemy_spawn_timer != 0:
            enemy_spawn_timer = enemy_spawn_timer - 1
        else:
            Enemy()
            enemy_spawn_timer = Player_shot.GUN_RELOAD

        all.clear(screen, background)
        all.update()
        pg.display.update(all.draw(screen))
        clock.tick(60)

    pg.time.wait(1000)
    pg.quit()


if __name__ == '__main__': main()
