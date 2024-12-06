#/usr/bin/env python3
import sys
import re
import itertools
from typing import Iterable


def solve1(matrix: list[str]) -> int:
    transposed = map(''.join, zip(*matrix))
    diags = find_diagonals(matrix)
    pattern = re.compile(r"(?=XMAS|SAMX)", re.MULTILINE)
    return sum(
        len(re.findall(pattern, line))
        for line in itertools.chain(matrix, transposed, diags)
    )


def find_diagonals(matrix: list[str], min_length=4) -> Iterable[str]:
    max_col = len(matrix[0]) 
    max_row = len(matrix)
    for col in range(max_col - min_length + 1):
        fdiag = []
        bdiag = []
        for x in range(col, max_col):
            y = x - col
            fdiag.append(matrix[y][x])
            bdiag.append(matrix[y][-x - 1])
        yield ''.join(fdiag)
        yield''.join(bdiag)
    for row in range(1, max_row - min_length + 1):
        fdiag = []
        bdiag = []
        for x in range(max_col - row):
            y = x + row
            fdiag.append(matrix[y][x])
            bdiag.append(matrix[y][-x - 1])
        yield ''.join(fdiag)
        yield ''.join(bdiag)


def solve2(matrix: list[str]) -> int:
    s = 0
    words = ('MS', 'SM')
    for y, line in enumerate(matrix[1:-1], 1):
        for x in (m.span()[0] for m in re.finditer(r'A', line)):
            if x == 0:
                continue
            try:
                ds = (
                    matrix[y-1][x-1] + matrix[y+1][x+1],
                    matrix[y+1][x-1] + matrix[y-1][x+1],
                )
            except IndexError:
                continue
            if all(d in words for d in ds):
                s += 1
    return s



def read_data(fname: str) -> list[str]:
    with open(fname) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    try:
        test_data = read_data("day4-test-input.txt")
        assert (result1 := solve1(test_data)) == 18, result1
        assert (result2 := solve2(test_data)) == 9, result2

        data = read_data("day4-input.txt")
        print(f"solve1: {solve1(data)}")
        print(f"solve2: {solve2(data)}")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        exit(1)
