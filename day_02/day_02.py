from operator import add, mul
from itertools import combinations

OPS = {1: add, 2: mul, 99: None}

def run(program, noun, verb):
    program = program[:]  # copy
    program[1] = noun
    program[2] = verb
    idx = 0
    while True:
        op = OPS[program[idx]]
        if op is None:
            break
        idx_a, idx_b = program[idx + 1 : idx + 3]
        a = program[idx_a]
        b = program[idx_b]
        dst = program[idx + 3]
        program[dst] = op(a, b)
        idx += 4
    return program[0]

with open('input.txt') as f:
    program = [int(n) for n in f.read().strip().split(',')]

# Part 1
print(run(program, 12, 2))

# Part 2
for noun, verb in combinations(range(100), 2):
    if run(program, noun, verb) == 19690720:
        break
print(100 * noun + verb)
