import itertools
with open('data/02.txt', 'r') as file:
    sheet = list(map(lambda row: list(map(int, row.split('\t'))), file.readlines()))
    print(f'Part one: {sum(max(row) - min(row) for row in sheet)}')
    print(f'Part two: {sum(next(a//b for a,b in itertools.permutations(row, 2) if a % b == 0) for row in sheet)}')
