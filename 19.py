import operator


def junction_route(maze, pos, original_heading):
    headings = [(-1, 0), (1, 0)] if original_heading[0] == 0 else [(0, -1), (0, 1)]
    for heading in headings:
        new_pos = tuple(map(operator.add, pos, heading))
        try:
            cell = maze[new_pos]
            if cell.isalpha() or cell in ['|', '-', '+']:
                return heading
        except (IndexError, KeyError):  # Out of bounds
            pass


with open('data/19.txt') as file:
    lines = file.readlines()
    pos, heading, letters, cell = (lines[0].index('|'), 0), (0, 1), '', '|'
    maze = dict(((x, y), v) for y, line in enumerate(lines) for x, v in enumerate(line))

    # Steps doesn't include the starting step, but does include an extra step at the end
    # where we step into whitespace, so balances out.
    steps = 0

    while cell != ' ':
        pos = tuple(map(operator.add, pos, heading))
        cell = maze[pos]
        steps += 1
        if cell == '+':
            heading = junction_route(maze, pos, heading)
        elif cell.isalpha():
            letters += cell

    print(f'Part one: {letters}')
    print(f'Part two: {steps}')
