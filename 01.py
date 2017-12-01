with open('data/01.txt', 'r') as file:
    captcha = file.readline().strip() * 2
    length = len(captcha) // 2
    print('Part one: %s' % sum(int(captcha[i]) for i in range(length) if captcha[i] == captcha[i+1]))
    print('Part two: %s' % sum(int(captcha[i]) for i in range(length) if captcha[i] == captcha[i + length // 2]))
