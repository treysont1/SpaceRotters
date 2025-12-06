import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, img = "assets/fighter_jet.png"):
        super().__init__()
        self.is_alive = True
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.size = size
        
    def left(self, dt):
        self.rect.x -= 1 * dt / 2

    def right(self, dt):
        self.rect.x += 1 * dt / 2

    def die(self):
        self.explosion = pygame.image.load("assets/explosion_pixel_art.png")
        self.image = pygame.transform.scale(self.explosion, (75, 75))
        self.rect.centerx -= 10
        self.rect.centery -= 5
    
    def respawn(self, x, y):
        self.image = pygame.transform.scale(self.original_image, self.size)
        self.rect.center = (x, y)
        
    



