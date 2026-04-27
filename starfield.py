import random
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, STARFIELD_COUNT


class Starfield(pygame.sprite.Sprite):
    def __init__(self):
        self.stars = []
        self.generate_field()

    def generate_field(self):
        for i in range(0,STARFIELD_COUNT):
            self.stars.append(pygame.Vector2(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT)))

    def draw(self, screen):
        for star in self.stars:
            pygame.draw.circle(screen, "grey", star, 1, 1)
