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
            case "freeze":
                self.image.fill('blue')
            case _:
                self.image.fill('black')

        self.posx = posx
        self.posy = posy
        self.rect = self.image.get_rect(topleft=(posx, posy))

        self.nb = nb
        
        self.use = False

        self.actif = False
        self.haveBeenActif = False

        self.game_over = False

    def util(self, player, actif = False):          # voir Pot, le fonctionnement est le même
        if actif:
            if not self.actif:
                self.haveBeenActif = True
                match self.action:
                    case "speed+":
                        player.modificateurs += self.nb
                    case "speed-":
                        player.modificateurs -= self.nb
                    case "mort":
                        self.game_over = True
                    case "freeze":
                        player.modificateurs -= player.speedBase
                    case _:
                        pass
                self.actif = True
        else:
            if self.actif:
                match self.action:
                    case "speed+":
                        player.modificateurs -= self.nb
                    case "speed-":
                        player.modificateurs += self.nb
                    case "mort":
                        self.game_over = False
                    case "freeze":
                        player.modificateurs += player.speedBase
                    case _:
                        pass
                self.actif = False