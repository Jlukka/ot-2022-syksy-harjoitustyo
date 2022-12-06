import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, maxhealth=1, speed=1):
        super().__init__()

        self.maxhealth = maxhealth
        self.health = maxhealth
        self.speed = speed
        self.last_update = None
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, time):
        if self.last_update is None:
            pass
        self.last_update = time

    def take_damage(self, damage):
        if damage > 0:
            self.health = self.health - damage
        if self.health <= 0:
            pass
            #fire on death event once implemented