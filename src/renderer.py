import pygame


class Renderer():
    def __init__(self, display, game):
        self._display = display
        self._game = game

    def render(self):
        self._game.all_sprites.draw(self._display)

        pygame.display.update()
