import os

import pygame as pg
from pygame.locals import *

# todo: Создать врагов
# todo: Детектить колиизии
# todo: апдейтить перемещения врагов
window_width = 400
window_height = 680
BACKGROUND_COLOR = (78, 167, 187)
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
        self.rect = self.image.get_rect(midbottom=screen_rect.midbottom)
        self.origtop = self.rect.top

    def move(self, horiz_direction, vert_direction):
        self.rect.move_ip(horiz_direction * self.speed, vert_direction * self.speed)
        self.rect = self.rect.clamp(screen_rect)

    def left_gun_pos(self):
        pos = self.rect.centerx - self.gun_offset
        return pos, self.rect.top

    def right_gun_pos(self):
        pos = self.rect.centerx + self.gun_offset
        return pos, self.rect.top


class Player_shot(pg.sprite.Sprite):
    speed = -15
    images = []
    gun_reload = 5

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=position)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


def main():
    pg.init()
    screen = pg.display.set_mode((window_width, window_height))
    pg.display.set_caption('My_game')
    clock = pg.time.Clock()
    img = load_image('player.png')
    Player.images = [img, pg.transform.flip(img, 1, 0)]
    img = load_image('player_shot.png')
    Player_shot.images = [img]

    background = pg.Surface(screen_rect.size)
    background.fill(BACKGROUND_COLOR)
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Создание контейнеров
    all = pg.sprite.RenderUpdates()
    shots = pg.sprite.Group()

    # Присвоение контейнеров
    Player.containers = all
    Player_shot.containers = all, shots

    player = Player()

    gun_timer = 0

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
        all.clear(screen, background)
        all.update()

        if key_state[K_x]:
            if gun_timer != 0:
                gun_timer = gun_timer - 1
            else:
                Player_shot(player.left_gun_pos())
                Player_shot(player.right_gun_pos())
                gun_timer = Player_shot.gun_reload

        pg.display.update(all.draw(screen))
        clock.tick(60)

    pg.time.wait(1000)
    pg.quit()


if __name__ == '__main__': main()
