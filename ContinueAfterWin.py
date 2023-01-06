import pygame

class ContinueAfterWin:

    def __init__(self, screen) -> None:
        self.screen_width, self.screen_height = 1280, 720
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def afficheContinueAfterWin(self):
        self.s = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)  # per-pixel alpha
        self.s.fill((255, 255, 255, 170))  # notice the alpha value in the color
        self.screen.blit(self.s, (0, 0))
        self.text_bouton_continue = self.font.render("Continuer", True, (0, 0, 0))
        self.text_bouton_rect_continue = self.text_bouton_continue.get_rect()
        self.text_bouton_continue_x = self.screen.get_width() / 2 - self.text_bouton_rect_continue.width / 2
        self.text_bouton_continue_y = self.screen.get_height() / 2 - self.text_bouton_rect_continue.height / 2

        self.text_bouton_exit = self.font.render("Quitter le niveau", True, (0, 0, 0))
        self.text_bouton_rect_exit = self.text_bouton_exit.get_rect()
        self.text_bouton_exit_x = self.screen.get_width() / 2 - self.text_bouton_rect_exit.width / 2
        self.text_bouton_exit_y = self.screen.get_height() / 2 - self.text_bouton_rect_exit.height / 2

        self.button_continue = self.screen.blit(self.text_bouton_continue, [self.text_bouton_continue_x, self.text_bouton_continue_y])
        self.button_exit = self.screen.blit(self.text_bouton_exit, [self.text_bouton_exit_x, self.text_bouton_exit_y])

    def update(self):
        self.afficheContinueAfterWin()