import pygame
from sys import exit
import time
from debug import debug
from player import Player
from StaticObstacle import StaticObstacle
from fantome import Fantome
from win import Win
from pot import Pot
from zone import Zone
import random

pygame.init()
pygame.display.set_caption("Pyt's Adventures")
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

spriteJoueur = pygame.sprite.Group()
spriteFantome = pygame.sprite.Group()
collisions = pygame.sprite.Group()
walls = pygame.sprite.Group()
objs = pygame.sprite.Group()
zones = pygame.sprite.Group()
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

#POTIONS
# potionVitesse = Pot([objs], 500, 300, 1, "speed+", 50)
# potionVitesse = Pot([objs], 500, 300, 1, "speed+", 50)

Spikes = Pot([objs], 500, 300, 2, "spikes", 0, 15, 0,0,0)
ZoneMort = Zone([zones], 700, 350, "mort", 0,0,0)

PotSpeedp = Pot([objs], 500, 300, 2, "speed+", 50, 3, 0, 0, 0)
ZoneSpeedp = Zone([zones], 700, 350, "speed+", 100,0,0)

PotSpeedm = Pot([objs], 500, 300, 2, "speed-", 50, 3, 0, 0, 0)
ZoneSpeedm = Zone([zones], 700, 350, "speed-", 200)

PotSpeedm = Pot([objs], 500, 300, 2, "freeze", 50, 1, 0,0,0)
ZoneSpeedm = Zone([zones], 700, 350, "freeze", 50,0,0)

starterPlayer = []

#zoneAcceleration = Zone([zones], 500, 400, "speed+", 50)

enJeu = True

for place in spawns:
    starterPlayer.append((place[0], place[1]))

random.shuffle(starterPlayer)

player = Player(spriteJoueur, walls, spriteFantome, win, starterPlayer, objs, zones)

listePosition = []

last_time = time.time()

TpsZero = pygame.time.get_ticks()  # Départ
TpsZeroBis = pygame.time.get_ticks()  # Départ

fini = False
game_over = False

compteur = 0

def destroy():
    global spriteJoueur, spriteFantome, collisions, walls, objs, zones, win, spawns, enJeu, temps_surf
    for item in spriteJoueur:
        item.kill()
    for item in spriteFantome:
        item.kill()
    for item in collisions:
        item.kill()
    for item in walls:
        item.kill()
    for item in objs:
        item.kill()
    for item in zones:
        item.kill()
    for item in win:
        item.kill()
    enJeu = False
    spawns = []

def lancer():
    global spriteJoueur, spriteFantome, collisions, walls, objs, zones, win, spawns, enJeu, temps_surf, player, listePosition, last_time, TpsZero, TpsZeroBis, fini, game_over, compteur
    enJeu = True
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

    Win((1060, 440), (200, 260), [win])


    #SPAWN
    spawns = [pygame.Rect(390, 220, 40, 80),
            pygame.Rect(170, 520, 40, 80),
            pygame.Rect(20, 20, 40, 70),
            pygame.Rect(860, 20, 40, 70),
            pygame.Rect(920, 20, 40, 70),
            pygame.Rect(1080, 280, 40, 70),
            ]

    #POTIONS
    # potionVitesse = Pot([objs], 500, 300, 1, "speed+", 50)
    # potionVitesse = Pot([objs], 500, 300, 1, "speed+", 50)

    Spikes = Pot([objs], 500, 300, 2, "spikes", 0, 15, 0,0,0)
    ZoneMort = Zone([zones], 700, 350, "mort", 0,0,0)

    PotSpeedp = Pot([objs], 500, 300, 2, "speed+", 50, 3, 0, 0, 0)
    ZoneSpeedp = Zone([zones], 700, 350, "speed+", 100,0,0)

    PotSpeedm = Pot([objs], 500, 300, 2, "speed-", 50, 3, 0, 0, 0)
    ZoneSpeedm = Zone([zones], 700, 350, "speed-", 200)

    PotSpeedm = Pot([objs], 500, 300, 2, "freeze", 50, 1, 0,0,0)
    ZoneSpeedm = Zone([zones], 700, 350, "freeze", 50,0,0)

    starterPlayer = []

    for place in spawns:
        starterPlayer.append((place[0], place[1]))

    random.shuffle(starterPlayer)

    player = Player(spriteJoueur, walls, spriteFantome, win, starterPlayer, objs, zones)

    listePosition = []

    last_time = time.time()

    TpsZero = pygame.time.get_ticks()  # Départ
    TpsZeroBis = pygame.time.get_ticks()  # Départ

    fini = False
    game_over = False

    compteur = 0

def temps(reset = False):
    global TpsZero
    seconds = 18 - (pygame.time.get_ticks() - TpsZero) / 1000
    if seconds < 0:
        seconds = 0
    if reset:
        TpsZero = pygame.time.get_ticks()
    return seconds

def temps_attentes(reset = False):
    global TpsZeroBis
    seconds = 1 - (pygame.time.get_ticks() - TpsZeroBis) / 1000
    if seconds < 0:
        seconds = 0
    if reset:
        TpsZeroBis = pygame.time.get_ticks()
    return seconds


while True:

    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            destroy()
            lancer()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('white')

    win.update(dt)
    win.draw(screen)

    walls.update(dt)

    for spawn in spawns:
        pygame.draw.rect(screen, (255, 51, 51), spawn)

    zones.draw(screen)

    walls.draw(screen)

    for obj in objs:
        if not obj.haveBeenActif:
            objs.draw(screen)

    spriteFantome.update(compteur)
    spriteFantome.draw(screen)
    compteur += 1

    spriteJoueur.update(dt, temps_attentes(), temps())
    spriteJoueur.draw(screen)

    if ( temps()<=0 or temps_attentes()<=0 ) and player.cheminTerminé  :                     # lorsque le joueur à atteint l'arrivé et que le temps d'attente ou le temps total est nul
        if not fini:                                            # pas encore utilisé
            compteur = 0
            listePosition.append(player.souvenir_pos[:])        # on récupère une copie de la liste de positions parcouru par le joueur jusque la et on l'ajoute à la liste des fantômes
            player.souvenir_pos = []                            # on vide la liste de position du joueur
            for i in range (len(listePosition)):                #on parcourt la liste de listes de positions des fantôme et pour chacun d'entre eux:
                fantome = Fantome(spriteFantome, listePosition[i], compteur)    # on créé un nouveau fantôme
            fini = True                                         # on termine l'instruction (encore pour éviter les problèmes de répétitions une fois que le jeux est finis)
            player.cheminTerminé = False                        # on permet au joueur de récupéré une raison de gagner
            temps(True)                                         # on reset le timer
    else:
        fini = False                                            #pour éviter les problèmes mais pas encore utilisé


    if (temps() <= 0 and not player.cheminTerminé) or (player.collisionMort):  # Si le temps est dépassé et que le chemin n'est pas fini
        game_over = True                                                            # ou si on touche le fantome qui se voit et qu'on est pas dans la zone de fin

    if ZoneMort.game_over or Spikes.game_over:
        game_over = True

    if pygame.sprite.spritecollide(player, win, False):                 # si il y a une collision entre le joueur et la zone de fin
        res = False                                                         # on reset le temps d'attente
    else :                                                              # sinon
        res = True                                                          # il ne se reset pas
    temps_attentes(res)

    if temps() > 15:
        s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((255, 255, 255, 170))  # notice the alpha value in the color
        screen.blit(s, (0, 0))

# AFFICHER LE CHRONO
    surf = pygame.display.get_surface()

    if enJeu:
        if temps() > 15 :
            affiche = str((temps()-14))[0]
            coordonnesX = 600
            coordonnesY = 300
            taille = 100
        else :
            affiche = str(temps())[:4]
            coordonnesX = 1190
            coordonnesY = 20
            taille = 50

        if temps() < 5.0 :      # changer la couleur du texte
            couleur = "Red"
        else :
            couleur = "Black"

        temps_surf = pygame.font.Font(None, taille).render(affiche, True, couleur)
        temps_rect = temps_surf.get_rect(topleft=(coordonnesX, coordonnesY))
        surf.blit(temps_surf, temps_rect)

#--------------------#

    font = pygame.font.Font(None, 36)

    if game_over:
        screen.fill((0, 0, 0))                                      # écran noir
        player.pos.x = 0                                            # le joueur ne peut plus bouger
        player.pos.y = 0                                            # le joueur ne peut plus bouger
        text = font.render("Game Over", True, (255, 255, 255))      # création du texte "game over"
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = screen.get_height() / 2 - text_rect.height / 2     # on le met au milieu de l'écran
        screen.blit(text, [text_x, text_y])                         # on affiche le "game over"


    if len(listePosition) == len(spawns) and len(spawns) != 0:
        screen.fill((0, 0, 0))                                      # écran noir
        player.pos.x = 0                                            # le joueur ne peut plus bouger
        player.pos.y = 0                                            # le joueur ne peut plus bouger
        text = font.render("Félicitations ! vous avez réussi !", True, (255, 255, 255))  # création du texte
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = screen.get_height() / 2 - text_rect.height / 2     # on le met au milieu de l'écran
        screen.blit(text, [text_x, text_y])                         # on affiche le texte




    #debug(player.pos.x)
    #debug(player.pos.y,20, 40)

    debug(player.speed)
    debug(player.modificateurs, 20, 40)

    pygame.display.update()
    clock.tick(50)