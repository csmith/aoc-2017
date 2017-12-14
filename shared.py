import functools
import itertools
import operator


def reverse_slice(input, start, length):
    """Reverses a slice of the input list, wrapping around if necessary."""
    output = list(input)
    for i, pos in enumerate(range(start, start + length)):
        output[pos % len(output)] = input[(start + length - i - 1) % len(output)]
    return output


def knot_hash_rounds(lengths, count=1):
    """Applies a number of rounds of the knot hash algorithm (see day 10)."""
    position, skip, data = 0, 0, list(range(256))
    for _ in range(count):
        for length in lengths:
            data = reverse_slice(data, position, length)
            position += length + skip
            skip += 1
    return data


def group(n, iterable):
    """Collates the iterable into groups n items long."""
    # https://docs.python.org/3.1/library/itertools.html#recipes
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def knot_hash(seed):
    """The knot has algorithm (day 10). Output is a hex string."""
    lengths = list(map(ord, seed.strip())) + [17, 31, 73, 47, 23]
    sparse_hash = knot_hash_rounds(lengths, 64)
    dense_hash = [functools.reduce(operator.xor, g) for g in group(16, sparse_hash)]
    return "".join(f"{c:02x}" for c in dense_hash)


def add_connected_components(sets, links, to_add=None):
    """
    Updates the given collection of sets to include a new group of connected components.

    Existing sets that overlap with the given `links` are removed and conjoined into a new superset along with the
    `to_add` items specified. If `to_add` is not specified then the `links` are added in their place.
    """
    overlapping = [s for s in sets if any(link in s for link in links)]
    for overlap in overlapping:
        sets.remove(overlap)
    sets.append(functools.reduce(set.union, overlapping, set(to_add if to_add is not None else links)))
