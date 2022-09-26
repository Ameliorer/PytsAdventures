import pygame
from sys import exit
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()

screen.fill('white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
