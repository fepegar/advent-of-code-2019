from int_computer import IntComputer

with open('input.txt') as f:
    program = [int(n) for n in f.read().strip().split(',')]

# Part 1
print(IntComputer(program).run(1))

# Part 2
is_8_pos = [3,9,8,9,10,9,4,9,99,-1,8]
assert IntComputer(is_8_pos).run(8)
assert not IntComputer(is_8_pos).run(7)
assert not IntComputer(is_8_pos).run(9)

lt_8_pos = [3,9,7,9,10,9,4,9,99,-1,8]
assert IntComputer(lt_8_pos).run(7)
assert not IntComputer(lt_8_pos).run(8)
assert not IntComputer(lt_8_pos).run(9)

is_8_imm = [3,3,1108,-1,8,3,4,3,99]
assert IntComputer(is_8_imm).run(8)
assert not IntComputer(is_8_imm).run(7)
assert not IntComputer(is_8_imm).run(9)

lt_8_imm = [3,3,1107,-1,8,3,4,3,99]
assert IntComputer(lt_8_imm).run(7)
assert not IntComputer(lt_8_imm).run(8)
assert not IntComputer(lt_8_imm).run(9)

is_nz_pos = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
assert IntComputer(is_nz_pos).run(1)
assert IntComputer(is_nz_pos).run(-1)
assert not IntComputer(is_nz_pos).run(0)

print(IntComputer(program).run(5))
