#!/usr/bin/env python
import math


def read_data(fname):
    with open(fname, 'rt') as f:
        return [(line[0], int(line[1:])) for line in f]


def solve1(data):
    pos = 50
    count = 0
    for dir, clicks in data:
        clicks %= 100
        if dir == 'R':
            pos += clicks
            if pos >= 100:
                pos -= 100
        if dir == 'L':
            pos -= clicks
            if pos < 0:
                pos = 100 + pos
        
        if pos == 0:
            count += 1
    return count


def solve2(data):
    pos = 50
    count = 0
    for dir, clicks in data:
        count += math.floor(clicks / 100)
        clicks %= 100
        
        if dir == 'R':
            pos += clicks
            if pos >= 100:
                pos -= 100
                count += 1
        
        elif dir == 'L':
            old_pos = pos
            pos -= clicks
            if pos < 0:
                pos = 100 + pos
                if old_pos != 0:
                    count += 1

            elif pos == 0:
                count += 1
    return count


if __name__ == '__main__':
    example_data = read_data("day1-example.txt")
    assert 3 == solve1(example_data)
    assert 6 == solve2(example_data)
    data = read_data("day1-input.txt")
    print(solve1(data))
    print(solve2(data))
