import pygame as p

p.init()
width = 400
height = 100
screen = p.display.set_mode((width, height))
p.display.set_caption('06')
clock = p.time.Clock()
running = False
x = 0
rect_height = 30
rect_width = 100
rect_distance = 20
color_delta = 70
start = 0


def draw_rect(i, x):
    if i + rect_width < x:
        p.draw.line(screen, [10 + color_delta * (i // (rect_width + rect_distance)),
                             55 + color_delta * (i // (rect_width + rect_distance)),
                             38 + color_delta * (i // (rect_width + rect_distance))],
                                [i, 50], [i + rect_width, 50], rect_height)


while not running:
    clock.tick(80)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = True
    screen.fill((255, 255, 255))
    for i in range(0, 3):
        draw_rect(start + (rect_distance + rect_width) * i, x)
    x += 2
    if x > width:
        x = 0
    p.display.flip()
