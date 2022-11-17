import pygame

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
        if actif:                                           # si le reset de la potion n'est pas demandée
            if not self.actif:                              # si la potion n'as pas été déjà utiliser lors de ce round
                match self.action:                          # regarde si le type de la potion existe
                    case "speed+":                          # si il existe
                        player.modificateurs += self.nb     # met en place les différentes modifications
                    case "speed-":
                        player.modificateurs -= self.nb
                    case _:                                 # sinon
                        pass                                # saute l'instruction
                self.nbUtilise += 1                         # augmente le nombre de fois que la potion a été utilisé
                self.actif = True                           # montre que la potion a été utiliser lors de la manche

        else:                                               # si on demande le reset
            if self.actif:                                  # si la potion a été utiliser lors de ce round
                match self.action:                          # regarde si le type de la potion existe
                    case "speed+":                          # si il existe
                        player.modificateurs -= self.nb     # met en place les différentes modifications
                    case "speed-":
                        player.modificateurs += self.nb
                    case _:                                 # sinon
                        pass                                # saute l'instruction
                self.actif = False                          # montre que la potion n'a pas été utiliser lors de la manche
    
    def apear(self):
        if self.nbUtilise == self.nbUtilisable:             # si le nombre d'utilisation maximum a été réaliser
            self.kill()                                     # détruit la potion