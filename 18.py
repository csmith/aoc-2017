import operator
from collections import defaultdict


def get_value(registers, operand):
    return registers[operand] if operand in registers else int(operand)


def handle_generic(op):
    def inner(pc, registers, _, args):
        registers[args[0]] = op(registers[args[0]], get_value(registers, args[1]))
        return pc + 1
    return inner


def handle_snd(pc, registers, state, args):
    state['snd'].append(get_value(registers, args[0]))
    state['sndc'] += 1
    return pc + 1


def handle_jgz(pc, registers, _, args):
    return pc + get_value(registers, args[1]) if get_value(registers, args[0]) > 0 else pc + 1


def handle_rcv_p1(pc, registers, state, args):
    if get_value(registers, args[0]) != 0:
        state['rcv'].append(state['snd'][-1])
    return pc + 1


def handle_rcv_p2(pc, registers, state, args):
    if len(state['rcv']) > 0:
        registers[args[0]] = state['rcv'].pop(0)
        return pc + 1
    else:
        return pc


def get_ops(part_one=True):
    return {
        'snd': handle_snd,
        'set': handle_generic(lambda _, v: v),
        'add': handle_generic(operator.add),
        'mul': handle_generic(operator.mul),
        'mod': handle_generic(operator.mod),
        'jgz': handle_jgz,
        'rcv': handle_rcv_p1 if part_one else handle_rcv_p2
    }


def new_program(snd, rcv):
    return {'pc': 0, 'snd': snd, 'sndc': 0, 'rcv': rcv, 'terminated': False, 'waiting': False, 'regs': defaultdict(lambda: 0)}


def process_p1(instructions):
    program = new_program([], [])
    ops = get_ops(True)
    while len(program['rcv']) == 0:
        ins = instructions[program['pc']]
        program['pc'] = ops[ins[0]](program['pc'], program['regs'], program, ins[1:])
    return program['rcv'][0]


def can_execute(programs):
    return any(not p['terminated'] and (not p['waiting'] or len(p['rcv']) > 0) for p in programs)


def process_p2(instructions):
    p1_to_p2, p2_to_p1 = [], []
    programs = [new_program(p1_to_p2, p2_to_p1), new_program(p2_to_p1, p1_to_p2)]
    programs[1]['regs']['p'] = 1

    ops = get_ops(False)
    p = 0
    while can_execute(programs):
        for _ in range(1000):
            pc = programs[p]['pc']
            programs[p]['waiting'] = False

            if pc < 0 or pc >= len(instructions):
                programs[p]['terminated'] = True
                break

            ins = instructions[pc]
            programs[p]['pc'] = ops[ins[0]](pc, programs[p]['regs'], programs[p], ins[1:])

            if programs[p]['pc'] == pc:
                programs[p]['waiting'] = True
                break

        p = 1 - p

    return programs[1]['sndc']


with open('data/18.txt', 'r') as file:
    input = list(map(str.split, file.readlines()))
    print(f'Part one: {process_p1(input)}')
    print(f'Part two: {process_p2(input)}')