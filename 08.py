import re
from collections import defaultdict
import operator

REGEX = r'^(?P<target>.*?) (?P<op>inc|dec) (?P<amount>.*?) if (?P<operand>.*?) (?P<comparator>.*?) (?P<value>.*?)(\s|$)'

comparators = {'>': operator.gt, '>=': operator.ge, '==': operator.eq, '!=': operator.ne, '<': operator.lt, '<=': operator.le}
operators = {'inc': 1, 'dec': -1}


def evaluate(instructions):
    registers = defaultdict(lambda: 0)
    for instruction in instructions:
        if comparators[instruction['comparator']](registers[instruction['operand']], int(instruction['value'])):
            registers[instruction['target']] += operators[instruction['op']] * int(instruction['amount'])
        yield dict(registers)


with open('data/08.txt', 'r') as file:
    instructions = [re.search(REGEX, line).groupdict() for line in file.readlines()]
    print(f'Part one: {max(list(evaluate(instructions))[-1].values())}')
    print(f'Part two: {max(max(regs.values()) for regs in evaluate(instructions))}')