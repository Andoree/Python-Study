import random

import pygame
from doodler import Doodler


class DoodleJump:
    '''
    ЭТО ВСЁ НЕ РАБОТАЕТ
    pygame.init()
    pygame.display.set_caption("Doodle Jump")
    platforms = []  # координаты платформ
    img = []
    '''
    GAME_FIELD_EDGE = 700
    UPDATE_PLATFORMS_CONSTANT = 1000
    PLATFORM_POP_CONST = 900
    VERY_BEATIFUL_COSTIL = -50000

    def __init__(self):
        self.window = pygame.display.set_mode((DoodleJump.GAME_FIELD_EDGE, DoodleJump.GAME_FIELD_EDGE))
        self.platforms = [[400, DoodleJump.GAME_FIELD_EDGE, 0]]
        # Не Андрей: третий параметр - стукнулся ли о платформу дудлер
        #  renamed platform to sprite
        self.sprite = pygame.image.load("static/platform_mini.png")
        self.doodler = Doodler()
        self.curr_level = 50
        self.run = True

    def draw_platforms(self):
        global a
        for platform in self.platforms:
            a = random.randint(0, DoodleJump.GAME_FIELD_EDGE)
            if platform[1] > DoodleJump.VERY_BEATIFUL_COSTIL:
                self.window.blit(self.sprite, (platform[0], platform[1] - self.doodler.cameray))
        self.platforms.append([a, self.platforms[-1][1] - 50, 0])

        self.platforms.append([random.randint(0, DoodleJump.GAME_FIELD_EDGE), self.platforms[-1][1] - 100, 0])
        if self.platforms[1][1] - self.doodler.cameray > \
                DoodleJump.PLATFORM_POP_CONST:
            self.platforms.pop(0)

    def update_platforms(self):
        player = pygame.Rect(self.doodler.x,
                             self.doodler.y,
                             self.doodler.image.get_width(),
                             self.doodler.image.get_height())
        # убрал где get_height() '- 10', и починил игру. PROFIT.

        for platform in self.platforms:
            rect = pygame.Rect(platform[0], platform[1],
                               self.sprite.get_width(), self.sprite.get_height())
            if rect.colliderect(player) and self.doodler.gravity and self.doodler.y < platform[
                1] - self.doodler.cameray:
                self.doodler.jump = 15
                self.doodler.gravity = 0

    '''
    нигде не применённый метод
    def isDeath(self):
        if self.doodler.y - self.doodler.cameray > 1000:
            self.platforms = [[0, -100, 0]]
    '''

    def main(self):
        #   platform = Platform()

        while self.run:
            if (self.doodler.y - self.doodler.cameray <
                    DoodleJump.UPDATE_PLATFORMS_CONSTANT):
                self.update_platforms()
            self.draw_platforms()
            self.window.blit(self.doodler.image, [self.doodler.x, self.doodler.y - self.doodler.cameray])
            self.doodler.update()
            pygame.display.update()
            pygame.time.delay(30)
            self.window.fill((0, 220, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        # self.isDeath() ничего не делает

    pygame.quit()


DoodleJump().main()
