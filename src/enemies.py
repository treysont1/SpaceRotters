import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/sahur.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move_down(self, screen):
        self.rect.centery += 50
        if not screen.get_rect().contains(self.rect):
            self.kill()
    
    def move(self, enemy_speed):
        self.rect.centerx += enemy_speed


        # if self.rect.right < width:
        #     self.rect.centerx += 10
        # elif self.rect.left >= 0:
        #     self.rect.centerx -= 10