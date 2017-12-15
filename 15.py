import itertools
import operator


def gen(seed, factor, multiple=1):
    value = seed
    while True:
        value = (value * factor) % 2147483647
        if value % multiple == 0:
            yield value & 65535


with open('data/15.txt', 'r') as file:
    seeds = [int(line.strip().split()[-1]) for line in file.readlines()]
    print(f'Part one: {sum(map(lambda t: t[0] == t[1], itertools.islice(zip(gen(seeds[0], 16807), gen(seeds[1], 48271)), 40_000_000)))}')
    print(f'Part two: {sum(map(lambda t: t[0] == t[1], itertools.islice(zip(gen(seeds[0], 16807, 4), gen(seeds[1], 48271, 8)), 5_000_000)))}')
