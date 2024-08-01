import pygame
from settings import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.math.Vector2(0, 5)  # Initial downward velocity

    def update(self):
        self.rect.y += self.velocity.y
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
