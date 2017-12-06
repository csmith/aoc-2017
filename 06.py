import operator


def redistribute(buckets):
    while True:
        max_index, max_value = max(enumerate(buckets), key=operator.itemgetter(1))
        buckets[max_index] = 0
        for i in range(max_value):
            buckets[(max_index + i + 1) % len(buckets)] += 1
        yield buckets


def find_loop(buckets):
    history = [list(buckets)]
    for i, new_bucket in enumerate(redistribute(buckets), start=1):
        if new_bucket in history:
            return i
        history.append(list(buckets))


with open('data/06.txt', 'r') as file:
    buckets = list(map(int, file.readline().split('\t')))
    print(f'Part one: {find_loop(buckets)}')
    print(f'Part two: {find_loop(buckets)}')
