import pygame as pg

from game import entities, JUMP_COUNT
from sprites_init import spr_ball_explosion


# extend this to draw entity
# extends pygame.sprite.Sprite
class Drawable(pg.sprite.Sprite):

    def __init__(self, x=0, y=0, image_index=0, image_speed=0,
                 sprite=[], origin_x=0, origin_y=0):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image_index = image_index
        self.image_speed = image_speed
        self.sprite = sprite
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.rect = sprite[0].get_rect()

    def update(self):
        self.rect.x = self.x - self.origin_x
        self.rect.y = self.y - self.origin_y

    def draw_rect(self, surface):
        pg.draw.rect(surface, (255, 0, 0),
                     pg.Rect(self.rect.x, self.rect.y,
                             self.rect.width, self.rect.height))

    def draw_self(self, surface):
        if len(self.sprite) > 0:
            if self.image_index >= len(self.sprite) - 1:
                self.image_index = 0;
            self.image_index += self.image_speed
            surface.blit(self.sprite[round(self.image_index)],
                         (self.x - self.origin_x, self.y - self.origin_y))


class Ball(Drawable):

    # call this instead of kill() to create explosion
    def explode(self):
        entities.add(Explosion(self.x, self.y, 0, 0.1,
                               spr_ball_explosion, spr_ball_explosion[0].get_width() // 2,
                               spr_ball_explosion[0].get_height() // 2))
        self.kill()


class Explosion(Drawable):

    # destroys itself after animation
    def draw_self(self, surface):
        if self.image_index >= len(self.sprite) - 1:
            self.kill()
        self.image_index += self.image_speed
        surface.blit(self.sprite[round(self.image_index)],
                     (self.x - self.origin_x, self.y - self.origin_y))


class Player(Drawable):

    def __init__(self, x=0, y=0, image_index=0, image_speed=0,
                 sprite=[], origin_x=0, origin_y=0, speed=2):
        Drawable.__init__(self, x, y, image_index, image_speed,
                          sprite, origin_x, origin_y)
        self.speed = speed
        self.right = False
        self.in_air = False
        self.jump_count = JUMP_COUNT
        self.attack = False

    # to change animation sprites (jump, fall, idle etc.)
    def set_sprite(self, sprite):
        self.sprite = sprite
        self.rect = sprite[0].get_rect()

    # to change animation speed
    def set_image_speed(self, image_speed):
        self.image_speed = image_speed

    # change sprite direction
    def draw_self(self, surface):
        if self.image_index + self.image_speed >= len(self.sprite) - 1:
            self.image_index = 0
        self.image_index += self.image_speed
        if not self.right:
            surface.blit(self.sprite[round(self.image_index)],
                         (self.x - self.origin_x, self.y - self.origin_y))
        else:
            surface.blit(pg.transform.flip(self.sprite[round(self.image_index)],
                                           True, False), (self.x - self.origin_x, self.y - self.origin_y))
