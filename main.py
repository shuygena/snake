import os
from pygame import display, event, QUIT, quit

# os.environ["SDL_VIDEODRIVER"] = "dummy" for Linux
# os.environ["SDL_VIDEODRIVER"]="x11" # for WSL
SIZE = [400, 600]

def game_loop():
    screen = display.set_mode(SIZE)
    display.set_caption("Змейка")
    while True:
        for ev in event.get():
            if ev.type == QUIT:
                quit()

if __name__ == '__main__':
    game_loop()