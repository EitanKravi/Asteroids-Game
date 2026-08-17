import pygame

# take snapshot of the game state
from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()

    # create a Clock object
    clock = pygame.time.Clock()

    # create delta time
    dt: float= 0.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # create a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create 2 empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add Player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)

    # create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen black
        screen.fill("black")

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        # update the screen
        pygame.display.flip()

        # update delta time for 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pygame.quit()
