import pygame
from sys import exit

pygame.init()                                    # here we are initializing pygame (Note it should always be the first line)
screen = pygame.display.set_mode((800 , 400))    # to create the display surface
pygame.display.set_caption("Runner")             # setting up the title / caption of the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)           # font style , font size


sky_surface = pygame.image.load('graphics/Sky.png').convert()        # background image for sky 
ground_surface = pygame.image.load('graphics/ground.png').convert()  # background image for ground
text_surface = test_font.render('Welcome to My First Game' , False , 'Green') # background text

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # image for snail
snail_rect = snail_surface.get_rect(midbottom = (800 , 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() # image for player
player_rect = player_surf.get_rect(midbottom = (80 , 300))


while True:                            # while this condition is true the screen will not switch off           

    for event in pygame.event.get():   # the method pygame.event.get() will give all the events and with the help of for loop we just loop through all of them  
        if event.type == pygame.QUIT:  # if the type of the event is equal to pygame.QUIT it means we are indicating to close the window
            pygame.quit()              # it is just opposite of pygame.init().....it uninitialize pygame
            exit()                     # this exist method closes any kind of code

    screen.blit(sky_surface , (0 , 0))        # setting the sky image 
    screen.blit(ground_surface , (0 , 300))   # setting the ground image  
    screen.blit(text_surface , (210 , 50))    # setting the background text

    snail_rect.x -= 4
    if(snail_rect.x < -100):
        snail_rect.x = 805
    screen.blit(snail_surface , snail_rect)

    screen.blit(player_surf , player_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    pygame.display.update()            # to update the display
    clock.tick(60)                     # this line says our game should not run faster than 60 times per second (setting up the maximum frame rate)
