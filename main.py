import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 

from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt = 0.0

    # Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        
        screen.fill("black")

        player.draw(screen)

        dt = clock.tick(60) / 1000

        pygame.display.flip()

if __name__ == "__main__":
    main()
