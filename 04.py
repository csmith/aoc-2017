with open('data/04.txt', 'r') as file:
    phrases = list(map(str.split, file.readlines()))
    sorted_phrases = map(lambda p: list(map(sorted, p)), phrases)
    print(f'Part one: {sum(1 for p in phrases if not any(p.count(w) > 1 for w in p))}')
    print(f'Part two: {sum(1 for p in sorted_phrases if not any(p.count(w) > 1 for w in p))}')
