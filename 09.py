with open('data/09.txt', 'r') as file:
    garbage, escaped, depth, score, removed = False, False, 0, 0, 0
    for char in file.readline():
        if escaped:
            escaped = False
        elif garbage:
            if char == '!':
                escaped = True
            elif char == '>':
                garbage = False
            else:
                removed += 1
        elif char == '<':
            garbage = True
        elif char == '{':
            depth += 1
            score += depth
        elif char == '}':
            depth -= 1

print(f'Part one: {score}')
print(f'Part two: {removed}')