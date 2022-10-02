import pygame
from sys import exit
import time
from debug import debug
from player import Player
from wall import Wall

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

sprite1 = pygame.sprite.Group()


walls = [
    pygame.Rect(0, 0, 1280, 20), pygame.Rect(0, 0, 20, 720),
    pygame.Rect(0, 700, 1280, 20), pygame.Rect(1260, 0, 20, 720),
    ]



player = Player(sprite1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('white')

    sprite1.update()
    sprite1.draw(screen)

    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    pygame.display.update()
    clock.tick(60)

