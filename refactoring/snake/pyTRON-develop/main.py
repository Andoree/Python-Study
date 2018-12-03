import pygame
import time

#
# PARAMETERS
#

# Colors
from player import Player

BLACK = (0, 0, 0)
YELLOW = (229, 226, 71)
CYAN = (118, 214, 202)

BG_COLOR = BLACK
P1_COLOR = CYAN  # player 1 trail color
P2_COLOR = YELLOW  # player 2 trail color

# Window

WIDTH, HEIGHT = 600, 660  # window dimensions
OFFSET = HEIGHT - WIDTH  # vertical space at top of window
WALL_WIDTH = 15
WINDOW_CAPTION = "pyTRON"
GAME_FPS = 60
ENDGAME_SCORE = 10  # An: endgame score

pygame.init()

#
# SETUP
#


# Options
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates window
pygame.display.set_caption(WINDOW_CAPTION)  # sets window title
SCORE_FONT = pygame.font.Font(None, 72)
BOOSTS_FONT = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
check_time = time.time()
start_pos = [50, (HEIGHT - OFFSET) / 2]


def new_game():
    new_p1 = Player(start_pos[0], start_pos[1], (2, 0), P1_COLOR)
    new_p2 = Player(WIDTH - start_pos[0], start_pos[1], (-2, 0), P2_COLOR)
    return new_p1, new_p2


# An: method for eliminating code duplicate
def handle_key(key_event, key_up, key_down, key_left, key_right, key_boost, p_id):
    if key_event.key == key_up:
        objects[p_id].direction = (0, -2)
    elif key_event.key == key_down:
        objects[p_id].direction = (0, 2)
    elif key_event.key == key_left:
        objects[p_id].direction = (-2, 0)
    elif key_event.key == key_right:
        objects[p_id].direction = (2, 0)
    elif key_event.key == key_boost:
        objects[p_id].__boost__()


# An: method for eliminating code duplicate
def process_boost(object, sign, color):
    boosts = BOOSTS_FONT.render("%d boosts" % object.boosts, 1, color)
    boosts_pos = boosts.get_rect()
    boosts_pos.centerx = (WIDTH + sign * (int(boosts.get_width() / 2) + WALL_WIDTH + 10)) % WIDTH
    boosts_pos.centery = \
        OFFSET + int(boosts.get_height() / 2) + WALL_WIDTH + 10

    screen.blit(boosts, boosts_pos)


# create players and add to list
objects = list()
tails = list()
p1, p2 = new_game()
objects.append(p1)
tails.append((p1.rect, '1'))
objects.append(p2)
tails.append((p2.rect, '2'))

players_score = [0, 0]  # current players score

SCREEN_FRAME = [pygame.Rect([0, OFFSET, WALL_WIDTH, HEIGHT]),
                pygame.Rect([0, OFFSET, WIDTH, WALL_WIDTH]),
                pygame.Rect([WIDTH - WALL_WIDTH, OFFSET, WALL_WIDTH, HEIGHT]),
                pygame.Rect([0, HEIGHT - WALL_WIDTH, WIDTH, WALL_WIDTH])]

finish = False
new = False

#
# GAME
#

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finish = True
            # An : eliminated key handle code duplicate
            # === Player 1 === #
            handle_key(event, pygame.K_w, pygame.K_s,
                       pygame.K_a, pygame.K_d, pygame.K_TAB, p_id=0)

            # === Player     2 === #
            handle_key(event, pygame.K_UP, pygame.K_DOWN,
                       pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RSHIFT, p_id=1)

    screen.fill(BG_COLOR)

    for tail_wall in SCREEN_FRAME:
        pygame.draw.rect(screen, (42, 42, 42), tail_wall, 0)  # draws the walls

    for o in objects:
        if time.time() - o.start_boost >= 0.5:  # limits boost to 0.5s
            o.boost = False

        if (o.rect, '1') in tails or (o.rect, '2') in tails \
                or o.rect.collidelist(SCREEN_FRAME) > -1:

            if (time.time() - check_time) >= 0.1:
                check_time = time.time()
                if o.color == P1_COLOR:
                    players_score[1] += 1
                else:
                    players_score[0] += 1
                new = True
                p1, p2 = new_game()
                objects = [p1, p2]
                tails = [(p1.rect, '1'), (p2.rect, '2')]
                break

        else:  # not yet traversed
            tails.append(
                (o.rect, '1')) if o.color == P1_COLOR \
                else tails.append((o.rect, '2'))
        o.__draw__(screen)
        o.__move__()

    for tail_wall in tails:
        if new is True:
            tails = []
            new = False
            break
        if tail_wall[1] == '1':
            pygame.draw.rect(screen, P1_COLOR, tail_wall[0], 0)
        else:
            pygame.draw.rect(screen, P2_COLOR, tail_wall[0], 0)

    score_text = SCORE_FONT.render('%d : %d' % (players_score[0],
                                                players_score[1]),
                                   1,
                                   (255, 255, 51))
    score_text_pos = score_text.get_rect()
    score_text_pos.centerx = int(WIDTH / 2)
    score_text_pos.centery = int(OFFSET / 2)
    screen.blit(score_text, score_text_pos)

    process_boost(objects[0], 1, P1_COLOR)
    process_boost(objects[1], -1, P2_COLOR)
    # An : eliminated code duplicate
    if players_score[0] >= ENDGAME_SCORE or players_score[1] >= ENDGAME_SCORE:
        finish = True

    pygame.display.flip()
    clock.tick(GAME_FPS)

pygame.quit()
