import pygame
from pygame.locals import *

pygame.init()

# affichage de la fenêtre
fen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Chrono")
fpsClock = pygame.time.Clock()

TpsZero = pygame.time.get_ticks()  ## Départ


def temps():
    seconds = (pygame.time.get_ticks() - TpsZero) / 1000
    print(seconds)


continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
        if evenement.type == KEYDOWN:
            if evenement.key == K_ESCAPE:
                continuer = False

    temps()

    pygame.display.flip()
    fpsClock.tick(60)

pygame.quit()