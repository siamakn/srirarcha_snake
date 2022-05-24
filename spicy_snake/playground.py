import random


class Playground:

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.food = None

    @property
    def size(self):
        """instead of a self.size attribute"""
        return self.xsize, self.ysize

    def is_obstacle(self, position):
        x, y = position
        if (
            0 < x < self.xsize and
            0 < y < self.ysize
        ):
            return False

        return True

    def add_food(self, position):
        if not self.is_obstacle(position):
            self.food = position
        else:
            self.food = None

    def add_random_food(self):
        position = (
            random.randint(1, self.xsize - 1),
            random.randint(1, self.ysize - 1)
        )
        self.add_food(position)
