import pygame
from sys import exit
from game import Game

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

game = Game(1, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEBUTTONUP:
            #game.destroy()
            #game.__init__(1, screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((game.game_over or game.win)and pygame.Rect.collidepoint(game.button,pygame.mouse.get_pos())):
                game.destroy()
                game.__init__(1, screen)
    game.update()
    
    pygame.display.update()
    clock.tick(50)