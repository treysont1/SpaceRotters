import pygame
import random
from src.player import Player
from src.titles import BrainRotters, Winner, Loser
from src.background import Backgrounds
from src.buttons import Start, Replay, Exit
from src.player_projectile import Player_Projectile
from src.enemies import Enemy
from src.enemy_projectile import Enemy_Projectile



class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(size= (800, 700))
        self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption("Space Rotters")
        self.background = Backgrounds((self.width, self.height), "assets/space_bg.jpg")
        self.title = BrainRotters(self.width * 0.5, self.height * 0.4)
        self.loser = Loser(self.width * 0.5, self.height * 0.4)
        self.winner = Winner(self.width * 0.5, self.height * 0.4)
        self.start = Start(self.width // 2 , self.height // 1.4)
        self.restart = Replay(self.width // 2 , self.height // 1.4)
        self.exit = Exit(self.width - 15, 15)
        self.font = pygame.font.Font("assets/retrostyle.ttf", 30)

        self.player = Player(self.width // 2, self.height - 150, (50, 50))
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.player_shots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_shots = pygame.sprite.Group()
        self.groups = (self.player_group, self.player_shots, self.enemies, self.enemy_shots)
        self.blaster_sound = pygame.mixer.Sound("assets/blaster_sound.wav")
        self.last_shot = 0
        self.shot_cooldown = 500

    def mainloop(self):
        run = "Start"

        while True:
            #title screen
            while run == "Start":
                self.screen.fill((0,0,0))
                self.screen.blit(self.background.image, (0,0))
                self.screen.blit(self.title.logo, self.title.rect)
                self.screen.blit(self.start.image, self.start.rect)
                self.screen.blit(self.exit.exit_button, self.exit.rect)
                pygame.display.flip()
                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN and self.start.rect.collidepoint(event.pos):
                        run = "Game"

            
            move_timer = 750
            move_event = pygame.USEREVENT + 1
            pygame.time.set_timer(move_event, move_timer)

            enemy_speed = 20
            # enemy_shot_timer = 750
            enemy_shot_timer = random.randint(1000, 1250)
            enemy_shot_event = pygame.USEREVENT + 2
            pygame.time.set_timer(enemy_shot_event, enemy_shot_timer)

            level = 1
            score = 0
            lives = 3
            player_alive = True

            respawn_event = pygame.USEREVENT + 3

            #game play        
            while run == "Game":
                #dt to cap framerate to make it similar across all platforms
                dt = self.clock.tick(60)
                self.screen.blit(self.background.image, (0,0))
                self.enemy_coords1 = [-280, -140, 0, 140, 280]
                text_surface = self.font.render(f"Score: {score}", True, "white")
                self.screen.blit(text_surface, (10, 0))
                instructions = self.font.render("right & left arrows to move | spacebar to shoot", True, "white")
                self.screen.blit(instructions, (20, self.height - 30))
                keys = pygame.key.get_pressed()
                current_time = pygame.time.get_ticks()

                if lives > 0 and not self.player_group:
                    self.player = Player(self.width // 2, self.height - 150, (50, 50))
                    self.player_group.add(self.player)


                if level == 1:
                    for coord in self.enemy_coords1:
                        enemy = Enemy(self.width // 2 + coord, 60)
                        self.enemies.add(enemy)
                    level += 1

                if level == 2 and not self.enemies:
                    for coord in self.enemy_coords1:
                        enemy1 = Enemy(self.width // 2 + coord, 60)
                        enemy2 = Enemy(self.width // 2 + coord, 125, "assets/skibiditoilet.png")
                        self.enemies.add(enemy1, enemy2)
                    level += 1
                    
                if level == 3 and not self.enemies:
                    for coord in self.enemy_coords1:
                        enemy1 = Enemy(self.width // 2 + coord, 60)
                        enemy2 = Enemy(self.width // 2 + coord, 125, "assets/skibiditoilet.png")
                        enemy3 = Enemy(self.width // 2 + coord, 190)
                        self.enemies.add(enemy1, enemy2, enemy3)
                    level += 1
                
                if level == 4 and not self.enemies:
                    run = "Winner"

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                        run = False
                    
                    if event.type == respawn_event:
                        player_alive = True
                        print("respawn starting")

                    if event.type == move_event and player_alive:
                        for enemy in self.enemies:
                            enemy.move(enemy_speed)

                    if event.type == enemy_shot_event and player_alive:
                        shooter = random.choice(list(self.enemies))
                        enemy_shot_position = shooter.rect.midbottom
                        enemy_shot = Enemy_Projectile(*enemy_shot_position)
                        self.enemy_shots.add(enemy_shot)
                        if level == 1:
                            enemy_shot_timer = random.randint(1000, 1250)
                        elif level == 2:
                            enemy_shot_timer = random.randint(750, 1000)
                        elif level == 3:
                            enemy_shot_timer = random.randint(500, 1000)
                        pygame.time.set_timer(enemy_shot_event, enemy_shot_timer)
                        
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                        shooter = random.choice(list(self.enemies))
                        enemy_shot_position = shooter.rect.midbottom
                        enemy_shot = Enemy_Projectile(*enemy_shot_position)
                        self.enemy_shots.add(enemy_shot)

                    #developer tool
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        # run = "Game Over"
                        lives += 1
                        print(lives)


                    #  Hitbox Testing
                    #  if event.type == pygame.MOUSEBUTTONDOWN:
                    #     enemy = Enemy(*(event.pos))
                    #     self.enemies.add(enemy)
                    #     print(event.pos)
                    # if event.type == pygame.MOUSEBUTTONDOWN and self.player.rect.collidepoint(event.pos):
                    #     print("Hit")

                edge_hit = False
                right_hit = False
                left_hit = False
                reach_player = False

                for enemy in self.enemies:
                    if enemy.rect.right >= self.width:
                        edge_hit = True
                        right_hit = True
                        break
                    if enemy.rect.left <= 0:
                        edge_hit = True
                        left_hit = True
                        break
                    if enemy.rect.bottom >= self.player.rect.top:
                        reach_player = True
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

                    pygame.time.set_timer(move_event, move_timer)
            
                
                # Movement Function  
                if player_alive:
                    if keys[pygame.K_LEFT] and self.player.rect.left > 0:
                        self.player.left(dt)

                    if keys[pygame.K_RIGHT] and self.player.rect.right < self.width:
                        self.player.right(dt)
                    
                    # New Shoot Function

                    if keys[pygame.K_SPACE]:
                        if current_time - self.last_shot > self.shot_cooldown:
                            shot_position = self.player.rect.midtop
                            shot = Player_Projectile(*shot_position)
                            self.player_shots.add(shot)
                            self.blaster_sound.play()
                            self.last_shot = current_time

                self.enemies.draw(self.screen)

                self.enemy_shots.draw(self.screen)
                self.enemy_shots.update(self.screen, dt)

                self.player_shots.draw(self.screen)
                self.player_shots.update(self.screen, dt)

                if pygame.sprite.groupcollide(self.player_shots, self.enemies, True, True):
                    score += 25

                if pygame.sprite.groupcollide(self.player_group, self.enemy_shots, True, True):
                    lives -= 1
                    self.enemy_shots.empty()
                    self.player_shots.empty()
                    player_alive = False
                    pygame.time.set_timer(respawn_event, 1500, 1)
                    print("hit")

                if (not self.player_group and lives == 0) or reach_player:
                    for group in self.groups:
                        group.empty()
                    
                    run = "Loser"

                # self.screen.blit(self.player.model, self.player.rect)
                self.player_group.draw(self.screen)
                self.screen.blit(self.exit.exit_button, self.exit.rect)
                
        
                pygame.display.flip()

            while run == "Winner":
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.background.image, (0,0))
                self.screen.blit(self.winner.logo, self.winner.rect)
                self.screen.blit(self.restart.image, self.restart.rect)
                self.screen.blit(self.exit.exit_button, self.exit.rect)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and self.restart.rect.collidepoint(event.pos):
                        run = "Game"

            #Lose screen
            while run == "Loser":
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.background.image, (0,0))
                self.screen.blit(self.loser.logo, self.loser.rect)
                self.screen.blit(self.restart.image, self.restart.rect)
                self.screen.blit(self.exit.exit_button, self.exit.rect)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.rect.collidepoint(event.pos):
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and self.restart.rect.collidepoint(event.pos):
                        run = "Game"
                        
            if run == False:
                break