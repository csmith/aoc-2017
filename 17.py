with open('data/17.txt', 'r') as file:
    steps = int(file.readline().strip())
    buffer = []
    position = 0
    for i in range(2018):
        buffer.insert(position, i)
        position = (position + steps + 1) % (i + 1)
    print(f'Part one: {buffer[(buffer.index(2017) + 1) % len(buffer)]}')

    # The entry for zero is always at the end of our buffer, as we never call insert beyond the length of the list,
    # so the entry after zero is always the one at position 0.
    for i in range(2018, 50000001):
        if position == 0:
            after_zero = i
        position = (position + steps + 1) % (i + 1)
    print(f'Part two: {after_zero}')