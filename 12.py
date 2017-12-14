from shared import add_connected_components

with open('data/12.txt', 'r') as file:
    sets = []
    pipes = list(map(lambda l: l.strip().replace(' <-> ', ', ').split(', '), file.readlines()))
    for pipe in pipes:
        add_connected_components(sets, pipe)

    print(f'Part one: {len(next(s for s in sets if "0" in s))}')
    print(f'Part two: {len(sets)}')