import pygame
import time


# An: moved player class to special file
class Player:
    def __init__(self, x, y, direction, color):
        self.x = x  # player x coord
        self.y = y  # player y coord
        self.speed = 1  # player speed
        self.direction = direction  # player direction
        self.color = color
        self.boost = False  # is boost active
        self.start_boost = time.time()  # used to control boost length
        self.boosts = 3
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2,
                                2)  # player rect objectdw

    def __draw__(self, screen):
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2, 2)  # redefines rect
        pygame.draw.rect(screen, self.color, self.rect,
                         0)  # draws player onto screen

    def __move__(self):
        if not self.boost:  # player isn't currently boosting
            self.x += self.direction[0]
            self.y += self.direction[1]
        else:
            self.x += self.direction[0] * 2
            self.y += self.direction[1] * 2

    def __boost__(self):
        if self.boosts > 0:
            self.boosts -= 1
            self.boost = True
            self.start_boost = time.time()
