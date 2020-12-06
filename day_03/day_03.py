def get_coords(path):
    instructions = path.split(',')
    coords = [(0, 0)]
    for instruction in instructions:
        num_steps = int(instruction[1:])
        direction = instruction[0]
        for step in range(num_steps):
            x0, y0 = coords[-1]
            if direction == 'R':
                x = x0 + 1
                y = y0
            elif direction == 'U':
                x = x0
                y = y0 + 1
            elif direction == 'L':
                x = x0 - 1
                y = y0
            elif direction == 'D':
                x = x0
                y = y0 - 1
            coords.append((x, y))
    return coords[1:]


def get_intersections(coords_a, coords_b):
    return set(coords_a).intersection(coords_b)


def get_min_distance(intersections):
    return min(abs(a) + abs(b) for (a, b) in intersections)


def get_min_delay(coords_a, coords_b, intersections):
    num_steps = []
    for intersection in intersections:
        steps_a = coords_a.index(intersection) + 1  # add initial
        steps_b = coords_b.index(intersection) + 1  # add initial
        num_steps.append(steps_a + steps_b)
    return min(num_steps)

# path_a = 'R8,U5,L5,D3'
# path_b = 'U7,R6,D4,L4'

# path_a = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# path_b = 'U62,R66,U55,R34,D71,R55,D58,R83'

with open('input.txt') as f:
    path_a, path_b = f.read().splitlines()

coords_a = get_coords(path_a)
coords_b = get_coords(path_b)
intersections = get_intersections(coords_a, coords_b)

# Part 1
print(get_min_distance(intersections))

# Part 2
print(get_min_delay(coords_a, coords_b, intersections))
