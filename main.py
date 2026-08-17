import pygame
import sys

# take snapshot of the game state
from logger import log_state
from logger import log_event


from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main() -> None:
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
    shots = pygame.sprite.Group()

    # add Player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)
    # add Asteroid class to the asteroids, updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    # add AsteroidField class to the updatable group
    AsteroidField.containers = updatable
    # add Shot class to the shots, updatable and drawable groups
    Shot.containers = (shots, updatable, drawable)

    # create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField()

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

        # collision check
        for asteroid in asteroids:
            # collision check with player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # collision check with bullet
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # update the screen
        pygame.display.flip()

        # update delta time for 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pygame.quit()
