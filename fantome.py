import pygame

class Fantome(pygame.sprite.Sprite):
    def __init__(self, groups, listePos) -> None:
        super().__init__(groups)
        self.compteur = 0
        self.passage = listePos
        self.image = pygame.Surface((30, 60))
        self.image.fill('grey')

        self.rect = self.image.get_rect(topleft=(self.passage[self.compteur][0], self.passage[self.compteur][1]))
    
    def update(self, dt, temps):
        self.compteur += 1

        if self.compteur < len(self.passage):
            if self.passage[self.compteur] == 'kill':
                self.kill()
            else:
                self.rect.x = self.passage[self.compteur].x
                self.rect.y = self.passage[self.compteur].y
        else:
            self.kill()