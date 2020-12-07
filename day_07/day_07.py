from itertools import permutations
from int_computer import IntComputer


class Amplifier:
    def __init__(self, program):
        self.computer = IntComputer(program)

    def get_outputs(self, inputs):
        return self.computer.run(inputs=inputs)

def get_max_signal(program, part=1, num_amps=5):
    if part == 1:
        range_phases = range(num_amps)
    elif part == 2:
        range_phases = range(num_amps, 2 * num_amps)
    signals = []
    for combination in permutations(range_phases, num_amps):
        amp_input = 0
        amps = [Amplifier(program) for _ in range(num_amps)]
        found = False
        while not found:
            for amp, phase in zip(amps, combination):
                inputs = [phase, amp_input]
                amp_outputs = amp.get_outputs(inputs)
                if not amp_outputs:
                    found = True
                    break
                amp_input = amp_outputs[-1]
            if part == 1: break
        signals.append(amp_outputs[-1])
    return max(signals)


if __name__ == "__main__":
    with open('input.txt') as f:
        input_program = [int(n) for n in f.read().strip().split(',')]

    # Part 1
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

    print(get_max_signal(input_program))


    # Part 2
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    assert get_max_signal(program, part=2) == 139629729

    # print(get_max_signal(input_program, part=2))
