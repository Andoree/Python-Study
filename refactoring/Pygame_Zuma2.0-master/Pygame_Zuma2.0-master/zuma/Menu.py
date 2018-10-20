import pygame

pygame.init()

pygame.display.set_caption("Menu")

height = 800
width = 800
FONT_COLOR = (25, 25, 112)
size = [width, height]
screen = pygame.display.set_mode(size)
chick = pygame.image.load('pictures/chick.png')
duck = pygame.image.load('pictures/duck.png')
parrot = pygame.image.load('pictures/parrot.png')
bg = pygame.image.load('pictures/fon.jpg')
flag = True
pygame.font.init()


def drow_menu():

    fontAcmeL = pygame.font.Font('Acme-Regular.ttf', 80)
    fontAcmeM = pygame.font.Font('Acme-Regular.ttf', 50)

    #An : FONT_COLOR const
    textSurfaceWelcome = fontAcmeL.render('Welcome!',True, FONT_COLOR)
    textSurfacePlay = fontAcmeM.render('Play',True, FONT_COLOR)
    textSurfaceAbout = fontAcmeM.render('About authors', True, FONT_COLOR)
    textSurfaceExit = fontAcmeM.render('Exit', True, FONT_COLOR)



    wellSize = pygame.font.Font.size(fontAcmeL, 'Well done!') #336, 102
    pointSize = pygame.font.Font.size(fontAcmeM, 'You have 1000 points!') #439, 64
    welcomeSize = pygame.font.Font.size(fontAcmeL, 'Welcome!') #318, 102
    playSize = pygame.font.Font.size(fontAcmeM, 'Play') #85, 64
    aboutSize = pygame.font.Font.size(fontAcmeM, 'About authors') #286, 64
    exitSize = pygame.font.Font.size(fontAcmeM, 'Exit') # 79, 64

    screen.blit(bg, (0,0))
    screen.blit(textSurfaceWelcome, (241, 150))
    screen.blit(textSurfacePlay, (357, 300))
    screen.blit(textSurfaceAbout, (257, 400))
    screen.blit(textSurfaceExit, (360, 500))
    screen.blit(chick, (202, 650))
    screen.blit(parrot, (370, 650))
    screen.blit(duck, (538, 650))


check = 0

def drow():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                global check
                check = 1
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                check = 2
                running = False

        drow_menu()

        pygame.display.flip()