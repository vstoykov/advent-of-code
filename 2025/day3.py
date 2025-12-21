#!/usr/bin/env python

def read_data(fname):
    with open(fname, 'rt') as f:
        for line in f:
            yield tuple(map(int, line.strip()))


def solve1(data):
    return sum(joltage(bank, 2) for bank in data)


def solve2(data):
    return sum(joltage(bank, 12) for bank in data)


def joltage(bank, digits):
    jltg = 0
    for p in range(digits, 0, -1):
        bigest = max(bank[:len(bank) - p + 1])
        bi = bank.index(bigest)
        jltg += bigest * (10 ** (p - 1))
        bank = bank[bi+1:]
    return jltg


if __name__ == '__main__':
    example_data = list(read_data("day3-example.txt"))
    assert (test_result1 := solve1(example_data)) == 357, test_result1
    assert (test_result2 := solve2(example_data)) == 3121910778619, test_result2
    data = list(read_data("day3-input.txt"))
    print(solve1(data))
    print(solve2(data))
