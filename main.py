import pygame
#imports all constants from the file
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import *

 #create groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

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
    player = Player(x,y, shots_group = shots)
    #create asteroids
    fields = AsteroidField()
    updatable.add(fields)

    #fill the groups
    updatable.add(player)
    drawable.add(player)
    
    
   
    #GAME LOOP
    #makes the x button usable
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
    #1. check for player inputs
    #2. update the game world
    #set fps to 60 and save delta time to dt
        dt = fps.tick(60) / 1000
    #3. drawing the game onto the screen
    
        #makes the display black
        screen.fill((0,0,0), rect=None, special_flags=0)
        
        #draw the player(triangle)
        for sprite in drawable:
            sprite.draw(screen)
        #rotate left and right
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over")
                running = False
                break
        if not running:
            break

        for obj in drawable:
            obj.draw(screen)
        #keep showing the display with everything that was drawn
        pygame.display.flip()
        
            
    


if __name__ == "__main__":
    main()

#print("Starting asteroids!")
#print(f"Screen width: {SCREEN_WIDTH}")
#print(f"Screen height: {SCREEN_HEIGHT}")