import collections

reductions = [
    # Simplifications
    [ 'n', 'se', 'ne'],
    [ 'n', 'sw', 'nw'],
    [ 's', 'ne', 'se'],
    [ 's', 'nw', 'sw'],
    ['sw', 'se',  's'],
    ['nw', 'ne',  'n'],
    # Opposites
    [ 'n',  's', '--'],
    ['sw', 'ne', '--'],
    ['nw', 'se', '--'],
]


def distance(steps):
    counts = collections.defaultdict(lambda: 0, collections.Counter(steps))
    last_counts = dict()
    while counts != last_counts:
        last_counts = dict(counts)
        for a, b, result in reductions:
            count = min(counts[a], counts[b])
            counts[a] -= count
            counts[b] -= count
            counts[result] += count
    counts['--'] = 0
    return sum(counts.values())


with open('data/11.txt', 'r') as file:
    steps = file.readline().strip().split(',')
    print(f'Part one: {distance(steps)}')
    print(f'Part two: {max(distance(steps[:i]) for i in range(len(steps)))}')
