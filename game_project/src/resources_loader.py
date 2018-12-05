import os
import pygame as pg

GAME_DIR = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(GAME_DIR, os.path.pardir, 'sprites', file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('image loading error')
    return surface.convert()


def load_sound(file):
    file = os.path.join(GAME_DIR, os.path.pardir, 'sounds', file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print('Warning, unable to load, %s' % file)
