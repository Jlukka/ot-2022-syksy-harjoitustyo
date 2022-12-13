import os
import pygame

dirname = os.path.dirname(__file__)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, tile_size=32):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "static", "tile.png")
        )
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
