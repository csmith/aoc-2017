def part_one():
    # Part one: manually translated to Python
    mul, a, b, c, d, e, f, g, h = 0, 0, 84, 84, 0, 0, 0, 0 , 0                  # set b 84
                                                                                # set c b
    if a != 0:                                                                  # jnz a 2
                                                                                # jnz 1 5
        b *= 100
        mul += 1                                                                # mul b 100
        b += 100000                                                             # sub b -100000
        c = b                                                                   # set c b
        c += 17000                                                              # sub c -17000

    while True:
        f = 1                                                                   # set f 1
        d = 2                                                                   # set d 2
        while True:
            e = 2                                                               # set e 2
            while True:
                g = d                                                           # set g d
                g *= e
                mul += 1                                                        # mul g e
                g -= b                                                          # sub g b
                if g == 0:                                                      # jnz g 2
                    f = 0                                                       # set f 0
                e += 1                                                          # sub e -1
                g = e                                                           # set g e
                g -= b                                                          # sub g b
                if g == 0: break                                                # jnz g -8
            d += 1                                                              # sub d -1
            g = d                                                               # set g d
            g -= b                                                              # sub g b
            if g == 0: break                                                    # jnz g -13
        if f == 0:                                                              # jnz f 2
            h += 1                                                              # sub h -1
        g = b                                                                   # set g b
        g -= c                                                                  # sub g c
        if g == 0: break                                                        # jnz g 2
                                                                                # jnz 1 3
        b += 17                                                                 # sub b -17
                                                                                # jnz 1 -23
    return mul


def part_two():
    # Part two: manually optimised and a little golfed... Turns out it's counting non-primes in a certain range.
    return sum(1 for b in range(108400, 125401, 17) if any(b % d == 0 for d in range(2, int(b**0.5)+1)))

print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
