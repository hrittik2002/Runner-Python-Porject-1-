import pygame
from sys import exit
from random import randint , choice


class Player(pygame.sprite.Sprite):  # Inherit from Spritre class

    def __init__(self):  # Constractor
        super().__init__() # we are initializing the sprite class right inside the Player class so that we can access it
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()  # image for player
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()  # image for player
        self.player_walk = [player_walk_1 , player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()  # image for player jump
        # Now this class needed 2 attribute at the very minimum one is self.image and the other self.rect
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if(self.rect.bottom < 300):
            #jump
            self.image = self.player_jump
        else:
            #walk
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self , type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1 , fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # image for snail 1
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()  # image for snail 2
            self.frames = [snail_1 , snail_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900 , 1100) , y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def  update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# for displaying the score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))  # background text
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf , score_rect)      # setting the background text
    return current_time

def  obstacle_movement(obstacle_list):
    if obstacle_list:      # if our list is empty this statement is not going to run
        for  obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface , obstacle_rect)
            else:
                screen.blit(fly_surf , obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player , obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite , obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True
def player_animation():

    global player_surf , player_index

    if(player_rect.bottom < 300):
        #jump
        player_surf = player_jump
    else:
        #walk
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]



# here we are initializing pygame (Note it should always be the first line)
pygame.init()
screen = pygame.display.set_mode((800, 400))    # to create the display surface
# setting up the title / caption of the game
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
# font style , font size
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False

bg_Music = pygame.mixer.Sound('audio/music.wav')
bg_Music.set_volume(0.1)
bg_Music.play(loops = -1)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# background image for sky
sky_surface = pygame.image.load('graphics/MySky.png').convert()
ground_surface = pygame.image.load('graphics/Myground.png').convert()  # background image for ground

# score_surf = test_font.render('Welcome to My First Game', False, (64, 64, 64))  # background text
# score_rect = score_surf.get_rect(center=(400, 50))


# Obstacles
# Snail
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # image for snail 1
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()  # image for snail 2
snail_frames = [snail_frame_1 , snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]
# Fly
fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1 , fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()  # image for player
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()  # image for player
player_walk = [player_walk_1 , player_walk_2]
player_index = 0
player_jump = player_walk1 = pygame.image.load('graphics/Player/jump.png').convert_alpha()  # image for player jump

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))

start_time = 0
player_gravity = 0
score = 0

# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha() # image for player during end screen
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400 , 200))

game_name = test_font.render('Pixel Runner' , False , (111 , 196 , 169))
game_name_rect = game_name.get_rect(center = (400 , 80))

game_message = test_font.render('Press Space to run' , False , (111 , 196 , 169))
game_message_rect = game_message.get_rect(center = (400 , 340))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer , 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer , 200)

# GAME LOOP
while True:                            # while this condition is true the screen will not switch off

    for event in pygame.event.get():   # the method pygame.event.get() will give all the events and with the help of for loop we just loop through all of them
        if event.type == pygame.QUIT:  # if the type of the event is equal to pygame.QUIT it means we are indicating to close the window
            pygame.quit()              # it is just opposite of pygame.init().....it uninitialize pygame
            exit()                     # this exist method closes any kind of code
        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -25


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -25
            # if event.type == pygame.KEYUP:
            #     print('keyup')
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly' , 'snail' , 'snail' , 'snail'])))
                # if randint(0 , 2): # eturn 0 or 1
                #     obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900 , 1100), 300)))       
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900 , 1100), 210))) 
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]
            
    if game_active:      
        screen.blit(sky_surface , (0 , 0))        # setting the sky image 
        screen.blit(ground_surface , (0 , 300))   # setting the ground image  

        score = display_score()
        # pygame.draw.rect(screen , '#c0e8eC' , score_rect)
        # pygame.draw.rect(screen , '#c0e8eC' , score_rect , 10)
        # screen.blit(score_surf , score_rect)      # setting the background text

        # snail_rect.x -= 4
        # if(snail_rect.x < -100):
        #     snail_rect.x = 805
        # screen.blit(snail_surface , snail_rect)


        # PLAYERS JUMP LOGIC
        # player_gravity += 1
        # player_rect.y += player_gravity

        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf , player_rect)

        player.draw(screen)

        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        # OBSTACLE MOVEMENT
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        # COLLISION BETWEEN PLAYER AND OBSTACLE
        game_active = collisions_sprite()
        # game_active = collisions(player_rect , obstacle_rect_list)
        
    else:    
        screen.fill((94,129,162))
        screen.blit(player_stand , player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80 , 300)
        player_gravity = 0
        score_message = test_font.render(f'Your score: {score}' , False , (111,196,169))
        score_message_rect = score_message.get_rect(center = (400 , 300))
        screen.blit(game_name , game_name_rect)

        if score == 0:
            screen.blit(game_message , game_message_rect)
        else:
            screen.blit(score_message , score_message_rect)

    pygame.display.update()            # to update the display
    clock.tick(60)                     # this line says our game should not run faster than 60 times per second (setting up the maximum frame rate)
