import pygame

class Player_Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 0, img = "assets/player_projectile.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, (9, 25))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        # self.projectile = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 40, 40)
    
    def update(self, dt):
        self.rect.centery -= 3 * dt

    # def shoot(self):

