from itertools import permutations
from int_computer import IntComputer


class Amplifier:
    def __init__(self, program):
        self.computer = IntComputer(program)

    def get_output(self, phase, input_):
        return self.computer.run(program_inputs=[phase, input_])[-1]

def get_max_signal(program, part=1):
    if part == 1:
        range_phases = range(5)
    elif part == 2:
        range_phases = range(5, 10)
    signals = []
    for combination in permutations(range_phases, 5):
        amp_input = 0
        for phase in combination:
            amp_output = Amplifier(program).get_output(phase, amp_input)
            amp_input = amp_output
        signals.append(amp_output)
    return max(signals)

program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
assert get_max_signal(program) == 43210

program = [
    3,23,3,24,1002,24,10,24,1002,23,-1,23,
    101,5,23,23,1,24,23,23,4,23,99,0,0
]
assert get_max_signal(program) == 54321

program = [
    3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
    1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
]
assert get_max_signal(program) == 65210

with open('input.txt') as f:
    program = [int(n) for n in f.read().strip().split(',')]

# Part 1
print(get_max_signal(program))
