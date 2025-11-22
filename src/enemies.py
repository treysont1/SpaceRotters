import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/sahur.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)