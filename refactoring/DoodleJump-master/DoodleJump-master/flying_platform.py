import pygame


class Platform(pygame.sprite.Sprite):
    start = (0, 0)
    end = (0, 0)
    doodler = 9
    image = pygame.image.load('static/platform_mini.png')
    # подгрузка спрайта для каждой
    # новой платформы нейтрализована

    def __init__(self):
      #  super(Platform, self).__init__() - бесполезная строка кода
        self.image = Platform.image
        self.rect = self.image.get_rect()
