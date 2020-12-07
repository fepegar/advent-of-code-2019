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


class IntComputer:
    def __init__(self, program):
        self.program = program[:]
        self.idx = 0

    def run(self, inputs=None):
        outputs = []
        if inputs is None:
            import sys
            inputs = [int(n) for n in sys.argv[1:]]
        else:
            try:
                iter(inputs)
            except TypeError:
                inputs = [inputs]
        idx = 0
        while True:
            instruction = self.program[idx]
            op = get_op(instruction)
            if op == 99:
                return outputs
            num_params = num_params_dict[op]
            params = self.program[idx + 1: idx + 1 + num_params]
            mode_a, mode_b = get_modes(instruction)
            if op == INPUT:
                result_idx = self.program[idx + 1]
                self.program[result_idx] = inputs.pop(0)
                idx += 2
            elif op == OUTPUT:
                param = params[0]
                output = param if mode_a == IMMEDIATE else self.program[param]
                outputs.append(output)
                idx += 2
            else:
                num_params = num_params_dict[op]
                params = self.program[idx + 1: idx + 1 + num_params]
                param_a, param_b = params[:2]
                a = param_a if mode_a == IMMEDIATE else self.program[param_a]
                b = param_b if mode_b == IMMEDIATE else self.program[param_b]
                if op in (JUMP_TRUE, JUMP_FALSE):
                    if a and op == JUMP_TRUE:
                        idx = b
                    elif (not a) and op == JUMP_FALSE:
                        idx = b
                    else:
                        idx += 3
                else:
                    result_idx = params[2]
                    if op == ADD:
                        result = a + b
                    elif op == MULT:
                        result = a * b
                    elif op == LESS_THAN:
                        result = int(a < b)
                    elif op == EQUAL:
                        result = int(a == b)
                    self.program[result_idx] = result
                    idx += 4
