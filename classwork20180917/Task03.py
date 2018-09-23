from math import pi

import pygame as p

p.init()
p.font.init()
myfont = p.font.SysFont('Timew New Roman', 30)

screen = p.display.set_mode((400, 400))
p.display.set_caption("03")
clock = p.time.Clock()
running = False
x = 0
perc = 0
center = 200
radius = 100
rect_side = radius * 2
while not running:
    clock.tick(20)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.arc(screen, (80, 51, 120), [center - radius, center - radius,
                                       rect_side, rect_side], 0, x, 5)
    if x > 2 * pi:
        x = 0
        perc = 0
    x += (2 * pi) / 99
    perc += 1
    text = myfont.render(str(perc) + '%', False, (255, 0, 0))
    screen.blit(text, (center - 15, center))
    p.display.flip()
