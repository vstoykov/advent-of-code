#/usr/bin/env python3
import sys
from collections import Counter


def solve1(rows: list[int]) -> int:
    return sum(abs(l - r) for l, r in zip(*map(sorted, zip(*rows))))


def solve2(rows: list[int]) -> int:
    list1, list2 = zip(*rows)
    apearances = Counter(list2)
    return sum(item * apearances.get(item, 0) for item in list1)


def read_data(fname: str) -> list[int]:
    with open(fname) as f:
        return [[int(x) for x in l.split()] for l in f]


if __name__ == "__main__":
    try:
        test_data = read_data("day1-test-input.txt")
        assert (result1 := solve1(test_data)) == 11, result1
        assert (result2 := solve2(test_data)) == 31, result2

        data = read_data("day1-input.txt")
        print(f"solve1: {solve1(data)}")
        print(f"solve2: {solve2(data)}")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        exit(1)
