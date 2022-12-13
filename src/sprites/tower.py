import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, radius=2, damage=1, firerate=1):
        super().__init__()

        self.radius = radius
        self.damage = damage
        self.firerate = firerate
        self.last_update = None
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, time):
        if self.last_update is None:
            pass
        self.last_update = time
