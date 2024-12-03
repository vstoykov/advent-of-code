#/usr/bin/env python3
import sys
import re

def solve1(data: str) -> int:
    rows = re.findall(r'mul\((\d+),(\d+)\)', data, re.MULTILINE)
    return sum(int(a) * int(b) for a, b in rows)


def solve2(data: str) -> int:
    rows = re.findall(r'(mul\((\d+),(\d+)\)|do(n\'t)?\(\))', data, re.MULTILINE)
    sum, should_do = 0, True
    for op, a, b, *_ in rows:
        if op.startswith("mul"):
            if should_do:
                sum += int(a) * int(b)
        elif op.startswith("don't"):
            should_do = False
        elif op.startswith("do"):
            should_do = True
        else:
            raise ValueError(f"Unknown operation: {op}")
    return sum


def read_data(fname: str) -> list[int]:
    with open(fname) as f:
        return f.read()


if __name__ == "__main__":
    try:
        test_data1 = read_data("day3-test-input.txt")
        assert (result1 := solve1(test_data1)) == 161, result1
        test_data2 = read_data("day3-test-input2.txt")
        assert (result2 := solve2(test_data2)) == 48, result2

        data = read_data("day3-input.txt")
        print(f"solve1: {solve1(data)}")
        print(f"solve2: {solve2(data)}")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        exit(1)
