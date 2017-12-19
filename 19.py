import operator


def junction_routes(maze, pos):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
        new_pos = tuple(map(operator.add, pos, dir))
        try:
            cell = maze[new_pos[1]][new_pos[0]]
            if cell.isalpha() or cell in ['|', '-', '+']:
                yield dir
        except:
            # Out of bounds
            pass


with open('data/19.txt', 'r') as file:
    maze = file.readlines()
    p, d, h, cell = (maze[0].index('|'), 0), (0, 1), [], '|'

    # Steps doesn't include the starting step, but does include an extra step at the end
    # where we step into whitespace, so balances out.
    steps = 0

    while cell != ' ':
        p = tuple(map(operator.add, p, d))
        cell = maze[p[1]][p[0]]
        steps += 1
        if cell == '+':
            d = next(o for o in junction_routes(maze, p) if o != (-d[0], -d[1]))
        elif cell.isalpha():
            h.append(cell)

    print(f'Part one: {"".join(h)}')
    print(f'Part two: {steps}')
