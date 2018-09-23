import pygame as p

p.init()
screen = p.display.set_mode((400, 100))
p.display.set_caption('02b')
clock = p.time.Clock()
running = False
x = 0
length = 380
bar_height = 30
rect_height = 20
rect_width = 33
rect_distance = 5
offset_top = 5
while not running:
    clock.tick(100)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    p.draw.line(screen, (170, 170, 170), [2, 50], [2 + length, 50], bar_height)
    i = 0
    while (i < x % (2 + length)):
        if i < x:
            p.draw.line(screen, (63, 167, 231), [i + 2, 50 + offset_top],
                        [2 + i + rect_width, 50 + offset_top], rect_height)
            i += rect_width + rect_distance
    x += 2
    p.display.flip()
