ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
POSITION = 0
IMMEDIATE = 1

def run(program, program_input):
    program = program[:]
    idx = 0
    while True:
        instruction = program[idx]
        string = f'{instruction:05d}'
        op = int(string[-2:])
        if op == 99:
            return
        modes_string = string[2::-1]
        mode_a, mode_b = [int(n) for n in modes_string][:2]
        if op in (ADD, MULT):
            param_a = program[idx + 1]
            param_b = program[idx + 2]
            a = param_a if mode_a == IMMEDIATE else program[param_a]
            b = param_b if mode_b == IMMEDIATE else program[param_b]
            result = a + b if op == ADD else a * b
            result_idx = program[idx + 3]
            program[result_idx] = result
            step = 4
        elif op == INPUT:
            result_idx = program[idx + 1]
            program[result_idx] = program_input  # int(input('Input instruction: '))
            step = 2
        elif op == OUTPUT:
            result_idx = program[idx + 1]
            output = program[result_idx]
            print(output)
            step = 2
        idx += step

with open('input.txt') as f:
    program = [int(n) for n in f.read().strip().split(',')]

run(program, 1)
