from typing import Tuple

from enum import Enum


class Direct(Enum):
    UP = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4


type Program = list[list[int]]
type Pos = Tuple[int, int]
type Opcode = int
type Register = int
type Stack = list[Register]


def dx(d: Direct) -> int:
    match d:
        case Direct.LEFT:
            return -1
        case Direct.RIGHT:
            return +1
        case _:
            return 0


def dy(d: Direct) -> int:
    match d:
        case Direct.DOWN:
            return -1
        case Direct.UP:
            return +1
        case _:
            return 0


def move_pos(pos: Pos, dx: int, dy: int):
    return (pos[0] + dx, pos[1] + dy)


class Cdb:
    prog: Program
    data: Stack
    point: Pos
    direct: Direct
    str_mode: bool

    def __init__(self, code: str):
        lines = code.split("\n")
        self.prog = [[int(x) for x in line] for line in lines]
        self.data = []
        self.point: Pos = 0, 0
        self.direct = Direct.RIGHT
        self.str_mode = False

    def get_at_point(self) -> Opcode:
        return self.prog[self.point[0]][self.point[1]]

    def move(self):
        self.pos = move_pos(self.pos, dx(self.direct), dy(self.direct))

    def pop_stack(self, n: int) -> list[Register]:
        r = self.stack[:n]
        self.stack = self.stack[n:]
        return r

    def push_stack(self, st: Stack):
        self.stack = st + self.stack

    # Note that this shouldn't actually do the movement (unless action calls for it).
    # Returns true if the program should continue execution
    def do_action(self) -> bool:
        cur = self.get_at_point()
        if cur == "@":
            return False
