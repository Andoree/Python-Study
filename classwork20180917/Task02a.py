import pygame as p

p.init()
line_end = 296
screen = p.display.set_mode((300, 300))
p.display.set_caption("02a")
clock = p.time.Clock()
running = False
x = 0
while not running:
    clock.tick(50)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))


    p.draw.line(screen, (140, 140, 140), [2, 100], [400, 100], 58)
    p.draw.line(screen, (0, 255, 0), [6, 100], [2 + x, 100], 50)
    if x != line_end:
        x += 2

    p.display.flip()
