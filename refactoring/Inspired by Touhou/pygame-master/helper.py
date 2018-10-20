import pygame as pg

MUSIC_PATH = 'audio/'
SPRITE_PATH = 'sprites/'


def load_sprite(path):
    image = pg.image.load(SPRITE_PATH + path)
    return image


def load_sound(path):
    sound = pg.mixer.Sound(MUSIC_PATH + path)
    return sound
