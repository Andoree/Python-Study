import pygame as p

p.init()
screen = p.display.set_mode((300, 300))
p.display.set_caption("Line")
clock = p.time.Clock()
running = False
x = 0
while not running:
    clock.tick(1000)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))


    p.draw.line(screen, (140, 140, 140), [2, 100], [400, 100], 58)
    p.draw.line(screen, (0, 255, 0), [6, 100], [2 + x, 100], 50)
    if x != 296:
        x += 2

    p.display.flip()
