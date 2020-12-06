import re
from pathlib import Path

class Object:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def get_num_orbits(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.get_num_orbits() + 1

def get_num_orbits(text):
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
    return sum(planet.get_num_orbits() for planet in planets.values())

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

# Part 1
print(get_num_orbits(text))
