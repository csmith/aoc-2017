import functools

with open('data/12.txt', 'r') as file:
    sets = []
    pipes = list(map(lambda l: l.strip().replace(' <-> ', ', ').split(', '), file.readlines()))
    for pipe in pipes:
        overlapping = [s for s in sets if any(program in s for program in pipe)]
        for overlap in overlapping:
            sets.remove(overlap)
        sets.append(functools.reduce(set.union, overlapping, set(pipe)))

    print(f'Part one: {len(next(s for s in sets if "0" in s))}')
    print(f'Part two: {len(sets)}')