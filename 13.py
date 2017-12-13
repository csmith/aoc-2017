import itertools

with open('data/13.txt', 'r') as file:
    layers = dict(map(lambda l: tuple(map(int, l.strip().split(': '))), file.readlines()))
    print(f'Part one: {sum(offset * length for offset, length in layers.items() if offset % ((length-1) * 2) == 0)}')
    print(f'Part two: {next(delay for delay in itertools.count() if all((offset + delay) % ((length - 1) * 2) != 0 for offset, length in layers.items()))}')
