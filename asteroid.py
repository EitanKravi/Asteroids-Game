import random
import pygame

# take snapshot of the game state
from logger import log_event

import circleshape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # create velocity for the split asteroid
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        # create the radius for the new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create 2 new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # set the new velocity for the new 2 asteroids
        asteroid1.velocity +=  velocity1 * 1.2
        asteroid2.velocity += velocity2 * 1.2
