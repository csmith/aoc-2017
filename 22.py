import operator
from collections import defaultdict
from enum import Enum


class State(Enum):
    clean = 0,
    weakened = 1,
    infected = 2,
    flagged = 3


def clean_cells():
    cells = defaultdict(lambda: State.clean)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            cells[(x, y)] = State.infected if c == '#' else State.clean
    return cells


def execute(runs, transitions):
    cells, location, direction, infected = clean_cells(), start, (0, -1), 0
    for _ in range(runs):
        direction = directions[cells[location]][direction]
        cells[location] = transitions[cells[location]]
        if cells[location] == State.infected:
            infected += 1
        location = tuple(map(operator.add, location, direction))
    return infected


with open('data/22.txt') as file:
    lines = file.readlines()
    start = ((len(lines[0]) - 1) // 2, (len(lines) - 1) // 2)

    right = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    left = {v: k for k, v in right.items()}
    identity = {v: v for v in right.values()}
    reverse = {v: (-1 * v[0], -1 * v[1]) for v in right.values()}

    directions = {
        State.clean: left,
        State.infected: right,
        State.weakened: identity,
        State.flagged: reverse
    }

    transitions = [
        {
            # part one
            State.clean: State.infected,
            State.infected: State.clean,
        },
        {
            # part two
            State.clean: State.weakened,
            State.weakened: State.infected,
            State.infected: State.flagged,
            State.flagged: State.clean,
        }
    ]

    print(f'Part one: {execute(10000, transitions[0])}')
    print(f'Part two: {execute(10000000, transitions[1])}')
