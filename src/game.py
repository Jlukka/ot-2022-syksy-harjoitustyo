import pygame
from config import tileSize

from sprites.tile import Tile
from sprites.road import Road
from sprites.goal import Goal


class Game:
    def __init__(self, grid, startcash, startlives):
        self._grid = grid
        self.money = startcash
        self.lives = startlives
        self.path = self.__find_path()
        self.tiles = pygame.sprite.Group()
        self.roads = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.__initialize_grid_sprites()

    def __initialize_grid_sprites(self):
        for y in range(0, len(self._grid)):
            for x in range(0, len(self._grid[0])):
                real_x = x*tileSize
                real_y = y*tileSize
                element = self._grid[y][x]
                if element == 0:
                    self.tiles.add(Tile(real_x, real_y, tileSize))
                elif element in [1, 2]:
                    self.roads.add(Road(real_x, real_y, tileSize))
                elif element == 3:
                    self.roads.add(Goal(real_x, real_y, tileSize))
        self.all_sprites.add(
            self.tiles,
            self.roads
        )

    def __find_path(self):
        start = self.__find_start()

        visited = []

        def search(cell):
            visited.append(cell)
            adjs = [(cell[0]+1, cell[1]),
                    (cell[0]-1, cell[1]),
                    (cell[0], cell[1]-1),
                    (cell[0], cell[1]+1)]
            for adj in adjs:
                if self._grid[adj[1]][adj[0]] != 0 and not adj in visited:
                    if self._grid[adj[1]][adj[0]] == 3:
                        return [adj]
                    if self._grid[adj[1]][adj[0]] == 2:
                        return [adj]+search(adj)

        return search(start)

    def __find_start(self):
        for y in range(0, len(self._grid)):
            for x in range(0, len(self._grid[0])):
                if self._grid[y][x] == 1:
                    return (x, y)
        return (-1, -1)

    def update(self, time):
        for i in self.all_sprites:
            i.update(time)
