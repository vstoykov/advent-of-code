#!/usr/bin/env python
import itertools
import math
from collections import namedtuple
from functools import reduce


Point = namedtuple('Point', 'x,y,z')


def read_data(fname):
    with open(fname, 'rt') as f:
        for line in f.readlines():
            x, y, z = line.split(',')
            yield Point(int(x), int(y), int(z))


def solve1(data, n=10):
    point_circuit_map = {}
    distances = [(pair, distance(*pair)) for pair in itertools.combinations(data, 2)]
    distances.sort(key=lambda x: x[1])
    for (p1, p2), distnace in distances[:n]:
        if circuit1 := point_circuit_map.get(p1):
            if circuit2 := point_circuit_map.get(p2):
                for p in circuit2:
                    circuit1.add(p)
                    point_circuit_map[p] = circuit1
            else:
                circuit1.add(p2)
                point_circuit_map[p2] = circuit1
        elif circuit2 := point_circuit_map.get(p2):
            circuit2.add(p1)
            point_circuit_map[p1] = circuit2
        else:
            circuit = {p1, p2}
            point_circuit_map[p1] = point_circuit_map[p2] = circuit
    
    circuits = {id(c): len(c) for c in point_circuit_map.values()}
    return reduce(lambda a, b: a*b, sorted(circuits.values(), reverse=True)[:3])


def solve2(data):
    total_points = len(data)
    point_circuit_map = {}
    distances = [(pair, distance(*pair)) for pair in itertools.combinations(data, 2)]
    distances.sort(key=lambda x: x[1])
    for (p1, p2), distnace in distances:
        if circuit := point_circuit_map.get(p1):
            if circuit2 := point_circuit_map.get(p2):
                for p in circuit2:
                    circuit.add(p)
                    point_circuit_map[p] = circuit
            else:
                circuit.add(p2)
                point_circuit_map[p2] = circuit
        elif circuit := point_circuit_map.get(p2):
            circuit.add(p1)
            point_circuit_map[p1] = circuit
        else:
            circuit = {p1, p2}
            point_circuit_map[p1] = point_circuit_map[p2] = circuit
        
        if len(circuit) == total_points:
            return p1.x * p2.x
    return 0


def distance(a: Point, b: Point):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)


if __name__ == '__main__':
    example_data = list(read_data("day8-example.txt"))
    assert (test_result1 := solve1(example_data, 10)) == 40, test_result1
    assert (test_result2 := solve2(example_data)) == 25272, test_result2
    data = list(read_data("day8-input.txt"))
    print(solve1(data, 1000))
    print(solve2(data))
