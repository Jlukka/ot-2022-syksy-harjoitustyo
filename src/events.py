import pygame


class Events:
    def __init__(self):
        self.enemy_death = pygame.event.custom_type()
        self.goal_reached = pygame.event.custom_type()


userEvents = Events()
