#!/usr/bin/env python

from collections import defaultdict


def read_data(fname):
    with open(fname, 'rt') as f:
        return f.readlines()


def solve1(data):
    result = 0
    start = data[0].index('S')
    beams = {start}
    for line in data[1:]:
        splitters = find_splitters(line)
        if not splitters:
            continue

        for beam in list(beams):
            if beam in splitters:
                beams.add(beam - 1)
                beams.add(beam + 1)
                beams.remove(beam)
                result += 1
    
    return result


def solve2(data):
    start = data[0].index('S')
    beams = defaultdict(lambda: 0)
    beams[start] = 1
    for line in data[1:]:
        splitters = find_splitters(line)
        if not splitters:
            continue
        
        for beam, timelines in list(beams.items()):
            if beam in splitters:
                beams[beam - 1] += timelines
                beams[beam + 1] += timelines
                beams.pop(beam)

    return sum(beams.values())


def find_splitters(line):
    pos = []
    current = 0
    while True:
        try:
            i = line.index('^', current)
        except ValueError:
            break
        pos.append(i)
        current = i + 1
    return pos


if __name__ == '__main__':
    example_data = read_data("day7-example.txt")
    assert (test_result1 := solve1(example_data)) == 21, test_result1
    assert (test_result2 := solve2(example_data)) == 40, test_result2
    data = read_data("day7-input.txt")
    print(solve1(data))
    print(solve2(data))
