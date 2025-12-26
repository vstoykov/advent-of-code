#!/usr/bin/env python
from functools import reduce

def read_data(fname):
    with open(fname, 'rt') as f:
        data = f.readlines()
    
    numbers = data[:-1]
    operations = data[-1].strip().split()
            
    return numbers, operations


def solve1(data, operations):
    numbers = [list(map(int, x.strip().split())) for x in data]
    size = len(numbers)
    ops = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
    }
    result = 0
    for x, operation in enumerate(operations):
        result += reduce(ops[operation], [numbers[y][x] for y in range(size)]) 
    
    return result


def solve2(data, operations):
    max_y = len(data)
    max_x = len(data[0])
    ops = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
    }

    i = 0
    buffer = []
    result = 0

    for x in range(max_x):
        try:
            buffer.append(int(''.join(data[y][x] for y in range(max_y)).strip()))
        except ValueError:
            result += reduce(ops[operations[i]], buffer)
            buffer = []
            i += 1
    
    return result


if __name__ == '__main__':
    example_data = list(read_data("day6-example.txt"))
    assert (test_result1 := solve1(*example_data)) == 4277556, test_result1
    assert (test_result2 := solve2(*example_data)) == 3263827, test_result2
    data = list(read_data("day6-input.txt"))
    print(solve1(*data))
    print(solve2(*data))
