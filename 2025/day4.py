#!/usr/bin/env python

def read_data(fname):
    with open(fname, 'rt') as f:
        return f.read().splitlines()


def solve1(data):
    rolls = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '@' and adjacent_rolls(data, x, y) <= 4:
                rolls += 1
    return rolls


def solve2(data):
    rolls = 0
    data = [list(line) for line in data]
    while True:
        positions = set()
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '@' and adjacent_rolls(data, x, y) <= 4:
                    positions.add((x, y))
                    rolls += 1
        if not positions:
            break
        for x, y in positions:
            data[y][x] = 'x'
    return rolls


def adjacent_rolls(data, x, y):
    positions = [
        line[max(0, x - 1):min(len(line), x + 2)] 
        for line in data[max(0, y - 1):min(len(data), y + 2)]
    ]
    return sum(1 for line in positions for c in line if c == '@')



if __name__ == '__main__':
    example_data = list(read_data("day4-example.txt"))
    assert (test_result1 := solve1(example_data)) == 13, test_result1
    assert (test_result2 := solve2(example_data)) == 43, test_result2
    data = list(read_data("day4-input.txt"))
    print(solve1(data))
    print(solve2(data))
