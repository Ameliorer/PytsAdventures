import pygame
from sys import exit
import time
from debug import debug
from player import Player
from StaticObstacle import StaticObstacle
from fantome import Fantome
import random

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

sprite1 = pygame.sprite.Group()
collisions = pygame.sprite.Group()
walls = pygame.sprite.Group()

creat = True

# CONTOUR
StaticObstacle((0, 0), (1280, 20), [walls, collisions])
StaticObstacle((0, 700), (1280, 20), [walls, collisions])
StaticObstacle((0, 0), (20, 720), [walls, collisions])
StaticObstacle((1260, 0), (20, 720), [walls, collisions])

# HORIZONTAL

StaticObstacle((20, 400), (310, 20), [walls, collisions])
StaticObstacle((330, 300), (120, 20), [walls, collisions])
StaticObstacle((150, 500), (450, 20), [walls, collisions])
StaticObstacle((150, 600), (550, 20), [walls, collisions])
StaticObstacle((350, 90), (550, 20), [walls, collisions])
StaticObstacle((720, 345), (420, 20), [walls, collisions])
StaticObstacle((170, 200), (480, 20), [walls, collisions])
StaticObstacle((900, 430), (240, 20), [walls, collisions])
StaticObstacle((900, 260), (240, 20), [walls, collisions])
StaticObstacle((900, 90), (240, 20), [walls, collisions])
StaticObstacle((1000, 175), (260, 20), [walls, collisions])

# VERTICAL
StaticObstacle((430, 200), (20, 120), [walls, collisions])
StaticObstacle((1120, 260), (20, 90), [walls, collisions])
StaticObstacle((150, 90), (20, 200), [walls, collisions])
StaticObstacle((150, 500), (20, 110), [walls, collisions])
StaticObstacle((700, 345), (20, 275), [walls, collisions])
StaticObstacle((580, 300), (20, 220), [walls, collisions])
StaticObstacle((900, 20), (20, 240), [walls, collisions])
StaticObstacle((900, 440), (20, 180), [walls, collisions])
StaticObstacle((1050, 620), (20, 100), [walls, collisions])

# ZONE
win = pygame.Rect(1060, 440, 200, 260)

#SPAWN

spawns = [pygame.Rect(390, 220, 40, 80),
          pygame.Rect(170, 520, 40, 80),
          pygame.Rect(20, 20, 40, 70),
          pygame.Rect(860, 20, 40, 70),
          pygame.Rect(920, 20, 40, 70),
          pygame.Rect(1080, 280, 40, 70),
          ]

starterPlayer = []

for place in spawns:
    starterPlayer.append((place[0], place[1]))

random.shuffle(starterPlayer)

print(starterPlayer)

player = Player(sprite1, walls, starterPlayer[0])


last_time = time.time()

while True:

    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] and creat:
        test = player.souvenir_pos
        test.append("kill")
        fantome = Fantome(sprite1, test)
        creat = False
        #print(test)

    screen.fill('white')

    walls.update(dt)

    for spawn in spawns:
        pygame.draw.rect(screen, (255, 51, 51), spawn)

    pygame.draw.rect(screen, (153, 255, 153), win)

    walls.draw(screen)


    sprite1.update(dt)
    sprite1.draw(screen)


    #debug(player.pos.x)
    #debug(player.pos.y,20, 40)

    pygame.display.update()
