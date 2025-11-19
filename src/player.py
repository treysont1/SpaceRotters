import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, img = "assets/fighter_jet.png"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        # self.x, self.y = x, y
        self.rect.center = (x, y)    
        self.left = False
        self.right = False
        
    
    def move(self):
        if self.left == True:
            self.rect.x -= 1
        if self.right == True:
            self.rect.x += 1


        
        
