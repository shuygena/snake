# import os
from sys import exit
from random import randint
from pygame import display, event, QUIT, quit, draw, time, KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT, font, init
from snake.snake import SnakeBlock
# os.environ["SDL_VIDEODRIVER"] = "dummy" for Linux
# os.environ["SDL_VIDEODRIVER"]="x11" # for WSL

SIZE_BLOCK = 20
WHITE = (255, 255, 255)
LIGHT_MALLOW = (223, 223, 255)
GHOSTLY_WHITE = (245, 245, 255)
FRAME_COLOR = (223, 223, 223)
# HEADER_COLOR = (171, 171, 212)
HEADER_COLOR = (190, 190, 212)
SNAKE_COLOR = (5, 115, 82)
RED = (180, 1, 1)
COUNT_BLOCKS = 20
MARGIN = 1
HEAD_MARGIN = 70
size = [SIZE_BLOCK * (COUNT_BLOCKS + 2) + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * (COUNT_BLOCKS + 2) + MARGIN * COUNT_BLOCKS + HEAD_MARGIN]


def get_random_empty_block(snake_blocks):
    x = randint(0, COUNT_BLOCKS - 1)
    y = randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block._x = randint(0, COUNT_BLOCKS - 1)
        empty_block._y = randint(0, COUNT_BLOCKS - 1)
    return empty_block


def draw_block(screen, color, row, column):
    x = (column + 1) * (SIZE_BLOCK + MARGIN)
    y = HEAD_MARGIN + (SIZE_BLOCK + MARGIN) * (row + 1)
    draw.rect(screen, color, [x, y, SIZE_BLOCK, SIZE_BLOCK])


def draw_snake(screen, snake):
    x = snake.get_x()
    y = snake.get_y()
    draw_block(screen, SNAKE_COLOR, x, y)


def draw_header(screen, score, speed):
    courier = font.SysFont('courier', 42)
    text_score = courier.render(f"Score: {score}", 0, WHITE)
    screen.blit(text_score, (SIZE_BLOCK, SIZE_BLOCK))
    text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
    screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))


def move_snake(screen, snake_blocks, d_row, d_col):
    head = snake_blocks[-1]
    new_head = SnakeBlock(head.get_x() + d_row, head.get_y() + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)


def draw_field(screen, snake_blocks, d_row, d_col, apple):
    draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEAD_MARGIN])
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = LIGHT_MALLOW
            else:
                color = GHOSTLY_WHITE
            draw_block(screen, color, row, column)
    head = snake_blocks[-1]
    if not head.is_inside(SIZE_BLOCK):
        quit()
        exit()
    draw_block(screen, RED, apple.get_x(), apple.get_y())
    for block in snake_blocks:
        draw_snake(screen, block)

    move_snake(screen, snake_blocks, d_row, d_col)


def game_loop():
    init()
    timer = time.Clock()
    screen = display.set_mode(size)
    screen.fill(FRAME_COLOR)
    display.set_caption("Змейка")
    d_row = 0
    d_col = 1
    score = 0
    speed = 1
    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block(snake_blocks)
    while True:
        # d_col = 0
        # d_row = 0
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                exit()
            elif ev.type == KEYDOWN:
                if ev.key == K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif ev.key == K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif ev.key == K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1
                elif ev.key == K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
        if apple == snake_blocks[-1]:
            score += 1
            speed = score // 5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block(snake_blocks)
        draw_field(screen, snake_blocks, d_row, d_col, apple)
        draw_header(screen, score, speed)
        display.flip()
        timer.tick(2 + speed)


if __name__ == '__main__':
    game_loop()
