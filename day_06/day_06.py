import re
from pathlib import Path

class Object:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def __repr__(self):
        string = (
            f'{self.name} ('
            f'parent: {self.parent.name if self.parent is not None else None}'
            f', children: {[c.name for c in self.children]})'
        )
        return string

    def get_num_orbits(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.get_num_orbits() + 1

    def get_parents(self):
        if self.parent is None:
            return []
        else:
            return [self.parent] + self.parent.get_parents()

def get_planets(text):
    planets = {}
    for parent_name, child_name in re.findall(r'(\w+)\)(\w+)', text):
        if parent_name in planets:
            parent = planets[parent_name]
        else:
            parent = Object(parent_name)
            planets[parent_name] = parent
        if child_name in planets:
            child = planets[child_name]
        else:
            child = Object(child_name)
            planets[child_name] = child
        parent.children.append(child)
        child.parent = parent
    return planets


def get_num_orbits(planets):
    return sum(planet.get_num_orbits() for planet in planets.values())


def get_distance(a, b):
    parents_a = a.parent.get_parents()
    parents_b = b.parent.get_parents()
    for parent in parents_a:
        if parent in parents_b:
            return parents_a.index(parent) + parents_b.index(parent) + 2

text = Path('input.txt').read_text()

# text = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L"""

# text = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

planets = get_planets(text)

# Part 1
print(get_num_orbits(planets))

# Part 2
print(get_distance(planets['YOU'], planets['SAN']))
