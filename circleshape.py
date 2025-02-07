import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, other_circle):
        return (
            self.position.distance_to(other_circle.position)
            <= self.radius + other_circle.radius
        )
        # should return True or False

    def draw(self, screen):
        # subclasses must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
