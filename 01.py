with open('data/01.txt', 'r') as file:
    captcha = file.readline().strip() * 2
    length = len(captcha) // 2
    print('Part one: %s' % sum(int(captcha[i]) for i in range(length) if captcha[i] == captcha[i+1]))
    print('Part two: %s' % sum(int(captcha[i]) for i in range(length) if captcha[i] == captcha[i + length // 2]))

# Alternatively...
import numpy as np
with open('data/01.txt', 'r') as file:
    captcha = list(file.readline().strip())
for part, roll in enumerate([1, len(captcha)//2]):
    print('Part %s: %s' % (part + 1, sum(int(i) for i, j in zip(captcha, np.roll(captcha, roll)) if i == j)))
