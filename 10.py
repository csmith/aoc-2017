import functools
import itertools
import operator


def reverse_slice(input, start, length):
    output = list(input)
    for i, pos in enumerate(range(start, start + length)):
        output[pos % len(output)] = input[(start + length - i - 1) % len(output)]
    return output


def do_rounds(lengths, count=1):
    position, skip, data = 0, 0, list(range(256))
    for _ in range(count):
        for length in lengths:
            data = reverse_slice(data, position, length)
            position += length + skip
            skip += 1
    return data


def group(n, iterable):
    # https://docs.python.org/3.1/library/itertools.html#recipes
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


with open('data/10.txt', 'r') as file:
    lengths = list(map(int, file.readline().strip().split(',')))
    data = do_rounds(lengths)
    print(f'Part one: {data[0]*data[1]}')


with open('data/10.txt', 'r') as file:
    lengths = list(map(ord, file.readline().strip())) + [17, 31, 73, 47, 23]
    sparse_hash = do_rounds(lengths, 64)
    dense_hash = [functools.reduce(operator.xor, g) for g in group(16, sparse_hash)]
    # Yo dawg, I heard you like f-strings, so we put an f-string in your f-string.
    print(f'Part two: {"".join(f"{c:02x}" for c in dense_hash)}')
