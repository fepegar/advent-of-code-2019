ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUAL = 8

num_params_dict = {
    ADD: 3,
    MULT: 3,
    INPUT: 1,
    OUTPUT: 1,
    JUMP_TRUE: 2,
    JUMP_FALSE: 2,
    LESS_THAN: 3,
    EQUAL: 3,
}

POSITION = 0
IMMEDIATE = 1

def get_modes(instruction):
    string = f'{instruction:05d}'
    op = int(string[-2:])
    if op == 99:
        return
    modes_string = string[2::-1]
    mode_a, mode_b = [int(n) for n in modes_string][:2]
    return mode_a, mode_b

def get_op(instruction):
    string = f'{instruction:05d}'
    return int(string[-2:])

def run(program, program_input):
    program = program[:]
    idx = 0
    while True:
        instruction = program[idx]
        op = get_op(instruction)
        if op == 99:
            return
        mode_a, mode_b = get_modes(instruction)
        num_params = num_params_dict[op]
        params = program[idx + 1: idx + 1 + num_params]
        if op in (INPUT, OUTPUT):
            result_idx = program[idx + 1]
            if op == INPUT:
                program[result_idx] = program_input
            else:
                output = program[result_idx]
                print(output)
            idx += 2
        else:
            mode_a, mode_b = get_modes(instruction)
            num_params = num_params_dict[op]
            params = program[idx + 1: idx + 1 + num_params]
            param_a, param_b = params[:2]
            a = param_a if mode_a == IMMEDIATE else program[param_a]
            b = param_b if mode_b == IMMEDIATE else program[param_b]
            if op in (JUMP_TRUE, JUMP_FALSE):
                if a and JUMP_TRUE:
                    idx = b
                if not a and JUMP_FALSE:
                    idx = b
            else:
                result_idx = params[2]
                if op == ADD:
                    result = a + b
                elif op == MULT:
                    result = a * b
                elif op == LESS_THAN:
                    result = a < b
                elif op == EQUAL:
                    result = a == b
                program[result_idx] = result
                idx += 4

with open('input.txt') as f:
    program = [int(n) for n in f.read().strip().split(',')]

run(program, 1)
