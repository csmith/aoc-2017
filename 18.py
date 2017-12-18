from collections import defaultdict

get_value = lambda registers, operand: registers[operand] if operand in registers else int(operand)

def handle_snd(pc, registers, state, args):
    state['snd'].append(get_value(registers, args[0]))
    state['sndc'] += 1
    return pc + 1

def handle_set(pc, registers, state, args):
    registers[args[0]] = get_value(registers, args[1])
    return pc + 1

def handle_add(pc, registers, state, args):
    registers[args[0]] += get_value(registers, args[1])
    return pc + 1

def handle_mul(pc, registers, state, args):
    registers[args[0]] *= get_value(registers, args[1])
    return pc + 1

def handle_mod(pc, registers, state, args):
    registers[args[0]] %= get_value(registers, args[1])
    return pc + 1

def handle_jgz(pc, registers, state, args):
    return pc + get_value(registers, args[1]) if get_value(registers, args[0]) > 0 else pc + 1

def handle_rcv_p1(pc, registers, state, args):
    if get_value(registers, args[0]) != 0:
        state['recovered'].append(state['snd'][-1])
    return pc + 1

def handle_rcv_p2(pc, registers, state, args):
    if len(state['rcv']) > 0:
        registers[args[0]] = state['rcv'].pop(0)
        return pc + 1
    else:
        return pc

def process_p1(instructions):
    pc, state, registers = 0, {'snd': [], 'sndc': 0, 'recovered': []}, defaultdict(lambda: 0)
    ops = {
        'snd': handle_snd,
        'set': handle_set,
        'add': handle_add,
        'mul': handle_mul,
        'mod': handle_mod,
        'jgz': handle_jgz,
        'rcv': handle_rcv_p1,
    }
    while len(state['recovered']) == 0:
        ins = instructions[pc]
        pc = ops[ins[0]](pc, registers, state, ins[1:])
    return state['recovered'][0]


def can_execute(programs):
    for p in programs:
        if p['state']['terminated']:
            yield False
        elif p['state']['waiting'] and len(p['state']['rcv']) == 0:
            yield False
        else:
            yield True


def process_p2(instructions):
    p1_to_p2, p2_to_p1 = [], []
    programs = [{
        'pc': 0,
        'state': {'snd': p1_to_p2, 'sndc': 0, 'rcv': p2_to_p1, 'terminated': False, 'waiting': False},
        'regs': defaultdict(lambda: 0)
    }, {
        'pc': 0,
        'state': {'snd': p2_to_p1, 'sndc': 0, 'rcv': p1_to_p2, 'terminated': False, 'waiting': False},
        'regs': defaultdict(lambda: 0),
    }]
    programs[1]['regs']['p'] = 1

    ops = {
        'snd': handle_snd,
        'set': handle_set,
        'add': handle_add,
        'mul': handle_mul,
        'mod': handle_mod,
        'jgz': handle_jgz,
        'rcv': handle_rcv_p2,
    }

    p = 0
    while any(can_execute(programs)):
        for _ in range(1000):
            pc = programs[p]['pc']
            programs[p]['state']['waiting'] = False
            if pc < 0 or pc >= len(instructions):
                programs[p]['state']['terminated'] = True
                break
            ins = instructions[pc]
            programs[p]['pc'] = ops[ins[0]](pc, programs[p]['regs'], programs[p]['state'], ins[1:])
            if programs[p]['pc'] == pc:
                programs[p]['state']['waiting'] = True
                break
        p = 1 - p

    return programs[1]['state']['sndc']



with open('data/18.txt', 'r') as file:
    input = list(map(str.split, file.readlines()))
    print(f'Part one: {process_p1(input)}')
    print(f'Part two: {process_p2(input)}')