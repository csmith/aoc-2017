import functools

from shared import knot_hash, add_connected_components

with open('data/14.txt', 'r') as file:
    seed = file.readline().strip()
    grid = [bin(int(knot_hash(f'{seed}-{i}'), 16))[2:].zfill(128) for i in range(128)]
    print(f'Part one: {sum(row.count("1") for row in grid)}')

    regions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '1':
                add_connected_components(regions, [(x-1, y), (x, y-1), (x+1, y), (x, y+1)], {(x, y)})
    print(f'Part two: {len(regions)}')
