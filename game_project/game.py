import os

import pygame as pg
from pygame.rect import Rect
from pygame.locals import *

window_width = 400
window_height = 680
rect = Rect(0, 0, window_width, window_height)

game_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(game_dir, 'sprites', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('image loading error')
    return surface.convert()


class Player(pg.sprite.Sprite):
    speed = 8
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=rect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(rect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)






  ##  def __init__(self):
     ##   self.image = self.images[0]


def main():
    pg.init()
    screen = pg.display.set_mode((window_width, window_height))
    pg.display.set_caption('My_game')
    clock = pg.time.Clock()
    img = load_image('player.png')
    Player.images = [img, pg.transform.flip(img, 1, 0)]
    background = pg.Surface(rect.size)

    all = pg.sprite.RenderUpdates()

    # Здесь будут контейнеры объектов
    Player.containers = all
    player = Player()
    while (player.alive()):
        for event in pg.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return

        all.clear(screen, background)
        all.update()
        # Отрисовка всего

        pg.display.update(all.draw(screen))
        clock.tick(60)


    pg.time.wait(1000)
    pg.quit()


if __name__ == '__main__': main()
