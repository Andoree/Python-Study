import pygame as p

p.init()
screen = p.display.set_mode((300, 300))
p.display.set_caption("04(beating)")
clock = p.time.Clock()
running = False
x = 0
expand = True
while not running:
    clock.tick(160)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.circle(screen, (0, 67, 78), [150, 150], 40 + x, 40)
    if expand:
        x += 9
        if x == 90:
            expand = False
    else:
        x -= 1
        if x == 0:
            expand = True
    p.display.flip()
