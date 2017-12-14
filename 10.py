from shared import knot_hash, knot_hash_rounds

with open('data/10.txt', 'r') as file:
    lengths = list(map(int, file.readline().strip().split(',')))
    data = knot_hash_rounds(lengths)
    print(f'Part one: {data[0]*data[1]}')

with open('data/10.txt', 'r') as file:
    print(f'Part two: {knot_hash(file.readline().strip())}')
