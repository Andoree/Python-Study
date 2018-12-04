# An: as menu --> as MainMenu
from MainMenu import Main as MainMenu
# An: Game as game --> Game
from Game import Game
from GameOver import Main as gg
import sys

game_name = "Asteroids"
name = -1
state = 1
score = -1


def exit_game():
    sys.exit()


while 1:
    if state == 1:
        state = MainMenu.load(game_name, score, name)
    elif state == 2:
        state, score = Game.main(Game())
    elif state == 3:
        state, name = gg.load(game_name, str(score))
    elif state == 4:
        exit_game()
