import os

import pygame as pg

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MUSIC_PATH = os.path.join(PROJECT_PATH, 'audio')
print(MUSIC_PATH)
SPRITE_PATH = 'sprites/'
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
fps = 60
SPRITE_SIZE = 32  # An: sprite  size const
FIELD_MARGIN = 5  # An: const for low speed
FONT_COLOR = (0, 128, 0)  # An: FONT_COLOR const


def load_sprite(path):
    image = pg.image.load(SPRITE_PATH + path)
    return image


def load_sound(path):
    sound = pg.mixer.Sound(os.path.join(MUSIC_PATH, path))
    return sound
