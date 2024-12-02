#/usr/bin/env python3
import sys
import itertools


def solve1(rows: list[int]) -> int:
    return sum(map(is_safe, rows))


def solve2(rows: list[int]) -> int:
    return sum(map(is_safeish, rows))


def is_safe(row: list[int]) -> bool:
    return any(
        all(0 < s - ns < 4 for s, ns in itertools.pairwise(r)) 
        for r in (row, row[::-1])
    )

def is_safeish(row: list[int]) -> bool:
    if is_safe(row):
        return True
    for i in range(len(row)):
        if is_safe(row[:i] + row[i+1:]):
            return True
    return False


def read_data(fname: str) -> list[int]:
    with open(fname) as f:
        return [[int(x) for x in l.split()] for l in f]


if __name__ == "__main__":
    try:
        test_data = read_data("day2-test-input.txt")
        assert (result1 := solve1(test_data)) == 2, result1
        assert (result2 := solve2(test_data)) == 4, result2

        data = read_data("day2-input.txt")
        print(f"solve1: {solve1(data)}")
        print(f"solve2: {solve2(data)}")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        exit(1)
