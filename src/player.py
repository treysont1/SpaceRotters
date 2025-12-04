import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, img = "assets/fighter_jet.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def left(self, dt):
        self.rect.x -= 1 * dt / 2

    def right(self, dt):
        self.rect.x += 1 * dt / 2
    



