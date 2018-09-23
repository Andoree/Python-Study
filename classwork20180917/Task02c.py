import pygame as p

p.init()
screen = p.display.set_mode((400, 100))
p.display.set_caption("02c")
clock = p.time.Clock()
running = False
x = 0
red = 255
green = 0
length = 380
delta = length / 255
while not running:
    clock.tick(40)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.line(screen, (140, 140, 140), [2, 50], [2 + length, 50], 58)
    p.draw.line(screen, (red % 255, green % 255, 0), [2, 50], [(2 + x) % length, 50], 50)
    x += delta
    red -= 1
    green += 1
    p.display.flip()
