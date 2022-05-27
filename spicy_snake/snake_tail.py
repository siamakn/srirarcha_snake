"""
Here we manage the snake
"""
from spicy_snake.moves import move


class Snake:
    """A snake with a tail that grows"""

    def __init__(self, xstart, ystart):
        self.head = xstart, ystart
        self.tail = [self.head]  # ???
        self.growing = 0        # ???
        self.direction = 'right'

    def forward(self):
        """Moves the snake one step ahead"""
        self.head = move(self.head, self.direction)
        self.tail.append(self.head)  # new position
        if self.growing == 0:
            self.tail.pop(0)
        else:
            # the snake is growing
            self.growing -= 1

    def grow(self):
        """Memorizes that the snake should grow when it moves next time"""
        self.growing += 1

    def set_direction(self, direction):
        """Moves the head to a new direction"""
        self.direction = direction

    def eat(self, playground):
        """Eats food at the position of the head, if any"""
        if playground.food == self.head:
            self.grow()
            playground.food = None

    def check_collision(self, playground):
        """Returns True if the head hits an obstacle or the tail"""
        return (
            playground.is_obstacle(self.head) or  # wall collisions
            self.head in self.tail[:-1]  # tail collisions
        )
