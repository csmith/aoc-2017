from types import SimpleNamespace

programs = {}

with open('data/07.txt', 'r') as file:
    for line in file.readlines():
        details = line.strip().split(' -> ')[0]
        children = line.strip().split(' -> ')[1].split(', ') if '->' in line else []
        name, weight = details.split(' ')
        weight = int(weight.strip('()'))
        programs[name] = SimpleNamespace(name=name, weight=weight, total_weight=-1, child_names=children, children=[])

roots = list(programs.keys())
leaves = []

for program in list(programs.values()):
    for child in program.child_names:
        program.children.append(programs[child])
        programs[child].parent = program
        roots.remove(child)
    if len(program.children) == 0:
        leaves.append(program)


def resolve_weight(program):
    if program.total_weight == -1:
        program.total_weight = program.weight + sum(resolve_weight(child) for child in program.children)
    return program.total_weight


def check_weight(program):
    weights = [child.total_weight for child in program.children]
    for child in program.children:
        if weights.count(child.total_weight) == 1:
            return check_weight(child) or next(w for w in weights if w != child.total_weight) - sum(c.total_weight for c in child.children)


resolve_weight(programs[roots[0]])
print(f'Part one: {programs[roots[0]].name}')
print(f'Part two: {check_weight(programs[roots[0]])}')