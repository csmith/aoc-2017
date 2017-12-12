with open('data/12.txt', 'r') as file:
    pipes = list(map(lambda l: l.strip().replace(' <-> ', ', ').split(', '), file.readlines()))
    groups = [set('0')]
    while len(pipes):
        for gi, group in enumerate(groups):
            last_size = 0
            while len(group) != last_size:
                last_size = len(group)
                remove = []
                for pipeset in pipes:
                    if any(program in group for program in pipeset):
                        group = group.union(pipeset)
                        groups[gi] = group
                        remove.append(pipeset)
                for pipeset in remove:
                    pipes.remove(pipeset)
        if len(pipes):
            pipeset = pipes[0]
            groups.append(set(pipeset))
            pipes.remove(pipeset)
    print(f'Part one: {len(groups[0])}')
    print(f'Part two: {len(groups)}')
