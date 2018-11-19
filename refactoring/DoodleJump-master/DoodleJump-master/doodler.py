import pygame


class Doodler(pygame.sprite.Sprite):
    jumpCount = 10
    x = 600
    y = 600
    sprite_dir = 'static/'
    isJump = False
    speed = 25  # Not Andrey: скорость дудлера по горизонтали
    images = []
    SHIFT_THRESHOLD = 200 # порог срабатывания смещения карты вынесен в константу

    '''
    Изображения больше не подгружаются при каждом апдейте.
    Загрузка спрайта вынесена в отдельный метод
    '''

    def load_sprites(path):
        Doodler.images = [
            pygame.image.load(path + 'corgi-small-left-new-eyes.png'),
            pygame.image.load(path + 'corgi-small-right-new-eyes.png')
        ]

    def __init__(self):
       # super(Doodler, self).__init__() - не понял, что это было.
       # Закомменчивание ничего не изменило
        Doodler.load_sprites('static/')
        self.image = Doodler.images[0]
        self.rect = self.image.get_rect()
        self.jump = 5
        self.gravity = 0
        self.cameray = 0
        self.delta = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.image = Doodler.images[1]
        if keys[pygame.K_RIGHT] and self.x < Doodler.x: # changed hardcoded number to
            # Doodler.x
            self.x += self.speed
            self.image = Doodler.images[0]

        if not self.jump:
            self.y += self.gravity
            self.gravity += 1
        elif self.jump:
            self.y -= self.jump
            self.jump -= 1
        if self.y - self.cameray < Doodler.SHIFT_THRESHOLD:
            self.cameray -= 10
