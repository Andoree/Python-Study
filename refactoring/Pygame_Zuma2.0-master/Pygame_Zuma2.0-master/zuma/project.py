import math
import random

import pygame

import About
import Menu
import Test

pygame.init()

tests = True


def go_play():
    Menu.drow()
    while tests:
        if Menu.check == 1:
            start_game()
            Test.drow(scores)
        if Menu.check == 2:
            About.run = True
            About.drow()
        if About.flag:
            Menu.running = True
            Menu.drow()


def start_game():
    width = 800
    height = 800

    size = [width, height]  # An: size hardcode fixed
    screen = pygame.display.set_mode(size)
    fon = pygame.image.load("pictures/fon.jpg")
    clock = pygame.time.Clock()
    speed = 5
    middle = 400
    CONST_100 = 100
    CONST_170 = 170
    MAX_ANGLE = 360  # An: Added MAX_ANGLE
    MY_BALL_SPEED = 13  # An: Added MY_BALL_SPEED
    BALL_OFFSET = 5  # An: BALL_OFFSET added
    BALL_RADIUS = 30  # An: BALL_RADIUS added
    count_of_balls = 0
    moving_balls = []
    # An : Color constants
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (255, 255, 255)
    x = 0
    y = 0
    running = True
    count_for_music = 0
    b = 0
    chick = pygame.image.load('pictures/chick.png')
    duck = pygame.image.load('pictures/duck.png')
    parrot = pygame.image.load('pictures/parrot.png')

    class dulo():
        def __init__(self):
            self.startx = height / 2
            self.starty = width / 2
            self.wid = 5
            self.speed = 4
            self.length = 700
            self.ugol = 0
            # An: + 400 ---> width // 2
            self.endx = math.cos(math.radians(self.ugol)) * self.length + width // 2
            # An: + 400 ---> height // 2
            self.endy = math.sin(math.radians(self.ugol)) * self.length + height // 2

    # класс движухщихся шариков
    class balls():
        def __init__(self):

            self.radius = BALL_RADIUS  # An : 30 ---> BALL_RADIUS
            self.rect = chick.get_rect()
            check = random.randint(0, 2)
            # An : color constants
            if check == 0:
                self.color = RED
            if check == 1:
                self.color = GREEN
            if check == 2:
                self.color = RED + GREEN
            self.x = width - self.radius - BALL_OFFSET
            self.y = self.radius + BALL_OFFSET

    # это класс шариков выстрелов
    class my_ball():
        def __init__(self):
            choose_color = random.randint(0, 2)
            # An : 30 ---> BALL_RADIUS
            self.radius = BALL_RADIUS

            self.x = width // 2  # An: = 400 ---> = width // 2
            self.y = height // 2  # An: = 400 ---> = height // 2
            self.ugol = 0
            self.speed = MY_BALL_SPEED
            # An : color constants
            if choose_color == 0:
                self.color = RED
            if choose_color == 1:
                self.color = GREEN
            if choose_color == 2:
                self.color = RED + GREEN
            self.check = False

    # функция по движению и рисованию шариков, которые движутся по периметру
    def drow_moving_balls():
        running = True
        for ball in moving_balls:
            # An: +5/-5 ---> BALL_OFFSET/-BALL_OFFSET
            if ball.x > ball.radius + speed + BALL_OFFSET and ball.y == ball.radius + BALL_OFFSET:
                ball.x -= speed
                # An: 5 ---> BALL_OFFSET
            elif ball.y < width - ball.radius - BALL_OFFSET \
                    and ball.x == ball.radius + speed + BALL_OFFSET:
                ball.y += speed
                # An: 5 ---> BALL_OFFSET
            elif ball.x < height - ball.radius - BALL_OFFSET \
                    and ball.y == width - ball.radius - BALL_OFFSET:
                ball.x += speed
            elif ball.y > CONST_100 and ball.x == height - ball.radius - BALL_OFFSET:
                ball.y -= speed
            elif ball.x > CONST_100 and ball.y == CONST_100:
                ball.x -= speed
            elif ball.y < width - CONST_100 and ball.x == CONST_100:
                ball.y += speed
            elif ball.x < height - CONST_100 and ball.y == width - CONST_100:
                ball.x += speed
            elif ball.y > CONST_170 and ball.x == height - CONST_100:
                ball.y -= speed
            elif ball.x > CONST_170 and ball.y == CONST_170:
                ball.x -= speed
            elif ball.y < width - CONST_170 and ball.x == CONST_170:
                ball.y += speed
            elif ball.x < height - CONST_170 and ball.y == width - CONST_170:
                ball.x += speed
            elif ball.y > middle and ball.x == height - CONST_170:
                ball.y -= speed
            elif ball.x > middle and ball.y == middle:
                ball.x -= speed
            elif ball.x - ball.radius < middle + ball.radius:
                sound1 = pygame.mixer.Sound('BB.wav')
                sound1.play()
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # Test.well_done_draw(scores)
                running = False
                break  # can delete
            # An : color constants
            if ball.color == RED:
                screen.blit(parrot, (normalize(ball.x), normalize(ball.y)))
            elif ball.color == GREEN:
                screen.blit(duck, (normalize(ball.x), normalize(ball.y)))
            else:
                screen.blit(chick, (normalize(ball.x), normalize(ball.y)))
        return running  # can delete

    def shout_music(count):
        sound1 = pygame.mixer.Sound('Tik.wav')
        sound1.play()

    def normalize(a):
        """
        why
        :param a:
        :return:
        """
        # An : 30 ---> BALL_RADIUS
        return a - BALL_RADIUS

    pygame.mixer.music.load("game_proc.mp3")
    pygame.mixer.music.play()
    next_ball = my_ball()
    current_ball = my_ball()
    shouting_balls = []
    d = dulo()
    global scores
    scores = 0

    while running:
        for event in pygame.event.get():
            # обработка пробела(выстрел)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                count_for_music += 1
                shout_music(count_for_music)
                current_ball = next_ball
                current_ball.ugol = d.ugol
                next_ball = my_ball()
                current_ball.check = True
                shouting_balls.append(current_ball)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                global tests
                tests = False

        screen.blit(fon, (0, 0))
        # An : 400 ---> width, height // 2
        # An : 30 ---> BALL_RADIUS
        # An : color constants
        pygame.draw.circle(screen, BLACK, (width // 2, height // 2), BALL_RADIUS)
        if next_ball.color == RED:
            screen.blit(parrot, (normalize(next_ball.x), normalize(next_ball.y)))
        elif next_ball.color == GREEN:
            screen.blit(duck, (normalize(next_ball.x), normalize(next_ball.y)))
        else:
            screen.blit(chick, (normalize(next_ball.x), normalize(next_ball.y)))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            d.ugol += d.speed
            # An : 360 ---> MAX_ANGLE
            if d.ugol % MAX_ANGLE == 0:
                d.ugol = 0
                # An: 400 ---> height // 2 or width // 2
            d.endx = math.cos(math.radians(d.ugol)) * d.length + width // 2
            d.endy = math.sin(math.radians(d.ugol)) * d.length + height // 2

        if keys[pygame.K_LEFT]:
            d.ugol -= d.speed
            # An : 360 ---> MAX_ANGLE
            if d.ugol % MAX_ANGLE == 0:
                d.ugol = MAX_ANGLE
            d.endx = math.cos(math.radians(d.ugol)) * d.length + width // 2
            d.endy = math.sin(math.radians(d.ugol)) * d.length + height // 2
        # An : color constants
        pygame.draw.line(screen, RED, (d.startx, d.starty), (d.endx, d.endy), d.wid)

        # пробегаемся по массиву всех выстреленных шариков, чтоб изменить координаты
        for ball in shouting_balls:
            # An: < 800 ---> < width
            # An: < 800 ---> < height
            if ball.x < width and ball.x > 0 and ball.y > 0 and ball.y < height and ball.check:
                ball.x += math.cos(math.radians(ball.ugol)) * ball.speed
                ball.y += math.sin(math.radians(ball.ugol)) * ball.speed
                # An : color constants
                if ball.color == RED:
                    screen.blit(parrot, (normalize(int(ball.x)), normalize(int(ball.y))))
                elif ball.color == GREEN:
                    screen.blit(duck, (normalize(int(ball.x)), normalize(int(ball.y))))
                else:
                    screen.blit(chick, (normalize(int(ball.x)), normalize(int(ball.y))))
            else:
                ball.check = False
                shouting_balls.pop(shouting_balls.index(ball))
            for move_ball in moving_balls:
                # An : 30 ---> BALL_RADIUS
                if abs(ball.x - move_ball.x) < BALL_RADIUS \
                        and abs(ball.y - move_ball.y) < BALL_RADIUS:
                    k = 1
                    if ball.color == move_ball.color:
                        k += 1
                        index1 = moving_balls.index(move_ball) - 1
                        index2 = index1 + 1
                        while moving_balls[index1].color == ball.color \
                                and len(moving_balls) - 1 > 0:
                            k += 1
                            moving_balls.pop(index1)
                            index1 -= 1
                            index2 -= 1
                        while moving_balls[index2].color == ball.color \
                                and len(moving_balls) > index2 + 1:
                            k += 1
                            moving_balls.pop(index2)

                        scores += 2 ** k
                    elif ball.color != move_ball.color:
                        # An: 5 ---> BALL_OFFSET
                        scores -= BALL_OFFSET
                    shouting_balls.pop(shouting_balls.index(ball))

        if count_of_balls % MY_BALL_SPEED == 0:
            moving_balls.append(balls())
        count_of_balls += 1

        if not drow_moving_balls():
            running = False

        pygame.display.flip()
        clock.tick(30)


go_play()
pygame.quit()
