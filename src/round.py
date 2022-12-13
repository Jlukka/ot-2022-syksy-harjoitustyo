class Round:
    def __init__(self, enemy_function, count, delay):
        self.enemy_func = enemy_function
        self.count = count
        self.spawned = 0
        self.delay = delay
