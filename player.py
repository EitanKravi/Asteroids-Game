import pygame

import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH

class Player(circleshape.CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0

    # coped from bootdev (create the point of the triangle shape)
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    # ended copy

    def draw(self, screen: pygame.Surface) -> None:
        # draw the triangle from the points
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


