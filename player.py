import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, obstacles):
        super().__init__(group)
        self.image = pygame.Surface((30, 60))
        self.image.fill('blue')

        self.rect = self.image.get_rect(topleft=(20, 20))
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 250
        self.obstacles = obstacles

        self.souvenir_position = []
    
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

    def collision(self, direction):
        walls = pygame.sprite.spritecollide(self, self.obstacles, False)
        if walls:
            if direction == 'hori':
                for wall in walls:
                    # a droite
                    if self.rect.right >= wall.rect.left and self.old_rect.right <= wall.old_rect.left:
                        self.rect.right = wall.rect.left
                        self.pos.x = self.rect.x

                    # a gauche
                    if self.rect.left <= wall.rect.right and self.old_rect.left >= wall.old_rect.right:
                        self.rect.left = wall.rect.right
                        self.pos.x = self.rect.x

            if direction == 'verti':
                for wall in walls:
                    # a bas
                    if self.rect.bottom >= wall.rect.top and self.old_rect.bottom <= wall.old_rect.top:
                        self.rect.bottom = wall.rect.top
                        self.pos.y = self.rect.y

                    # a haut
                    if self.rect.top <= wall.rect.bottom and self.old_rect.top >= wall.old_rect.bottom:
                        self.rect.top = wall.rect.bottom
                        self.pos.y = self.rect.y
        
    def update(self, dt):
        self.souvenir_position.append(self.old_rect)
        self.old_rect = self.rect.copy()
        self.input()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision('hori')

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision('verti')
