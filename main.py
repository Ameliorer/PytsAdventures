import pygame
from sys import exit
from game import Game
from LevelSelector import LevelSelector

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

image = pygame.image.load("imageLogo.png")

game = Game(1, screen)
LevelSelector = LevelSelector(3, screen)

font = pygame.font.Font("font.ttf", 36)

text_bouton = font.render("Lancer la partie", True, (0, 0, 0))
text_bouton_rect = text_bouton.get_rect()
text_bouton_x = screen.get_width() / 2 - text_bouton_rect.width / 2
text_bouton_y = screen.get_height() / 2 - text_bouton_rect.height / 2 - 30


text_bouton_level = font.render("Choisir le niveau", True, (0, 0, 0))
text_bouton_rect_level = text_bouton_level.get_rect()
text_bouton_level_x = screen.get_width() / 2 - text_bouton_rect_level.width / 2
text_bouton_level_y = screen.get_height() / 2 - text_bouton_rect_level.height / 2 + 30

text_bouton_exit = font.render("Quitter le jeu", True, (0, 0, 0))
text_bouton_rect_exit = text_bouton_exit.get_rect()
text_bouton_exit_x = screen.get_width() / 2 - text_bouton_rect_exit.width / 2
text_bouton_exit_y = screen.get_height() / 2 - text_bouton_rect_exit.height / 2 + 90


button = [text_bouton_x - 10, text_bouton_y + 50, text_bouton_rect.width + 20, text_bouton_rect.height + 20]
button_level = [text_bouton_level_x, text_bouton_level_y, text_bouton_rect_level.width, text_bouton_rect_level.height]
button_exit = [text_bouton_exit_x, text_bouton_exit_y, text_bouton_rect_exit.width, text_bouton_rect_exit.height]

inSuiteGame = False
inGame = False
inLevelSelector = False

listeNiveau = [1, 2, 3]

def setGame():
    global listeNiveau
    game.destroy()
    niveau = listeNiveau.pop(0)
    game.__init__(niveau, screen)

def cleanGame():
    global inSuiteGame, listeNiveau, inGame
    inSuiteGame = False
    listeNiveau = [1, 2, 3]
    inGame = False

def setGameParticulier(x: int):
    game.destroy()
    game.__init__(x, screen)

def setLevelSelector():
    game.destroy()
    LevelSelector.__init__(3, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEBUTTONUP:
            #game.destroy()
            #game.__init__(1, screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((not inGame) and pygame.Rect.collidepoint(button,pygame.mouse.get_pos())):
                inSuiteGame = True
                inGame = True
                setGame()

            elif ((not inGame) and (not inLevelSelector) and pygame.Rect.collidepoint(button_exit,pygame.mouse.get_pos())):
                pygame.quit()
                exit()

            elif ((not inLevelSelector) and pygame.Rect.collidepoint(button_level,pygame.mouse.get_pos())):
                inLevelSelector = True
                setLevelSelector()

            elif (inLevelSelector):
                if (pygame.Rect.collidepoint(LevelSelector.n1 ,pygame.mouse.get_pos())):
                    inGame = True
                    inLevelSelector = False
                    setGameParticulier(1)

                if (pygame.Rect.collidepoint(LevelSelector.n2 ,pygame.mouse.get_pos())):
                    inGame = True
                    inLevelSelector = False
                    setGameParticulier(2)

                if (pygame.Rect.collidepoint(LevelSelector.n3 ,pygame.mouse.get_pos())):
                    inGame = True
                    inLevelSelector = False
                    setGameParticulier(3)

                if (pygame.Rect.collidepoint(LevelSelector.retur,pygame.mouse.get_pos())):
                    inLevelSelector = False

            elif (game.game_over):
                if (pygame.Rect.collidepoint(game.button,pygame.mouse.get_pos())):
                    inGame = True
                    inLevelSelector = False
                    game.recommencer()

                if (pygame.Rect.collidepoint(game.retur,pygame.mouse.get_pos())):
                    cleanGame()
            elif (game.wining):
                if (pygame.Rect.collidepoint(game.retur,pygame.mouse.get_pos())):
                    cleanGame()

    screen.fill('white')

    if inSuiteGame and game.wining and listeNiveau != []:
        setGame()

    if inGame:
        game.update()

    elif inLevelSelector :
        LevelSelector.update()

    else:
        screen.blit(image, [0, 0])
        button = screen.blit(text_bouton, [text_bouton_x, text_bouton_y])
        button_level = screen.blit(text_bouton_level, [text_bouton_level_x, text_bouton_level_y])
        button_exit = screen.blit(text_bouton_exit, [text_bouton_exit_x, text_bouton_exit_y])

    pygame.display.update()
    clock.tick(50)