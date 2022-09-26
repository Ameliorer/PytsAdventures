import pygame
from sys import exit
from debug import debug

pygame.init()
screen = pygame.display.set_mode((978, 694))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
