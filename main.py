import pygame
from sys import exit
from debug import debug
from player import Player

pygame.init()
sprite1 = pygame.sprite.Group()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()

player = Player(sprite1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('white')
    sprite1.update()
    sprite1.draw(screen)
    pygame.display.update()
    clock.tick(60)