import pygame
from game import Game
from gameloop import GameLoop
from eventqueue import EventQueue
from renderer import Renderer
from clock import Clock
from static.levels.level import grid
from config import tileSize


def main():
    height = len(grid)
    width = len(grid[0])
    display_height = height * tileSize
    display_width = width * tileSize
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("towerdefence")

    game = Game(grid, 500, 100)
    event_queue = EventQueue()
    renderer = Renderer(display, game)
    clock = Clock()
    game_loop = GameLoop(game, renderer, event_queue, clock, tileSize)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
