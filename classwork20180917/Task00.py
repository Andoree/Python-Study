import pygame as p

p.init()
screen = p.display.set_mode((300, 100))
p.display.set_caption("00")
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
    p.draw.line(screen, (80, 255, 70), [2, 50], [x % 300, 50], 10)
    x += 10
    p.display.flip()
