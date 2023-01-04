import pygame

class LevelSelector:

    def __init__(self, nbLevels, screen) -> None:
        self.screen_width, self.screen_height = 1280, 720
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.nbLevels = nbLevels

        self.text_retour = self.font.render("Quitter la partie", True, (0, 0, 0))
        self.text_retour_rect = self.text_retour.get_rect()
        self.text_retour_x = self.screen.get_width() / 2 - self.text_retour_rect.width / 2
        self.text_retour_y = self.screen.get_height() / 2 - self.text_retour_rect.height / 2 + 150

        self.retour = [self.text_retour_x - 10, self.text_retour_y + 50, self.text_retour_rect.width + 20, self.text_retour_rect.height + 20]

    def afficheLevelSelector(self):
        self.screen.fill((255, 255, 255))                                      # écran blanc
        text = self.font.render("Choisissez votre niveau :", True, (0, 0, 0))      # création du texte
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = self.screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = self.screen.get_height() / 3 - text_rect.height / 2     # on le met au milieu de l'écran
        self.screen.blit(text, [text_x, text_y])

        niveau1 = self.font.render(str(1), True, (0, 0, 0))  # création du texte
        text_rect = niveau1.get_rect()  # c'est un rectangle
        text_x = ((1)*self.screen.get_width()) / (self.nbLevels+1) - text_rect.width / 2  # on le met au milieu de l'écran
        text_y = (2*self.screen.get_height()) / 3 - text_rect.height / 2  # on le met au milieu de l'écran
        self.n1 = self.screen.blit(niveau1, [text_x, text_y])

        niveau2 = self.font.render(str(2), True, (0, 0, 0))  # création du texte
        text_rect = niveau2.get_rect()  # c'est un rectangle
        text_x = ((2)*self.screen.get_width()) / (self.nbLevels+1) - text_rect.width / 2  # on le met au milieu de l'écran
        text_y = (2*self.screen.get_height()) / 3 - text_rect.height / 2  # on le met au milieu de l'écran
        self.n2 = self.screen.blit(niveau2, [text_x, text_y])

        niveau3 = self.font.render(str(3), True, (0, 0, 0))  # création du texte
        text_rect = niveau3.get_rect()  # c'est un rectangle
        text_x = ((3)*self.screen.get_width()) / (self.nbLevels+1) - text_rect.width / 2  # on le met au milieu de l'écran
        text_y = (2*self.screen.get_height()) / 3 - text_rect.height / 2  # on le met au milieu de l'écran
        self.n3 = self.screen.blit(niveau3, [text_x, text_y])

        niveau4 = self.font.render(str(4), True, (0, 0, 0))  # création du texte
        text_rect = niveau4.get_rect()  # c'est un rectangle
        text_x = ((4)*self.screen.get_width()) / (self.nbLevels+1) - text_rect.width / 2  # on le met au milieu de l'écran
        text_y = (2*self.screen.get_height()) / 3 - text_rect.height / 2  # on le met au milieu de l'écran
        self.n4 = self.screen.blit(niveau4, [text_x, text_y])

        pygame.draw.rect(self.screen, (175, 175, 175), self.retour)
        self.retur = self.screen.blit(self.text_retour, [self.text_retour_x, self.text_retour_y + 60])

    def update(self):
        self.afficheLevelSelector()