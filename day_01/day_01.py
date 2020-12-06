with open('input.txt') as f:
    lines = f.readlines()

# Part 1
def get_fuel(module):
    return int(int(module) / 3) - 2
print(sum(get_fuel(line) for line in lines))

# Part 2
def get_total_fuel(module):
    fuel = get_fuel(module)
    if fuel < 1:
        return [0]
    else:
        return [fuel] + get_total_fuel(fuel)
print(sum(sum(get_total_fuel(line)) for line in lines))
