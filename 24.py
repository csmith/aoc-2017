
with open('data/24.txt') as file:
    connectors = [tuple(map(int, line.strip().split('/'))) for line in file.readlines()]

    def search(connector, chain, available):
        possible = [c for c in available if c[0] == connector or c[1] == connector]
        if len(possible) == 0:
            return [chain]
        else:
            chains = []
            for p in possible:
                new_chain = list(chain) + [p]
                new_available = list(available)
                new_available.remove(p)
                chains += search(sum(p) - connector, new_chain, new_available)
            return chains

    chains = search(0, [], connectors)
    print(f'Part one: {max(sum(sum(p) for p in chain) for chain in chains)}')
    longest = max(len(chain) for chain in chains)
    print(f'Part two: {max(sum(sum(p) for p in chain) for chain in chains if len(chain) == longest)}')
