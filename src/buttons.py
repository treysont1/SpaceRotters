import pygame

class Start:
    def __init__(self, x, y, img = "assets/start_button.png"):
        self.start_button = pygame.image.load(img)
        self.image = pygame.transform.scale(self.start_button, (5, 5))
        self.rect = self.start_button.get_rect()
        self.rect.center = (x, y)

class Exit:
    def __init__(self, x, y, img = "assets/exit_icon.png"):
        self.exit_button = pygame.image.load(img)
        self.rect = self.exit_button.get_rect()
        self.rect.center = (x, y)

