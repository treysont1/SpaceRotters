import pygame

class Enemy_Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 0, img = "assets/enemy_projectile.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, (9, 25))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
    
    # def update(self, screen, dt):
    #     self.rect.centery -= 1 * dt / 2
    #     if not screen.get_rect().contains(self.rect):
    #         self.kill()

