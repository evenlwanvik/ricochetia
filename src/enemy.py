import pygame
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10)

    def update(self):
        pass  # Add enemy movement logic here
