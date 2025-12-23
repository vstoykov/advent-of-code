#!/usr/bin/env python

def read_data(fname):
    ranges = []
    body = False
    data = []
    with open(fname, 'rt') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                body = True
                continue
            
            if body:
                data.append(int(line))
                continue
            
            b, e = line.strip().split('-')
            ranges.append(range(int(b), int(e) + 1))
            
    return ranges, data


def solve1(ranges, data):
    return sum(any(n in r for r in ranges) for n in data)


def solve2(ranges, data):
    fresh = 0
    ranges = sorted(ranges, key=lambda r: r.start)
    combined = [ranges[0]]
    for current in ranges[1:]:
        last = combined[-1]
        if current.start in last:
            combined[-1] = range(last.start, max(last.stop, current.stop))
        else:
            combined.append(current)
    for r in combined:
        fresh += r.stop - r.start
    return fresh


if __name__ == '__main__':
    example_data = list(read_data("day5-example.txt"))
    assert (test_result1 := solve1(*example_data)) == 3, test_result1
    assert (test_result2 := solve2(*example_data)) == 14, test_result2
    data = list(read_data("day5-input.txt"))
    print(solve1(*data))
    print(solve2(*data))
