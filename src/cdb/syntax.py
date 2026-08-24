from typing import Union, Literal, assert_type
from dataclasses import dataclass
import re

debug = __name__ == "__main__"


def debug_print(m: str):
    if debug:
        print(m)


@dataclass
class IntLit:
    intLit: int


@dataclass
class StrLit:
    strLit: str


type Program = list[list[Code]]


@dataclass
class Nested:
    subprog: Program


@dataclass
class Opcode:
    value: str


type Code = Nested | Opcode

type PRes[T] = tuple[T, str]


class ParseError(Exception):
    def __init__(self, msg):
        self.msg = msg


# Text at point (including brace) should be included
def get_match(s: str, begin: str, end: str) -> int:
    """
    Takes a input string, which starts with '{', and returns the first point at which the number of { and } are balenced
    """
    depth = 1
    assert s[0] == begin
    i = 1
    while (i < len(s)) and (depth > 0):
        if s[i] == begin:
            depth += 1
        elif s[i] == end:
            depth -= 1
        else:
            pass

        if depth <= 0:
            return i
        else:
            i += 1

    raise ParseError("Brace not matched")


def get_word(s: str) -> tuple[str, str]:
    return (s[0], s[1:])


def parse1(s: str) -> PRes[Code | Literal["\n"]]:
    """
    Parse exactly one element from the input (either a sub proc, and number lit, a string lit, or an opcode)
    """
    debug_print(f"Parsing {s}")
    # Nesting of the parse
    if s[0] == "{":
        i = get_match(s, "{", "}")
        debug_print(f"Nested @ {i}")
        r = parse(s[1:i])
        return (Nested(r), s[i:])
        return (r, s[i:])
    elif s[0] == "\n" or s[0] == "\\":
        debug_print("newline")
        return ("\n", s[1:])
    elif s[0].isspace():
        assert s[0] != "\n"  # Per above branch
        return parse1(s[1:])
    else:
        r, t = get_word(s)
        return (Opcode(r), t)


def parse(s: str) -> Program:
    cur: str = s
    acc: Program = []
    res: list[Code] = []
    while len(cur) > 0:
        try:
            r: PRes[Code | Literal["\n"]] = parse1(cur)
            pt = r[0]
            cur = r[1]
            if pt == "\n":
                list.append(acc, res)
                res = []
            else:
                list.append(res, pt)
        except ParseError as e:
            es = s
            es.removesuffix(cur)
            epos = len(es)
            raise ParseError(f"Couldn't finish parsing, got {e}, at pos {epos}")

    list.append(acc, res)
    assert len(cur) <= 0
    return acc


if debug:
    testInput = """
fetea[xy[uj]]{isa{nested}}
nope, nothing here
    """
    testOutput = parse(testInput)
    print(testOutput)
