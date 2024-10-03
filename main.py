import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    #start of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                exit(0)

        pygame.Surface.fill(screen, color=0)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

#ensures the main function is only called when this file
#is run directly; it won't run if it's imported as a module
if __name__ == "__main__":
    main()
