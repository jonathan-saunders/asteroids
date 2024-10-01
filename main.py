import pygame
from constants import *

def main():
    n = 5
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while n > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=0)
        pygame.display.flip()
        dt = clock.tick(60)/1000

#ensures the main function is only called when this file
#is run directly; it won't run if it's imported as a module
if __name__ == "__main__":
    main()
