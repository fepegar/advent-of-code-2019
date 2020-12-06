pwd_min = 254032
pwd_max = 789860


def fix(n):
    inp = str(n)
    out = [inp[0]]
    for c in inp[1:]:
        if int(c) < int(out[-1]):
            out += (6 - len(out)) * out[-1]
            break
        else:
            out.append(c)
    return int(''.join(out))


def same_adjacent_old(n):
    string = str(n)
    for i, c in enumerate(string[1:], 1):
        if c == string[i - 1]:
            result = True
            break
    else:
        result = False
    return result


def same_adjacent(n, part):
    string = str(n)
    for c in set(string):
        count = string.count(c)
        ok_1 = part == 1 and count > 1
        ok_2 = part == 2 and count == 2
        if ok_1 or ok_2:
            result = True
            break
    else:
        result = False
    return result


num = fix(pwd_min)
num_valid_part_1 = num_valid_part_2 = 0
while num <= pwd_max:
    num_valid_part_1 += same_adjacent(num, 1)
    num_valid_part_2 += same_adjacent(num, 2)
    num += 1
    num = fix(num)
print(num_valid_part_1)
print(num_valid_part_2)
