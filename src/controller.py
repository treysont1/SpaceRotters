import pygame
from src.player import Player
from src.exit import Exit
from src.player_projectile import Player_Projectile


class Controller:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        self.player = Player(self.width // 2, self.height //2, (50, 50))
        self.exit = Exit(self.width - 15, 15)
        self.player_bullets = pygame.sprite.Group()

    def mainloop(self):
        run = True
        while run == True:
            dt = self.clock.tick(60)
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    position = self.player.hitbox.midtop
                    shot = Player_Projectile(position[0], position[1])
                    self.player_bullets.add(shot)
                    print("shoot")
                if event.type == pygame.MOUSEBUTTONDOWN and self.player.hitbox.collidepoint(event.pos):
                    print("Hit")
                
            
            self.player_bullets.draw(self.screen)

            self.player_bullets.update(dt)

            # Movement Function  
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.hitbox.x > 0:
                self.player.left()

            if keys[pygame.K_RIGHT] and self.player.hitbox.right < self.width:
                self.player.right()
            

            self.screen.blit(self.player.model, self.player.hitbox)
            self.screen.blit(self.exit.exit_button, self.exit.rect)

            pygame.display.flip()
                

        
            
            
        
        

