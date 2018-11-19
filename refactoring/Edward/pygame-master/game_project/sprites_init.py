import pygame as pg


def load_sprite_strip(sprite, amount):
    sprite_strip = []
    for i in range(amount):
        sprite_strip.append(pg.image.load(sprite.format(i + 1)))
    return sprite_strip


# load background
spr_background = load_sprite_strip("sprites/bg/bg_{}.png", 6)

# player sprites
spr_player_attack = load_sprite_strip("sprites/player/player_attack_{}.png", 5)
spr_player_fall = load_sprite_strip("sprites/player/player_fall_{}.png", 2)
spr_player_idle = load_sprite_strip("sprites/player/player_idle_{}.png", 4)
spr_player_jump = load_sprite_strip("sprites/player/player_jump_{}.png", 2)
spr_player_run = load_sprite_strip("sprites/player/player_run_{}.png", 4)

# other sprites
spr_ball_blue = load_sprite_strip("sprites/entities/ball_blue_{}.png", 4)
spr_ball_green = load_sprite_strip("sprites/entities/ball_green_{}.png", 4)
spr_ball_purple = load_sprite_strip("sprites/entities/ball_purple_{}.png", 4)
spr_ball_red = load_sprite_strip("sprites/entities/ball_red_{}.png", 4)
spr_ball_explosion = load_sprite_strip(
    "sprites/other/ball_explosion_{}.png", 3)


