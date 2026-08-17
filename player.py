import pygame

import circleshape
from constants import *
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0
        self.cooldown: float = 0

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

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shot(self) -> None:
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt: float) -> None:
        self.cooldown -= dt

        keys = pygame.key.get_pressed()

        # rotate player
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move player
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)

        # shot a bullet
        if keys[pygame.K_SPACE]:
            if not self.cooldown > 0:
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shot()
