import operator
import re
from collections import defaultdict

POS, VEL, ACC = 0, 1, 2

with open('data/20.txt') as file:
    pattern = re.compile(r'<(.*?),(.*?),(.*?)>')
    particles = list([list(map(int, part)) for part in pattern.findall(line)] for line in file.readlines())

    # Part one: I'm not sure this will work for all inputs. This is just a rough approximation
    # based on the fastest acceleration and then velocity. It's possible that some input will
    # have multiple particles with the same acceleration and velocity, or that a higher
    # velocity will be better as it works against the acceleration. It should probably be
    # simulated fully, instead.

    # Acceleration will always win out in the long run
    min_acc = min(sum(map(abs, p[ACC])) for p in particles)
    slowest = [(i, p) for i, p in enumerate(particles) if sum(map(abs, p[ACC])) == min_acc]
    # Tie-break using velocity...
    print(f'Part one: {min(slowest, key=lambda indexed: sum(map(abs, indexed[1][VEL])))[0]}')

    last_collision = 0
    while last_collision < 1000:  # Assume if we don't collide in 1k iterations, we'll never collide
        last_collision += 1
        positions = defaultdict(list)
        for i, particle in enumerate(particles):
            particle[VEL] = list(map(operator.add, particle[VEL], particle[ACC]))
            particle[POS] = list(map(operator.add, particle[POS], particle[VEL]))
            pos_key = ','.join(map(str, particle[POS]))
            positions[pos_key].append(particle)
        for overlaps in positions.values():
            if len(overlaps) > 1:
                particles = [p for p in particles if p not in overlaps]
                last_collision = 0

    print(f'Part two: {len(particles)}')
