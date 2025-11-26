import pygame
from src.player import Player
from src.exit import Exit
from src.player_projectile import Player_Projectile
from src.enemies import Enemy


class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        self.player = Player(self.width // 2, self.height - 150, (50, 50))
        self.exit = Exit(self.width - 15, 15)
        self.player_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.blaster_sound = pygame.mixer.Sound("assets/blaster_sound.wav")
        self.setup = 0

    def mainloop(self):
        run = True
        move_down = 1000
        move_down_event = pygame.USEREVENT + 1
        pygame.time.set_timer(move_down_event, move_down)

        while run == True:
            #dt to cap framerate to make it similar across all platforms
            dt = self.clock.tick(60)
            self.screen.fill("black")
            self.enemy_coords1 = [-280, -140, 0, 140, 280]

            if self.setup == 0:
                for coord in self.enemy_coords1:
                    enemy = Enemy(self.width // 2 + coord, 30)
                    self.enemies.add(enemy)
                self.setup += 1
            
            if not self.enemies:
                self.setup = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    position = self.player.hitbox.midtop
                    shot = Player_Projectile(*position)
                    self.player_bullets.add(shot)
                    self.blaster_sound.play()
                    # print("shoot")
                if event.type == move_down_event:
                    for enemy in self.enemies:
                        enemy.move_down()
                
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     enemy = Enemy(*(event.pos))
                #     self.enemies.add(enemy)
                #     print(event.pos)
                # if event.type == pygame.MOUSEBUTTONDOWN and self.player.hitbox.collidepoint(event.pos):
                #     print("Hit")
            # if self.setup == 0:
            #     for coord in self.enemy_coords1:
            #         enemy = Enemy(self.width // 2 + coord, 30)
            #         self.enemies.add(enemy)
            #     self.setup += 1
            
            # if not self.enemies:
            #     self.setup = 0

            self.enemies.draw(self.screen)

            self.player_bullets.draw(self.screen)

            self.player_bullets.update(self.screen, dt)

            pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)
            # Movement Function  
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.hitbox.x > 0:
                self.player.left(dt)

            if keys[pygame.K_RIGHT] and self.player.hitbox.right < self.width:
                self.player.right(dt)
            

            self.screen.blit(self.player.model, self.player.hitbox)
            self.screen.blit(self.exit.exit_button, self.exit.rect)

            pygame.display.flip()
                

        
            
            
        
        

