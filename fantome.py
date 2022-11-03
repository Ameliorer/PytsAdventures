import pygame

class Fantome(pygame.sprite.Sprite):
    def __init__(self, groups, listePos, compteur) -> None:
        super().__init__(groups)
        self.passage = listePos
        self.image = pygame.Surface((30, 60))
        self.image.fill('grey')

        self.rect = self.image.get_rect(topleft=(self.passage[compteur][0], self.passage[compteur][1]))
    
    def update(self, compteur):

        if compteur < len(self.passage):
            if self.passage[compteur] == 'kill':
                self.kill()
            else:
                self.rect.x = self.passage[compteur].x
                self.rect.y = self.passage[compteur].y
        else:
            self.kill()