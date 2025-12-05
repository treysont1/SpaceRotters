import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/sahur.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.smoothscale(self.original_image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move_down(self):
        self.rect.centery += 50
    
    def move_horizontally(self, enemy_speed):
        self.rect.centerx += enemy_speed