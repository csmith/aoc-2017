import string
from functools import partial


def spin(amount, line):
    return line[-amount:] + line[:-amount]


def exchange(p1, p2, line):
    line[p1], line[p2] = line[p2], line[p1]
    return line


def partner(n1, n2, line):
    p1, p2 = line.index(n1), line.index(n2)
    line[p1], line[p2] = line[p2], line[p1]
    return line


def dance(reps, moves):
    line = list(string.ascii_lowercase[:16])
    # Maintain a history to try and find cycles. If we ever generate the same line twice
    # then all of the remainder will just cycle between those two lines.
    history = []
    for i in range(reps):
        for move in moves:
            line = move(line)
        if line in history:
            start = history.index(line)
            cycle = len(history) - start
            return ''.join(history[start + (reps - i - 1) % cycle])
        history.append(line[:])  # NB: Copy of the line, so it doesn't get mutated next cycle...
    return ''.join(line)


instructions = {
    's': lambda r: partial(spin, int(r)),
    'x': lambda r: partial(exchange, *map(int, r.split('/'))),
    'p': lambda r: partial(partner, *r.split('/'))
}

with open('data/16.txt', 'r') as file:
    # Pre-parse the list of moves into function calls to save string-fiddling lots of times
    moves = list(map(lambda line: instructions[line[0]](line[1:]), file.readline().strip().split(',')))
    print(f'Part one: {dance(1, moves)}')
    print(f'Part two: {dance(1000000000, moves)}')
