import pygame
from sys import exit
import time
from debug import debug
from player import Player
from StaticObstacle import StaticObstacle
from fantome import Fantome
from win import Win
import random

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

sprite1 = pygame.sprite.Group()
collisions = pygame.sprite.Group()
walls = pygame.sprite.Group()
win = pygame.sprite.Group()

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
Win((1060, 440), (200, 260), [win])


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

player = Player(sprite1, walls, win, starterPlayer)

listePosition = []

last_time = time.time()

TpsZero = pygame.time.get_ticks()  # Départ

def temps(reset = False):
    global TpsZero
    seconds = 5 - (pygame.time.get_ticks() - TpsZero) / 1000
    if seconds < 0:
        seconds = 0
    if reset:
        TpsZero = pygame.time.get_ticks()
    return seconds

fini = False
game_over = False

while True:

    dt = time.time() - last_time
    last_time = time.time()

    if temps() <= 0 and not player.cheminTerminé:  # Si le temps est dépassé et que le chemin n'est pas fini
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        test = player.souvenir_pos
        test.append("kill")
        fantome = Fantome(sprite1, test)
        creat = False
        #print(test)

    screen.fill('white')

    win.update(dt)
    win.draw(screen)

    walls.update(dt)

    for spawn in spawns:
        pygame.draw.rect(screen, (255, 51, 51), spawn)


    walls.draw(screen)

    sprite1.update(dt, temps())
    sprite1.draw(screen)

    if player.cheminTerminé and temps()<=0:                     # lorsque le joueur à atteint l'arrivé
        print("player cheminTerminé")
        if not fini:                                            # pas encore utilisé
            print(not fini)                                     #test
            print('fin du parcours')                            #test
            listePosition.append(player.souvenir_pos[:])        # on récupère une copie de la liste de positions parcouru par le joueur jusque la et on l'ajoute à la liste des fantômes
            player.souvenir_pos = []                            # on vide la liste de position du joueur
            for i in range (len(listePosition)):                #on parcourt la liste de listes de positions des fantôme et pour chacun d'entre eux:
                fantome = Fantome(sprite1, listePosition[i])    # on créé un nouveau fantôme
            fini = True                                         # on termine l'instruction (encore pour éviter les problèmes de répétitions une fois que le jeux est finis)
            player.cheminTerminé = False                        # on permet au joueur de récupéré une raison de gagner
            temps(True)                                         # on reset le timer
        else:
            print("fini true")                                  #pas encore utilisé
    else:
        fini = False                                            #pour éviter les problèmes mais pas encore utilisé




    font = pygame.font.Font(None, 36)

    if game_over:

        screen.fill((0, 0, 0))                                      # écran noir
        player.pos.x = 0                                            # le joueur ne peux plus bouger
        player.pos.y = 0                                            # le joueur ne peux plus bouger
        text = font.render("Game Over", True, (255,255,255))        # création du texte "game over"
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = screen.get_height() / 2 - text_rect.height / 2     # on le met au milieu de l'écran
        screen.blit(text, [text_x, text_y])                         # on affiche le "game over"








# AFFICHER LE CHRONO
    surf = pygame.display.get_surface()

    if temps() < 10.0 and not int(str(temps())[0]) %2 == 0:      # pour faire clignoter le texte dans on est en dessous des 10 secondes et quand il est impair

        temps_surf = pygame.font.Font(None, 50).render(str(temps())[:4], True, 'Red')
        temps_rect = temps_surf.get_rect(topleft=(1190, 20))
        surf.blit(temps_surf, temps_rect)

    else :
        temps_surf = pygame.font.Font(None, 50).render(str(temps())[:4], True, 'Black')
        temps_rect = temps_surf.get_rect(topleft=(1190, 20))
        surf.blit(temps_surf, temps_rect)

    #debug(player.pos.x)
    #debug(player.pos.y,20, 40)

    pygame.display.update()
    clock.tick(50)