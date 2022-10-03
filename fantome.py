import pygame

class fantome(pygame.sprite.Sprite):
    def __init__(self, groups, listePos) -> None:
        super().__init__(*groups)
        self.compteur = 0
        self.passage = listePos
        self.image = pygame.Surface((30, 60))
        self.image.fill('red')

        self.rect = self.image.get_rect(topleft=self.passage[self.compteur])
    
    def run(self):
        self.compteur += 1

        if self.compteur < self.passage.length:
            self.rect.x = self.passage[self.compteur].x
            self.rect.y = self.passage[self.compteur].y