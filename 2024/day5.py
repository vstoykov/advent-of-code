#/usr/bin/env python3
from collections import defaultdict
from functools import cmp_to_key
import sys


def solve1(rules: dict[int, list[int]], updates: list[int]) -> int:
    s = 0
    for update in updates:
        if all(np in rules[p] for p, np in zip(update, update[1:])):
            s += update[int(len(update) / 2)]
    return s

def solve2(rules: dict[int, list[int]], updates: list[int]) -> int:
    s = 0
    for update in updates:
        if not all(np in rules[p] for p, np in zip(update, update[1:])):
            update = sorted(update, key=cmp_to_key(lambda p, np: -1 if np in rules[p] else 1))
            s += update[int(len(update) / 2)]
    return s


def read_data(fname: str) -> tuple[dict[int, list[int]], list[int]]:
    rules = defaultdict(list)
    updates = []
    parse_rules = True
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if parse_rules:
                if not line:
                    parse_rules = False
                    continue
                x, y = line.split('|')
                rules[int(x)].append(int(y))
            else:
                updates.append(list(int(x) for x in line.split(',')))
    return rules, updates


if __name__ == "__main__":
    try:
        test_data = read_data("day5-test-input.txt")
        assert (result1 := solve1(*test_data)) == 143, result1
        assert (result2 := solve2(*test_data)) == 123, result2

        data = read_data("day5-input.txt")
        print(f"solve1: {solve1(*data)}")
        print(f"solve2: {solve2(*data)}")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        exit(1)
