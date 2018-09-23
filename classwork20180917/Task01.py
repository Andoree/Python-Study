import pygame as p

p.init()
screen = p.display.set_mode((1000, 1000))
p.display.set_caption("Line")
clock = p.time.Clock()
cosPhi = 0.5
sinPhi = (3 ** 0.5) / 2
points1 = [[250, 250], [150, 150], [150, 50], [350, 50], [350, 150]]
points2 = [[250, 250], (350, 350), (350, 450), (150, 450), (150, 350)]
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
        p.draw.line(screen, (250, 2, 1), [points2[i][0], points2[i][1]],
                    [points2[(i + 1) % 5][0], points2[(i + 1) % 5][1]], 3)
    for i in range(1, 5):
        points1t0 = (points1[i][0] - points1[0][0]) * cosPhi\
                    + (points1[i][1] - points1[0][1]) * sinPhi
        points1t1 = -(points1[i][0] - points1[0][0]) * sinPhi\
                    + (points1[i][1] - points1[0][1]) * cosPhi
        points1[i][0] = points1t0
        points1[i][1] = points1t1

    p.display.flip()
