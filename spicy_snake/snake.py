import curses
import time

from spicy_snake.playground import Playground
from spicy_snake.snake_tail import Snake
from spicy_snake.screen_helpers import prepare_screen

# ASCII codes of characters on the keyboard
# KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}
KEY_COMMANDS = {68: 'left', 67: 'right', 65: 'down', 66: 'up'}

SNAKE_SYMBOL = 'O'
HEAD_SYMBOL = 'G'
WALL_SYMBOL = '#'
FOOD_SYMBOL = '*'


def draw(snake, pg, win, screen):
    # separate functions draw_player and draw_playground
    screen.clear()

    # draw the snake
    for x, y in snake.tail:
        screen.addch(y, x, SNAKE_SYMBOL, curses.color_pair(1))
    x, y = snake.head
    screen.addch(y, x, HEAD_SYMBOL, curses.color_pair(1))

    # draw the playground:
    for pgx in range(pg.xsize + 1):
        for pgy in range(pg.ysize + 1):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, WALL_SYMBOL, curses.color_pair(2))

    if pg.food:
        fx, fy = pg.food
        screen.addch(fy, fx, FOOD_SYMBOL, curses.color_pair(3))

    win.refresh()
    screen.refresh()


win, screen = prepare_screen()


def move_player(player_position, direction):
    dx, dy = direction
    x, y = player_position
    x += dx
    y += dy
    return x, y


def game_loop(screen):
    pg = Playground(30, 14)
    pg.add_random_food()
    snake = Snake(5, 5)
    draw(snake, pg, win, screen)

    delay = 20000

    while not snake.check_collision(pg):
        # move the player
        char = win.getch()  # returns the code of a pressed key
        direction = KEY_COMMANDS.get(char)  # direction is a tuple or None
        if direction:
            snake.set_direction(direction)

        delay -= 1
        if delay == 0:
            delay = 20000
            snake.forward()
            snake.eat(pg)
            if not pg.food:
                pg.add_random_food()
            draw(snake, pg, win, screen)

    time.sleep(2)


if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
