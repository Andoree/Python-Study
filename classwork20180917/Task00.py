import pygame as p

p.init()
screen = p.display.set_mode((300, 300))
p.display.set_caption("Line")
clock = p.time.Clock()
running = False
x = 0
frames = 0
while not running:
    clock.tick(10)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.circle(screen, (80, 20, 249), (100, 150), 30)
    p.draw.line(screen, (80, 255, 70), [2, 100], [x % 300, 100], 190)
    p.draw.circle(screen, (80, 20, 249), (100, 150), 30)
    x += 10
    p.display.flip()
