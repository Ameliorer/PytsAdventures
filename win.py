import pygame


class Win (pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill((153, 255, 153))
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()
