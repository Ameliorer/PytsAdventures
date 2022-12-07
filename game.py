import pygame
import time
from debug import debug
from player import Player
from StaticObstacle import StaticObstacle
from fantome import Fantome
from win import Win
from pot import Pot
from zone import Zone
import random

class Game:
    def __init__(self, place, screen) -> None:
        self.screen_width, self.screen_height = 1280, 720
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        
        self.spriteJoueur = pygame.sprite.Group()
        self.spriteFantome = pygame.sprite.Group()
        self.collisions = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.objs = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.win = pygame.sprite.Group()

        self.creat = True

        self.starterPlayer = []

        self.enJeu = True

        match place:
            case 1:

                StaticObstacle((0, 0), (1280, 20), [self.walls, self.collisions])
                StaticObstacle((0, 700), (1280, 20), [self.walls, self.collisions])
                StaticObstacle((0, 0), (20, 720), [self.walls, self.collisions])
                StaticObstacle((1260, 0), (20, 720), [self.walls, self.collisions])

                # HORIZONTAL

                StaticObstacle((20, 400), (310, 20), [self.walls, self.collisions])
                StaticObstacle((330, 300), (120, 20), [self.walls, self.collisions])
                StaticObstacle((150, 500), (450, 20), [self.walls, self.collisions])
                StaticObstacle((150, 600), (550, 20), [self.walls, self.collisions])
                StaticObstacle((350, 90), (550, 20), [self.walls, self.collisions])
                StaticObstacle((720, 345), (420, 20), [self.walls, self.collisions])
                StaticObstacle((170, 200), (480, 20), [self.walls, self.collisions])
                StaticObstacle((900, 430), (240, 20), [self.walls, self.collisions])
                StaticObstacle((900, 260), (240, 20), [self.walls, self.collisions])
                StaticObstacle((900, 90), (240, 20), [self.walls, self.collisions])
                StaticObstacle((1000, 175), (260, 20), [self.walls, self.collisions])

                # VERTICAL
                StaticObstacle((430, 200), (20, 120), [self.walls, self.collisions])
                StaticObstacle((1120, 260), (20, 90), [self.walls, self.collisions])
                StaticObstacle((150, 90), (20, 200), [self.walls, self.collisions])
                StaticObstacle((150, 500), (20, 110), [self.walls, self.collisions])
                StaticObstacle((700, 345), (20, 275), [self.walls, self.collisions])
                StaticObstacle((580, 300), (20, 220), [self.walls, self.collisions])
                StaticObstacle((900, 20), (20, 240), [self.walls, self.collisions])
                StaticObstacle((900, 440), (20, 180), [self.walls, self.collisions])
                StaticObstacle((1050, 620), (20, 100), [self.walls, self.collisions])

                # ZONE
                Win((1060, 440), (200, 260), [self.win])


                #SPAWN
                self.spawns = [pygame.Rect(390, 220, 40, 80),
                        pygame.Rect(170, 520, 40, 80),
                        pygame.Rect(20, 20, 40, 70),
                        pygame.Rect(860, 20, 40, 70),
                        pygame.Rect(920, 20, 40, 70),
                        pygame.Rect(1080, 280, 40, 70),
                        ]

                #POTIONS
                # potionVitesse = Pot([self.objs], 500, 300, 1, "speed+", 50)
                # potionVitesse = Pot([self.objs], 500, 300, 1, "speed+", 50)
                self.ZoneMort = Zone([self.zones], 700, 350, "mort", 0,0,0)
                PotSpeedp = Pot([self.objs], 500, 300, 15, "speed+", 50, 3)
                self.Spikes = Pot([self.objs], 500, 300, 2, "spikes", 0, 15, 0,0,0)
                # ZoneSpeedp = Zone([self.zones], 700, 350, "speed+", 100,0,0)
                # PotSpeedm = Pot([self.objs], 500, 300, 2, "speed-", 50, 3, 0, 0, 0)
                # ZoneSpeedm = Zone([self.zones], 700, 350, "speed-", 200)
                # PotSpeedm = Pot([self.objs], 500, 300, 2, "freeze", 50, 1, 0,0,0)
                ZoneSpeedm = Zone([self.zones], 700, 350, "freeze", 50,0,0)

            case _:
                pass
        
        for place in self.spawns:
            self.starterPlayer.append((place[0], place[1]))

        random.shuffle(self.starterPlayer)

        self.player = Player(self.spriteJoueur, self.walls, self.spriteFantome, self.win, self.starterPlayer, self.objs, self.zones)

        self.listePosition = []

        self.wining = False

        self.clock = pygame.time.Clock()
        self.TpsZero = pygame.time.get_ticks()  # Départ
        self.TpsZeroBis = pygame.time.get_ticks()  # Départ
        self.last_time = time.time()
        self.compteur = 0
        self.dt = time.time() - self.last_time

        self.fini = False
        self.game_over = False

        self.text_bouton = self.font.render("Recommencer", True, (255, 255, 255))
        self.text_bouton_rect = self.text_bouton.get_rect()
        self.text_bouton_x = self.screen.get_width() / 2 - self.text_bouton_rect.width / 2
        self.text_bouton_y = self.screen.get_height() / 2 - self.text_bouton_rect.height / 2

        self.bouton = [self.text_bouton_x - 10, self.text_bouton_y + 50, self.text_bouton_rect.width + 20, self.text_bouton_rect.height + 20]

    def destroy(self):
        for item in self.spriteJoueur:
            item.kill()
        for item in self.spriteFantome:
            item.kill()
        for item in self.collisions:
            item.kill()
        for item in self.walls:
            item.kill()
        for item in self.objs:
            item.kill()
        for item in self.zones:
            item.kill()
        for item in self.win:
            item.kill()
        self.enJeu = False
        self.spawns = []
    
    def temps(self, reset = False):
        seconds = 18 - (pygame.time.get_ticks() - self.TpsZero) / 1000
        if seconds < 0:
            seconds = 0
        if reset:
            self.TpsZero = pygame.time.get_ticks()
        return seconds

    def temps_attentes(self, reset = False):
        seconds = 1 - (pygame.time.get_ticks() - self.TpsZeroBis) / 1000
        if seconds < 0:
            seconds = 0
        if reset:
            self.TpsZeroBis = pygame.time.get_ticks()
        return seconds
    
    def drawAndUpdate(self):
        self.win.update(self.dt)
        self.win.draw(self.screen)

        self.walls.update(self.dt)

        for spawn in self.spawns:
            pygame.draw.rect(self.screen, (255, 51, 51), spawn)

        self.zones.draw(self.screen)

        self.walls.draw(self.screen)

        for obj in self.objs:
            if not obj.haveBeenActif:
                self.screen.blit(obj.image, obj.rect)

        self.spriteFantome.update(self.compteur)
        self.spriteFantome.draw(self.screen)
        self.compteur += 1

        self.spriteJoueur.update(self.dt, self.temps_attentes(), self.temps())
        self.spriteJoueur.draw(self.screen)

    def nextStartPlayer(self):
        self.compteur = 0
        self.listePosition.append(self.player.souvenir_pos[:])        # on récupère une copie de la liste de positions parcouru par le joueur jusque la et on l'ajoute à la liste des fantômes
        self.player.souvenir_pos = []                            # on vide la liste de position du joueur
        for i in range (len(self.listePosition)):                #on parcourt la liste de listes de positions des fantôme et pour chacun d'entre eux:
            fantome = Fantome(self.spriteFantome, self.listePosition[i], self.compteur)    # on créé un nouveau fantôme
        self.fini = True                                         # on termine l'instruction (encore pour éviter les problèmes de répétitions une fois que le jeux est finis)
        self.player.cheminTerminé = False                        # on permet au joueur de récupéré une raison de gagner
        self.temps(True)

    def afficheChrono(self):
        if self.temps() > 15:
            s = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)  # per-pixel alpha
            s.fill((255, 255, 255, 170))  # notice the alpha value in the color
            self.screen.blit(s, (0, 0))

        surf = pygame.display.get_surface()

        if self.enJeu:
            if self.temps() > 15 :
                affiche = str((self.temps()-14))[0]
                coordonnesX = 600
                coordonnesY = 300
                taille = 100
            else :
                affiche = str(self.temps())[:4]
                coordonnesX = 1190
                coordonnesY = 20
                taille = 50

            if self.temps() < 5.0 :      # changer la couleur du texte
                couleur = "Red"
            else :
                couleur = "Black"

            temps_surf = pygame.font.Font(None, taille).render(affiche, True, couleur)
            temps_rect = temps_surf.get_rect(topleft=(coordonnesX, coordonnesY))
            surf.blit(temps_surf, temps_rect)

    def afficheGameOver(self):
        self.screen.fill((0, 0, 0))                                      # écran noir
        self.player.pos.x = 0                                            # le joueur ne peut plus bouger
        self.player.pos.y = 0                                            # le joueur ne peut plus bouger
        text = self.font.render("Game Over", True, (255, 255, 255))      # création du texte "game over"
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = self.screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = self.screen.get_height() / 2 - text_rect.height / 2     # on le met au milieu de l'écran
        self.screen.blit(text, [text_x, text_y])
        pygame.draw.rect(self.screen, (45, 45, 45), self.bouton)
        self.button = self.screen.blit(self.text_bouton, [self.text_bouton_x, self.text_bouton_y + 60])

    def afficheWin(self):
        self.wining = True
        self.screen.fill((0, 0, 0))                                      # écran noir
        self.player.pos.x = 0                                            # le joueur ne peut plus bouger
        self.player.pos.y = 0                                            # le joueur ne peut plus bouger
        text = self.font.render("Félicitations ! vous avez réussi !", True, (255, 255, 255))  # création du texte
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = self.screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = self.screen.get_height() / 2 - text_rect.height / 2     # on le met au milieu de l'écran
        self.screen.blit(text, [text_x, text_y])

    def majTemps(self):
        self.dt = time.time() - self.last_time
        self.last_time = time.time()

    def update(self):
        self.majTemps()

        self.drawAndUpdate()

        if ( self.temps()<=0 or self.temps_attentes()<=0 ) and self.player.cheminTerminé  :                     # lorsque le joueur à atteint l'arrivé et que le temps d'attente ou le temps total est nul
            if not self.fini:                                        # on reset le timer
                self.nextStartPlayer()
        else:
            self.fini = False                                            #pour éviter les problèmes mais pas encore utilisé


        if ((self.temps() <= 0 and not self.player.cheminTerminé) or (self.player.collisionMort) or self.ZoneMort.game_over or self.Spikes.game_over):  # Si le temps est dépassé et que le chemin n'est pas fini
            self.game_over = True                                                            # ou si on touche le fantome qui se voit et qu'on est pas dans la zone de fin

        if pygame.sprite.spritecollide(self.player, self.win, False):                 # si il y a une collision entre le joueur et la zone de fin
            res = False                                                         # on reset le temps d'attente
        else :                                                              # sinon
            res = True                                                          # il ne se reset pas
        self.temps_attentes(res)

        self.afficheChrono()

        if self.game_over:
            self.afficheGameOver()


        if len(self.listePosition) == len(self.spawns) and len(self.spawns) != 0:
            self.afficheWin()