import pygame
import sys

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

    # create score
    score_value = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # create a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # add front
    game_over_font = pygame.font.Font(None, 74)
    score_font = pygame.font.Font(None, 50)

    # Render the text Game over!
    game_over_text = game_over_font.render("Game over!", True, "white")

    # Render the score text
    score_text = score_font.render(f"Score: {score_value}", True, "GREEN")

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

    game_run = True

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen black
        screen.fill("black")

        if game_run:
            # update score
            score_text = score_font.render(f"Score: {score_value}", True, "GREEN")

            updatable.update(dt)
            for d in drawable:
                d.draw(screen)

            # collision check
            for asteroid in asteroids:
                # collision check with player
                if asteroid.collides_with(player):
                    game_run = False
                # collision check with bullet
                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()
                        score_value += asteroid.get_score()

            # draw score
            screen.blit(score_text, (20, 20))

        else:
            # draw game over text
            screen.blit(game_over_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2))
            screen.blit(score_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 50))

        # update the screen
        pygame.display.flip()

        # update delta time for 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
