# import os
from pygame import display, event, QUIT, quit, draw
from snake.snake import SnakeBlock
# os.environ["SDL_VIDEODRIVER"] = "dummy" for Linux
# os.environ["SDL_VIDEODRIVER"]="x11" # for WSL

SIZE_BLOCK = 20
LIGHT_MALLOW = (223, 223, 255)
GHOSTLY_WHITE = (245, 245, 255)
FRAME_COLOR = (223, 223, 223)
# HEADER_COLOR = (171, 171, 212)
HEADER_COLOR = (190, 190, 212)
SNAKE_COLOR = (5, 115, 82)
COUNT_BLOCKS = 20
MARGIN = 1
HEAD_MARGIN = 70
size = [SIZE_BLOCK * (COUNT_BLOCKS + 2) + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * (COUNT_BLOCKS + 2) + MARGIN * COUNT_BLOCKS + HEAD_MARGIN]


def draw_block(screen, color, row, column):
    x = (column + 1) * (SIZE_BLOCK + MARGIN)
    y = HEAD_MARGIN + (SIZE_BLOCK + MARGIN) * (row + 1)
    draw.rect(screen, color, [x, y, SIZE_BLOCK, SIZE_BLOCK])


def draw_snake(screen, snake):
    draw_block(screen, SNAKE_COLOR, snake.x, snake.y)


def draw_field(screen):
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = LIGHT_MALLOW
            else:
                color = GHOSTLY_WHITE
            draw_block(screen, color, row, column)
            snake = SnakeBlock(9, 9)
            draw_snake(screen, snake)


def game_loop():
    screen = display.set_mode(size)
    screen.fill(FRAME_COLOR)
    draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEAD_MARGIN])
    while True:
        for ev in event.get():
            if ev.type == QUIT:
                quit()
        display.set_caption("Змейка")
        draw_field(screen)
        display.flip()


if __name__ == '__main__':
    game_loop()
