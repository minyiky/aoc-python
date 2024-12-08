"""Solution for Day 8 - Resonant Collinearity"""

import os


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    max_x, max_y = len(lines[0]), len(lines)
    locations: dict[str, list[tuple[int, int]]] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ".":
                continue
            if char not in locations:
                locations[char] = []
            locations[char].append((x, y))
    anti_nodes: set[tuple[int, int]] = set({})
    for coords in locations.values():
        if len(coords) == 1:
            continue
        for coord in coords:
            for other_coord in coords:
                if coord == other_coord:
                    continue
                x1, y1 = coord
                x2, y2 = other_coord
                anti_node = (x1 + 2 * (x2 - x1), y1 + 2 * (y2 - y1))
                if 0 <= anti_node[0] < max_x and 0 <= anti_node[1] < max_y:
                    anti_nodes.add(anti_node)
    return len(anti_nodes)


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    max_x, max_y = len(lines[0]), len(lines)
    locations: dict[str, list[tuple[int, int]]] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ".":
                continue
            if char not in locations:
                locations[char] = []
            locations[char].append((x, y))
    anti_nodes: set[tuple[int, int]] = set({})
    for coords in locations.values():
        for coord in coords:
            for other_coord in coords:
                if coord == other_coord:
                    continue
                x1, y1 = coord
                x2, y2 = other_coord
                diff = (x2 - x1, y2 - y1)
                anti_node = coord
                while 0 <= anti_node[0] < max_x and 0 <= anti_node[1] < max_y:
                    anti_nodes.add(anti_node)
                    anti_node = (anti_node[0] + diff[0], anti_node[1] + diff[1])
                anti_node = coord
                while 0 <= anti_node[0] < max_x and 0 <= anti_node[1] < max_y:
                    anti_nodes.add(anti_node)
                    anti_node = (anti_node[0] - diff[0], anti_node[1] - diff[1])
    return len(anti_nodes)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 8 - Resonant Collinearity")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
