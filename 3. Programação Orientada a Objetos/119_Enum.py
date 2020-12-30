"""Enum
Quando precisa escolher algo sem sair"""
from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    # if direction != 'right' and direction != "left":
    #     raise ValueError("Cannot moe in this direction")

    if not isinstance(direction, Directions):
        raise ValueError("Cannot moe in this direction")
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    print(move('left'))
