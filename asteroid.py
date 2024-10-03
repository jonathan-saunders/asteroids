from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
            super().__init__(x, y, radius)
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
         self.kill()
         rand_angle = random.uniform(20, 50)
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         vector1 = pygame.math.Vector2.rotate(self.velocity, rand_angle)
         vector2 = pygame.math.Vector2.rotate(self.velocity, -rand_angle)
         self.radius -= ASTEROID_MIN_RADIUS
         small_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius, vector1*1.2)
         small_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius, vector2)

