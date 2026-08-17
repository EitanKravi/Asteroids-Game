import pygame

# take snapshot of the game state
from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    # create 3 empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add Player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)
    # add Asteroid class to the asteroids, updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    # add AsteroidField class to the updatable group
    AsteroidField.containers = updatable

    # create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

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
