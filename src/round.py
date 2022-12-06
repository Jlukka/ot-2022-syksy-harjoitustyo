class Round:
    def __init__(self, enemyFunction, count, delay):
        self.enemyFunc = enemyFunction
        self.count = count
        self.spawned = 0
        self.delay = delay
        