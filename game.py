import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))  # background text
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf , score_rect)      # setting the background text


# here we are initializing pygame (Note it should always be the first line)
pygame.init()
screen = pygame.display.set_mode((800, 400))    # to create the display surface
# setting up the title / caption of the game
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
# font style , font size
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = True

# background image for sky
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()  # background image for ground

# score_surf = test_font.render('Welcome to My First Game', False, (64, 64, 64))  # background text
# score_rect = score_surf.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # image for snail
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()  # image for player
player_rect = player_surf.get_rect(midbottom=(80, 300))

start_time = 0
player_gravity = 0

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
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:      
        screen.blit(sky_surface , (0 , 0))        # setting the sky image 
        screen.blit(ground_surface , (0 , 300))   # setting the ground image  

        display_score()
        # pygame.draw.rect(screen , '#c0e8eC' , score_rect)
        # pygame.draw.rect(screen , '#c0e8eC' , score_rect , 10)
        # screen.blit(score_surf , score_rect)      # setting the background text

        snail_rect.x -= 4
        if(snail_rect.x < -100):
            snail_rect.x = 805
        screen.blit(snail_surface , snail_rect)


        # PLAYERS JUMP LOGIC
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf , player_rect)
        
        # COLLISION BETWEEN PLAYER AND SNAIL LOGIC
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:    
        screen.fill('Yellow')

    pygame.display.update()            # to update the display
    clock.tick(60)                     # this line says our game should not run faster than 60 times per second (setting up the maximum frame rate)
