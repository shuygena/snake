class SnakeBlock:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def move_x(self, x):
        self._x += x

    def move_y(self, y):
        self._y += y

    def is_inside(self, size_block):
        return 0 <= self._x < size_block and 0 <= self._y < size_block

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self._x == other._x and self._y == other._y
