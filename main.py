import pygame
from sys import exit
from game import Game
from LevelSelector import LevelSelector
from random import randint

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

game = Game(1, screen)
LevelSelector = LevelSelector(3, screen)

font = pygame.font.Font(None, 36)

text_bouton = font.render("Lancer la partie", True, (0, 0, 0))
text_bouton_rect = text_bouton.get_rect()
text_bouton_x = screen.get_width() / 2 - text_bouton_rect.width / 2
text_bouton_y = screen.get_height() / 2 - text_bouton_rect.height / 2 - 30


text_bouton_level = font.render("Choisir le niveau", True, (0, 0, 0))
text_bouton_rect_level = text_bouton_level.get_rect()
text_bouton_level_x = screen.get_width() / 2 - text_bouton_rect_level.width / 2
text_bouton_level_y = screen.get_height() / 2 - text_bouton_rect_level.height / 2 + 30


button = [text_bouton_x - 10, text_bouton_y + 50, text_bouton_rect.width + 20, text_bouton_rect.height + 20]
button_level = [text_bouton_level_x, text_bouton_level_y, text_bouton_rect_level.width, text_bouton_rect_level.height]

inGame = False
inLevelSelector = False

def setGame():
    game.destroy()
    game.__init__(randint(1, 4), screen)

def setLevelSelector():
    game.destroy()
    LevelSelector.__init__(4, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEBUTTONUP:
            #game.destroy()
            #game.__init__(1, screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((not inGame) and pygame.Rect.collidepoint(button,pygame.mouse.get_pos())):
                inGame = True
                setGame()

            elif ((not inLevelSelector) and pygame.Rect.collidepoint(button_level,pygame.mouse.get_pos())):
                inLevelSelector = True
                setLevelSelector()

            elif ((game.game_over or game.wining) and pygame.Rect.collidepoint(game.button,pygame.mouse.get_pos())):
                setGame()
    screen.fill('white')
    if inGame:
        game.update()

    elif inLevelSelector :
        LevelSelector.update()

    else:
        button = screen.blit(text_bouton, [text_bouton_x, text_bouton_y])
        button_level = screen.blit(text_bouton_level, [text_bouton_level_x, text_bouton_level_y])

    pygame.display.update()
    clock.tick(50)