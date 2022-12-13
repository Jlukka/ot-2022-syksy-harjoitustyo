import os
from math import floor
import pygame
from events import userEvents

dirname = os.path.dirname(__file__)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, maxhealth=1, speed=1, path=[], tile_size=32):
        super().__init__()

        self.maxhealth = maxhealth
        self.health = maxhealth
        self.speed = speed
        self.distance = 0
        self.path = path
        self.last_update = None
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "static", "enemy.png")
        )
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.tile_size = tile_size
        self.rect = self.image.get_rect()
        self.rect.x = x*self.tile_size
        self.rect.y = y*self.tile_size

    def update(self, time):
        if not self.last_update is None:
            time_delta = time - self.last_update
            self.distance += (time_delta * self.speed)
            if self.distance >= len(self.path):
                goal_event = pygame.event.Event(userEvents.goal_reached)
                pygame.event.post(goal_event)
                self.kill()
        self.last_update = time
        self.update_pos()

    def update_pos(self):
        prev_tile = self.path[min(floor(self.distance), len(self.path)-1)]
        next_tile = self.path[min(floor(self.distance)+1, len(self.path)-1)]
        prev_pos = (prev_tile[0], prev_tile[1])
        next_pos = (next_tile[0], next_tile[1])
        new_pos = pygame.math.Vector2(prev_pos).lerp(next_pos, self.distance % 1)
        new_x = new_pos[0]*self.tile_size
        new_y = new_pos[1]*self.tile_size
        self.rect.x = new_x
        self.rect.y = new_y

    def take_damage(self, damage):
        if damage > 0:
            self.health = self.health - damage
        if self.health <= 0:
            death_event = pygame.event.Event(userEvents.enemy_death)
            pygame.event.post(death_event)
