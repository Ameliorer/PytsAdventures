import pygame

class Zone (pygame.sprite.Sprite):
    def __init__(self, group, posx, posy, action,nb = 0, tx = 200, ty = 200):
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

        self.nb = nb
        
        self.use = False

    def util(self, player, actif = False):          # voir Pot, le fonctionnement est le même
        if actif:
            if not self.use:
                match self.action:
                    case "speed+":
                        player.modificateurs += self.nb
                    case "speed-":
                        player.modificateurs -= self.nb
                    case _:
                        pass
            self.use = True
        else:
            if self.use:
                match self.action:
                    case "speed+":
                        player.modificateurs -= self.nb
                    case "speed-":
                        player.modificateurs += self.nb
                    case _:
                        pass
            self.use = False