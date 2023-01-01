import pygame
from sys import exit
from game import Game

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

game = Game(2, screen)

font = pygame.font.Font(None, 36)
text_bouton = font.render("Lancer la partie", True, (0, 0, 0))
text_bouton_rect = text_bouton.get_rect()
text_bouton_x = screen.get_width() / 2 - text_bouton_rect.width / 2
text_bouton_y = screen.get_height() / 2 - text_bouton_rect.height / 2

button = [text_bouton_x - 10, text_bouton_y + 50, text_bouton_rect.width + 20, text_bouton_rect.height + 20]

inGame = False

def setGame():
    game.destroy()
    game.__init__(2, screen)

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
            elif ((game.game_over or game.wining) and pygame.Rect.collidepoint(game.button,pygame.mouse.get_pos())):
                setGame()
    screen.fill('white')
    if inGame:
        game.update()
    else:
        button = screen.blit(text_bouton, [text_bouton_x, text_bouton_y])

    pygame.display.update()
    clock.tick(50)