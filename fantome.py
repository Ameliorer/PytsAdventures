import pygame

class Fantome(pygame.sprite.Sprite):
    def __init__(self, groups, listePos, compteur) -> None:
        super().__init__(groups)
        self.passage = listePos
        self.image = pygame.Surface((30, 60))
        self.image.fill('grey')

        self.rect = self.image.get_rect(topleft=(self.passage[compteur][0], self.passage[compteur][1]))
    
    def update(self, compteur):

        if compteur < len(self.passage):                        # si le compteur est inferieur au len de la liste de positions
            if self.passage[compteur] == 'kill':                    # si dans la liste de positions on trouve 'kill'
                self.kill()                                             # on tue le fantome
            else:                                                   #si dans la liste de positions on ne trouve pas 'kill'
                self.rect.x = self.passage[compteur].x                  # on affiche le fantome à sa place
                self.rect.y = self.passage[compteur].y
        else:                                                   # si le compteur est supérieur ou égal au len de la liste de positions
            self.kill()                                             # on tue le fantome