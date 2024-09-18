import pygame
#imports all constants from the file
from constants import *
from player import Player

def main():
    #initialize pygame
    pygame.init()
    #set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #set up a clock for fps
    fps = pygame.time.Clock()
    dt = 0
    #create an instance of the player class
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2 
    player = Player(x,y)


    #GAME LOOP
    #makes the x button usable
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
    #1. check for player inputs
    #2. update the game world
    #3. drawing the game onto the screen
    
        #makes the display black
        screen.fill((0,0,0), rect=None, special_flags=0)
        #set fps to 60 and save delta time to dt
        dt = fps.tick(60) / 1000
        #draw the player(triangle)
        player.draw(screen)
        #rotate left and right
        player.update(dt)
        #keep showing the display with everything that was drawn
        pygame.display.flip()
        
            
    


if __name__ == "__main__":
    main()

#print("Starting asteroids!")
#print(f"Screen width: {SCREEN_WIDTH}")
#print(f"Screen height: {SCREEN_HEIGHT}")