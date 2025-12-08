#!/usr/bin/env python

def read_data(fname):
    with open(fname, 'rt') as f:
        return [tuple(map(int, r.split('-'))) for r in f.read().split(',')]


def solve1(data):
    result = 0
    for begin, end in data:
        for item in range(begin, end + 1):
            if is_invalid1(item):
                result += item            
    return result


def is_invalid1(item):
    item = str(item)
    if len(item) % 2 != 0:
        return False
    half = len(item) // 2
    return item[:half] == item[half:]


def solve2(data):
    result = 0
    for begin, end in data:
        for item in range(begin, end + 1):
            if is_invalid2(item):
                result += item 
    return result


def is_invalid2(item):
    item = str(item)
    if len(item) > 1 and len(set(item)) == 1:
        return True
    for n in range(2, len(item)):
        parts = tuple(chunks(item, n))
        if len(set(parts)) == 1:
            return True
    return False


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    example_data = read_data("day2-example.txt")
    assert (test_result1 := solve1(example_data)) == 1227775554, test_result1
    assert (test_result2 := solve2(example_data)) == 4174379265, test_result1
    data = read_data("day2-input.txt")
    print(solve1(data))
    print(solve2(data))
