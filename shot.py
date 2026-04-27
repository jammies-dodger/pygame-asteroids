import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, SHOT_LIFETIME_SECONDS, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.time_to_live = SHOT_LIFETIME_SECONDS 
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        if(self.time_to_live < 0): self.kill()
        else:
            self.position += self.velocity * dt
            self.time_to_live -= dt
            self.loop_back()