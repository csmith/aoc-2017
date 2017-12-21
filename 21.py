import numpy as np

with open('data/21.txt') as file:
    mappings = dict()
    for line in file.readlines():
        parts = tuple(map(lambda p: np.array(list(map(lambda r: [c == '#' for c in r], p.split('/')))),
                          line.strip().split(' => ')))

        # All possible transformations of our mappings:
        #  - 0, 90, 180 and 270 degree rotations
        #  - vertical (up<>down) flip followed by the 4 rotations
        #  - horizontal (left<>right) flip followed by the 4 rotations
        # ...Some of these may be equivalent...
        keys = [
            *(np.rot90(parts[0], k) for k in range(3)),
            *(np.rot90(np.flipud(parts[0]), k) for k in range(3)),
            *(np.rot90(np.fliplr(parts[0]), k) for k in range(3)),
        ]

        for key in keys:
            mappings[key.tobytes()] = parts[1]


    def expand(old_grid, length, oss, nss):
        """
        Expands a grid by replacing all segments with their mapped versions.

        :param old_grid: The grid to expand
        :param length: The current size of the grid (length in any direction)
        :param oss: The size of the segment to be replaced (old segment size)
        :param nss: The size of the segment that will replace it (new segment size)
        :return: A new grid, with each segment expanded
        """
        new_grid = np.empty((length // oss * nss, length // oss * nss), dtype=bool)
        for x in range(0, length, oss):
            for y in range(0, length, oss):
                new_x = x // oss * nss
                new_y = y // oss * nss
                new_grid[new_x:new_x+nss, new_y:new_y+nss] = mappings[old_grid[x:x + oss, y:y + oss].tobytes()]
        return new_grid


    grid = np.array([[False, True, False], [False, False, True], [True, True, True]])
    for i in range(18):
        size = len(grid)
        grid = expand(grid, size, 2, 3) if size % 2 == 0 else expand(grid, size, 3, 4)

        if i == 4:
            print(f'Part one: {sum(sum(grid))}')
        elif i == 17:
            print(f'Part two: {sum(sum(grid))}')
