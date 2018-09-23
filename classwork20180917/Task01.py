import math

import pygame as p

p.init()
screen = p.display.set_mode((1000, 1000))
p.display.set_caption("01")
clock = p.time.Clock()
phi = math.pi / 6
points1 = [[500, 500], [400, 400], [400, 300], [600, 300], [600, 400]]
points2 = [[500, 500], [600, 600], [600, 700], [400, 700], [400, 600]]
center = 500
running = False
x = 0
while not running:
    clock.tick(3)
    screen.fill((255, 255, 255))
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    for i in range(0, 5):
        p.draw.line(screen, (250, 2, 1), [points1[i][0], points1[i][1]],
                    [points1[(i + 1) % 5][0], points1[(i + 1) % 5][1]], 3)
    for i in range(0, 5):
        p.draw.line(screen, (2, 255, 1), [points2[i][0], points2[i][1]],
                    [points2[(i + 1) % 5][0], points2[(i + 1) % 5][1]], 3)
    for i in range(1, 5):
        points1t0 = center + (points1[i][0] - center) * math.cos(phi) - \
                    (points1[i][1] - center) * math.sin(phi)
        points1t1 = center + (points1[i][0] - center) * math.sin(phi) + \
                    (points1[i][1] - center) * math.cos(phi)
        points1[i][0] = points1t0
        points1[i][1] = points1t1

    for i in range(1, 5):
        points2t0 = center + (points2[i][0] - center) * math.cos(phi) - \
                    (points2[i][1] - center) * math.sin(phi)
        points2t1 = center + (points2[i][0] - center) * math.sin(phi) + \
                (points2[i][1] - center) * math.cos(phi)
        points2[i][0] = points2t0
        points2[i][1] = points2t1

    p.display.flip()
