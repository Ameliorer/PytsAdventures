import pygame

class LevelSelector:

    def __init__(self, nbLevels, screen) -> None:
        self.screen_width, self.screen_height = 1280, 720
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.nbLevels = nbLevels

    def afficheLevelSelector(self):
        self.screen.fill((255, 255, 255))                                      # écran blanc
        text = self.font.render("Choisissez votre niveau :", True, (0, 0, 0))      # création du texte
        text_rect = text.get_rect()                                 # c'est un rectangle
        text_x = self.screen.get_width() / 2 - text_rect.width / 2       # on le met au milieu de l'écran
        text_y = self.screen.get_height() / 3 - text_rect.height / 2     # on le met au milieu de l'écran
        self.screen.blit(text, [text_x, text_y])

        for i in range (self.nbLevels):
            text = self.font.render(str(i+1), True, (0, 0, 0))  # création du texte
            text_rect = text.get_rect()  # c'est un rectangle
            text_x = ((i+1)*self.screen.get_width()) / (self.nbLevels+1) - text_rect.width / 2  # on le met au milieu de l'écran
            text_y = (2*self.screen.get_height()) / 3 - text_rect.height / 2  # on le met au milieu de l'écran
            self.screen.blit(text, [text_x, text_y])

    def update(self):

        self.afficheLevelSelector()
