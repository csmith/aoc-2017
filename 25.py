import re
from collections import defaultdict

VALUE = 0
MOVE = 1
STATE = 2


def parse():
    begin_state = re.compile(r'Begin in state (.*?)\.')
    checksum_steps = re.compile(r'Perform a diagnostic checksum after ([0-9]+) steps\.')
    state_header = re.compile(r'In state (.*?):')
    value_header = re.compile(r'If the current value is ([01]):')
    value_action = re.compile(r'- Write the value ([01])\.')
    move_action = re.compile(r'- Move one slot to the (right|left)\.')
    state_action = re.compile(r'- Continue with state (.*?)\.')

    initial_state = checksum = None
    transitions = defaultdict(lambda: [[None]*3, [None]*3])
    cur_state = None
    cur_value = None

    with open('data/25.txt') as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue

            if initial_state is None:
                initial_state = begin_state.match(line).group(1)
            elif checksum is None:
                checksum = int(checksum_steps.match(line).group(1))
            elif cur_state is None:
                cur_state = state_header.match(line).group(1)
            elif cur_value is None:
                cur_value = int(value_header.match(line).group(1))
            elif transitions[cur_state][cur_value][VALUE] is None:
                transitions[cur_state][cur_value][VALUE] = int(value_action.match(line).group(1))
            elif transitions[cur_state][cur_value][MOVE] is None:
                transitions[cur_state][cur_value][MOVE] = move_action.match(line).group(1)
            elif transitions[cur_state][cur_value][STATE] is None:
                transitions[cur_state][cur_value][STATE] = state_action.match(line).group(1)
                if cur_value == 1:
                    cur_state = None
                cur_value = None

    return initial_state, checksum, dict(transitions)


def execute(state, rounds, transitions):
    tape = defaultdict(lambda: 0)
    head = 0
    for _ in range(rounds):
        instr = transitions[state][tape[head]]
        tape[head] = instr[VALUE]
        head += 1 if instr[MOVE] == 'right' else -1
        state = instr[STATE]

    return sum(v for v in tape.values() if v == 1)


state, target, transitions = parse()
print(execute(state, target, transitions))