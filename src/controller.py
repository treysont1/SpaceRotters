import pygame
from player import Player


class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        self.player = Player(self.width // 2, self.height //2, 25)

    def mainloop(self):
        run = True
        while run == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.left = True
            else:
                self.player.left = False
            if keys[pygame.K_RIGHT]:
                self.player.right = True
                print("hello)")
            else: 
                self.player.right = False
                # if event.key == pygame.K_RIGHT:
                #     self.player.right = True
            # elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            #     self.player.left = False
                
                # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #     self.player.left = False
                self.player.move()
               
            self.screen.fill("white")
            self.screen.blit(self.player.image, self.player.rect)
            pygame.display.flip()
                

        
            
            
        
        

