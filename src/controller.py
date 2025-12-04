import pygame
from src.player import Player
from src.background import Backgrounds
from src.buttons import Start, Exit
from src.player_projectile import Player_Projectile
from src.enemies import Enemy



class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(size= (800, 800))
        self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption("Space Rotters")
        self.background = Backgrounds((self.width, self.height), "assets/space_bg.jpg")
        self.start = Start(self.width //2, self.height // 2)

        self.player = Player(self.width // 2, self.height - 150, (50, 50))
        self.exit = Exit(self.width - 15, 15)
        self.player_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.blaster_sound = pygame.mixer.Sound("assets/blaster_sound.wav")
        self.setup = 0
        self.last_shot = 0
        self.shot_cooldown = 500

    def mainloop(self):
        run = "Start"
        while run == "Start":
            self.screen.fill((0,0,0))
            self.screen.blit(self.background.image, (0,0))
            self.screen.blit(self.start.start_button, self.start.rect)
            self.screen.blit(self.exit.exit_button, self.exit.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.start.rect.collidepoint(event.pos):
                    run = "Game"

        move_down = 1000
        move_down_event_id = pygame.USEREVENT + 1
        # move_down_event = pygame.event.Event(move_down_event_id)
        # pygame.time.set_timer(move_down_event, move_down)
        move_timer = 500
        move_event = pygame.USEREVENT + 2
        pygame.time.set_timer(move_event, move_timer)
        enemy_speed = 10

                
        while run == "Game":
            #dt to cap framerate to make it similar across all platforms
            dt = self.clock.tick(60)
            # self.screen.fill("black")
            self.screen.blit(self.background.image, (0,0))
            self.enemy_coords1 = [-280, -140, 0, 140, 280]
            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            

            if self.setup == 0:
                for coord in self.enemy_coords1:
                    enemy = Enemy(self.width // 2 + coord, 30)
                    self.enemies.add(enemy)
                self.setup += 1
            
            if not self.enemies:
                self.setup = 0

            # for enemy in self.enemies:
            #     if enemy.rect.right >= self.width or enemy.rect.left <= 0:
            #         for enemy in self.enemies:
            #             enemy.move_down(self.screen)
            #         enemy_speed = - (enemy_speed + 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                    run = False

                if event.type == move_event:
                    for enemy in self.enemies:
                        enemy.move(enemy_speed)

              
                
                #  Hitbox Testing
                #  if event.type == pygame.MOUSEBUTTONDOWN:
                #     enemy = Enemy(*(event.pos))
                #     self.enemies.add(enemy)
                #     print(event.pos)
                # if event.type == pygame.MOUSEBUTTONDOWN and self.player.hitbox.collidepoint(event.pos):
                #     print("Hit")
            edge_hit = False
            # direction_changed = False 

            for enemy in self.enemies:
                if enemy.rect.right >= self.width or enemy.rect.left <= 0:
                    edge_hit = True
                    for enemy in self.enemies:
                        if enemy.rect.right >= self.width:
                            enemy.rect.right -= 10
                        if enemy.rect.left <= 0:
                            enemy.rect.left += 10
                    break

            if edge_hit:    
                for enemy in self.enemies:   
                    enemy.move_down(self.screen)
                enemy_speed = - (enemy_speed)
                # direction_changed = True
            
            # if not edge_hit:
            #     direction_changed = False

            self.enemies.draw(self.screen)

            self.player_bullets.draw(self.screen)

            self.player_bullets.update(self.screen, dt)

            pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)
            
            # Movement Function  
            
            if keys[pygame.K_LEFT] and self.player.hitbox.x > 0:
                self.player.left(dt)

            if keys[pygame.K_RIGHT] and self.player.hitbox.right < self.width:
                self.player.right(dt)
            
            # New Shoot Function

            if keys[pygame.K_SPACE]:
                if current_time - self.last_shot > self.shot_cooldown:
                    position = self.player.hitbox.midtop
                    shot = Player_Projectile(*position)
                    self.player_bullets.add(shot)
                    self.blaster_sound.play()
                    self.last_shot = current_time


            self.screen.blit(self.player.model, self.player.hitbox)
            self.screen.blit(self.exit.exit_button, self.exit.rect)

            pygame.display.flip()
                            

                    
                        
                        
                    
                    

