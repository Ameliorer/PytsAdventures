from socket import create_connection
import pygame
from sys import exit
import time
from debug import debug
from player import Player
from StaticObstacle import StaticObstacle
from fantome import Fantome

creat = True
pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

sprite1 = pygame.sprite.Group()
collisions = pygame.sprite.Group()
walls = pygame.sprite.Group()


StaticObstacle((0, 0), (1280, 20), [walls, collisions])
StaticObstacle((0, 700), (1280, 20), [walls, collisions])
StaticObstacle((0, 0), (20, 720), [walls, collisions])
StaticObstacle((1260, 0), (20, 720), [walls, collisions])
StaticObstacle((200, 50), (500, 20), [walls, collisions])
StaticObstacle((200, 250), (120, 20), [walls, collisions])
StaticObstacle((250, 50), (20, 200), [walls, collisions])

player = Player(sprite1, walls)

last_time = time.time()

while True:

    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(player.souvenir_pos)
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] and creat:
        test = player.souvenir_pos
        test.append("kill")
        fantome = Fantome(sprite1, test)
        creat = False
        print(test)

    screen.fill('white')

    walls.update(dt)


    walls.draw(screen)

    sprite1.update(dt)
    sprite1.draw(screen)

    #    for wall in walls:
    #    pygame.draw.rect(screen, (0, 0, 0), wall)

    pygame.display.update()