from math import pi

import pygame as p

p.init()
screen = p.display.set_mode((400, 400))
p.display.set_caption("05(youtube)")
clock = p.time.Clock()
running = False
x = 0
y = 0

center = 200
radius = 100
rect_side = radius * 2
while not running:
    clock.tick(30)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.arc(screen, (80, 210, 120), [center - radius, center - radius,
                                        rect_side, rect_side], 0, x, 25)
    if x > 1.5 * pi:
        p.draw.arc(screen, (255, 255, 255), [center - radius, center - radius,
                                             rect_side, rect_side], 0, y, 25)
        y += (2 * pi) / 25

    if x < 2 * pi:
        x += (2 * pi) / 99
    if y > x:
        y = 0
        x = 0

    p.display.flip()
