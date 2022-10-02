import pygame

class StaticObstacle (pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=pos)