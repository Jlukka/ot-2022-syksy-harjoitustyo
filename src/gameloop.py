import pygame
from sprites.enemy import Enemy


class GameLoop():
    def __init__(self, game, renderer, event_queue, clock, cell_size):
        self._game = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        a = Enemy(0, 1, 10, 0.005, self._game.path, 32)
        self._game.all_sprites.add(a)

        while True:
            if self._handle_events() is False:
                break

            self._game.update(self._clock.get_ticks())

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
