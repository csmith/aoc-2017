from shared import knot_hash, add_connected_components

with open('data/14.txt', 'r') as file:
    seed = file.readline().strip()
    grid = '\n'.join([bin(int(knot_hash(f'{seed}-{i}'), 16))[2:].zfill(128) for i in range(128)])

    count = 0
    regions = []
    for offset, cell in enumerate(grid):
        if cell == '1':
            count += 1
            add_connected_components(regions, [offset-1, offset-129], {offset})
    print(f'Part one: {count}')
    print(f'Part two: {len(regions)}')
