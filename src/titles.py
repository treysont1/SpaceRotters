import pygame

class BrainRotters:
    def __init__(self, x, y, img = "assets/logo.png"):
        pygame.sprite.Sprite.__init__(self)
        self.logo = pygame.image.load(img)
        self.logo = pygame.transform.smoothscale(self.logo, (512*1.7, 104*1.7))
        self.rect = self.logo.get_rect()
        # print(x, y)
        self.rect.center = (x, y)

class Loser:
    def __init__(self, x, y, img = "assets/You_Lose.png"):
        pygame.sprite.Sprite.__init__(self)
        self.logo = pygame.image.load(img)
        self.logo = pygame.transform.smoothscale(self.logo, (512*1.7, 104*1.7))
        self.rect = self.logo.get_rect()
        # print(x, y)
        self.rect.center = (x, y)

class Winner:
    def __init__(self, x, y, img = "assets/You_Win.png"):
        pygame.sprite.Sprite.__init__(self)
        self.logo = pygame.image.load(img)
        self.logo = pygame.transform.smoothscale(self.logo, (512*1.7, 104*1.7))
        self.rect = self.logo.get_rect()
        # print(x, y)
        self.rect.center = (x, y)
