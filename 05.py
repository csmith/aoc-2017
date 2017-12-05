def execute(instructions, incrementor, position=0):
    while 0 <= position < len(instructions):
        next_position = position + instructions[position]
        instructions[position] += incrementor(instructions[position])
        position = next_position
        yield position


with open('data/05.txt', 'r') as file:
    instructions = list(map(int, file.readlines()))
    print(f'Part one: {sum(1 for _ in execute(list(instructions), lambda x: 1))}')
    print(f'Part two: {sum(1 for _ in execute(list(instructions), lambda x: -1 if x >= 3 else 1))}')
