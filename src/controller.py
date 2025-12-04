import pygame
import random
from src.player import Player
from src.background import Backgrounds
from src.buttons import Start, Exit
from src.player_projectile import Player_Projectile
from src.enemies import Enemy
from src.enemy_projectile import Enemy_Projectile



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
        self.enemy_shots = pygame.sprite.Group()
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

        
        move_timer = 750
        move_event = pygame.USEREVENT + 2
        pygame.time.set_timer(move_event, move_timer)

        enemy_speed = 20
                
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

           

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                    run = False

                if event.type == move_event:
                    for enemy in self.enemies:
                        enemy.move(enemy_speed)
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                    shooter = random.choice(self.enemies)
                    enemy_shot_position = shooter.midbottom
                    enemy_shot = Enemy_Projectile(*enemy_shot_position)
                    self.enemy_shots.add(enemy_shot)


              
                
                #  Hitbox Testing
                #  if event.type == pygame.MOUSEBUTTONDOWN:
                #     enemy = Enemy(*(event.pos))
                #     self.enemies.add(enemy)
                #     print(event.pos)
                # if event.type == pygame.MOUSEBUTTONDOWN and self.player.hitbox.collidepoint(event.pos):
                #     print("Hit")
            edge_hit = False
            right_hit = False
            left_hit = False
            for enemy in self.enemies:
                if enemy.rect.right >= self.width:
                    edge_hit = True
                    right_hit = True
                if enemy.rect.left <= 0:
                    edge_hit = True
                    left_hit = True
                    break

            if edge_hit:   
                if right_hit: 
                    for enemy in self.enemies:
                        enemy.rect.right -= abs(enemy_speed)
                if left_hit:
                    for enemy in self.enemies:
                        enemy.rect.left += abs(enemy_speed)
                for enemy in self.enemies:   
                    enemy.move_down(self.screen)

                enemy_speed = - (enemy_speed)
                if move_timer > 350:
                    move_timer -= 50
                print(move_timer)
                pygame.time.set_timer(move_event, move_timer)
        
            

            
            # Movement Function  
            
            if keys[pygame.K_LEFT] and self.player.hitbox.x > 0:
                self.player.left(dt)

            if keys[pygame.K_RIGHT] and self.player.hitbox.right < self.width:
                self.player.right(dt)
            
            # New Shoot Function

            if keys[pygame.K_SPACE]:
                if current_time - self.last_shot > self.shot_cooldown:
                    shot_position = self.player.hitbox.midtop
                    shot = Player_Projectile(*shot_position)
                    self.player_bullets.add(shot)
                    self.blaster_sound.play()
                    self.last_shot = current_time

            self.enemies.draw(self.screen)
            self.enemy_shots.draw(self.screen)
            self.enemy_shots.update(self.screen, dt)
            self.player_bullets.draw(self.screen)
            self.player_bullets.update(self.screen, dt)

            pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)

            self.screen.blit(self.player.model, self.player.hitbox)
            self.screen.blit(self.exit.exit_button, self.exit.rect)

            pygame.display.flip()
                            

                    
                        
                        
                    
                    

