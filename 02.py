import itertools
with open('data/02.txt', 'r') as file:
    sheet = map(lambda row: map(int, row.split('\t')), file.readlines())
    print('Part one: %s' % sum(max(row) - min(row) for row in sheet))
    print('Part two: %s' % sum(next(a//b for a,b in itertools.permutations(row, 2) if a % b == 0) for row in sheet))
