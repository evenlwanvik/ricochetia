import pygame
from settings import *
from enemy import Enemy
from ball import Ball


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bouncer")
        self.clock = pygame.time.Clock()
        self.running = True

        self.score = 0

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()

        self.spawn_enemy()

    def spawn_enemy(self):
        enemy = Enemy()
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.MOUSEBUTTONDOWN:
                    self.drop_ball(event.pos)

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.groupcollide(self.balls, self.enemies, True, False)
        if hits:
            self.score += 1

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def drop_ball(self, position):
        ball = Ball(position)
        self.all_sprites.add(ball)
        self.balls.add(ball)
