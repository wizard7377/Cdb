from dataclasses import dataclass
import cdb.syntax as syntax


@dataclass
class ISubprog:
    refr: int


type ICell = Opcode | ISubprog
type Cell = Opcode | Subprog


class Subprog(list[list[ICell]]):
    pass


class Opcode(int):
    pass


class Prog:
    # Actual data
    data: Subprog
    subs: list[Subprog] = []

    growing: bool = False

    def __init__(self, syntax: syntax.Program, growing: bool = False):
        return ...

    def new_subprog(self, subprog: syntax.Program) -> Subprog:


    def __getitem__(self, idx: tuple[int, int]) -> Cell:
        return self.get_at(idx[0], idx[1])

    def get_at(self, x: int, y: int) -> Cell:
        return self.desugar(self._get_at_raw(self.actual_x(y, x), self.actual_y(y)))

    def actual_y(self, y: int) -> int:
        if self.growing:
            return y
        else:
            return y % len(self.data)

    def actual_x(self, y: int, x: int) -> int:
        if self.growing:
            return x
        else:
            return x % len(self.data[self.actual_y(y)])

    def desugar(self, cell: ICell) -> Cell:
        if isinstance(cell, ISubprog):
            return self.subs[cell.refr]
        else:
            return cell

    def _get_at_raw(self, x: int, y: int) -> ICell:
        return self.data[y][x]

    def _set_at_raw(self, x: int, y: int, cell: ICell):
        self.data[y][x] = cell

    def _del_at_raw(self, x: int, y: int):
        del self.data[y][x]
