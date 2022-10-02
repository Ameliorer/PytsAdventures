import pygame
from sys import exit
import time
from debug import debug
from player import Player

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

sprite1 = pygame.sprite.Group()
collisions = pygame.sprite.Group()
walls = pygame.sprite.Group()


StaticObstacle((0,0),(1280,20),[walls,collisions])
StaticObstacle((0, 700),(1280,20),[walls,collisions])




player = Player(sprite1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('white')

    sprite1.update()
    sprite1.draw(screen)

    #    for wall in walls:
    #    pygame.draw.rect(screen, (0, 0, 0), wall)

    pygame.display.update()
    clock.tick(60)

