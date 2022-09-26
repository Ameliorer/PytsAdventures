import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((30, 60))
        self.image.fill('blue')

        self.rect = self.image.get_rect(topleft = (20, 20))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 5
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
    def update(self):
        self.input()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed
        self.rect.topleft = round(self.pos.x), round(self.pos.y)