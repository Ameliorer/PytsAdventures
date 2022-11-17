import pygame
# from objetInteractif import ObjetInteractif

class Pot (pygame.sprite.Sprite):
    def __init__(self, group, posx, posy, nbUtilisable, action,nb = 0, tx = 10, ty = 10):
        super().__init__(group)
        self.type = "potion"

        self.image = pygame.Surface((tx, ty))

        self.action = action

        match self.action:
            case "speed+":
                self.image.fill('yellow')
            case "speed-":
                self.image.fill('brown')
            case _:
                self.image.fill('black')

        self.rect = self.image.get_rect(topleft=(posx, posy))

        self.actif = False

        self.nbUtilisable = nbUtilisable
        self.nbUtilise = 0

        self.nb = nb

    def use(self, player, actif = False):
        if actif:
            if not self.actif:
                match self.action:
                    case "speed+":
                        player.speed += self.nb
                    case _:
                        pass
                self.nbUtilise += 1
                self.actif = True
        else:
            if self.actif:
                match self.action:
                    case "speed+":
                        player.speed -= self.nb
                    case _:
                        pass
            self.actif = False
    
    def apear(self):
        if self.nbUtilise == self.nbUtilisable:
            self.kill()