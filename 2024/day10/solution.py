"""Solution for Day 10 - Hoof It"""

import os
from collections import defaultdict


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    loc_map: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(
        set[tuple[int, int]], set({})
    )
    grid: dict[tuple[int, int], int] = defaultdict(int)

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            try:
                grid[(i, j)] = int(char)
            except ValueError:
                pass
            if char == "0":
                loc_map[(i, j)].add((i, j))

    directions = ([1, 0], [-1, 0], [0, 1], [0, -1])

    for i in range(1, 10):
        new_map: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(
            set[tuple[int, int]], set({})
        )

        for point, values in loc_map.items():

            for direction in directions:
                new_point = (point[0] + direction[0], point[1] + direction[1])
                if grid[new_point] == i:
                    new_map[new_point] = new_map[new_point].union(values)

        loc_map = new_map

    return sum(len(v) for v in loc_map.values())


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    loc_map: dict[tuple[int, int], int] = defaultdict(int)
    grid: dict[tuple[int, int], int] = defaultdict(int)

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            try:
                grid[(i, j)] = int(char)
            except ValueError:
                pass
            if char == "0":
                loc_map[(i, j)] += 1

    directions = ([1, 0], [-1, 0], [0, 1], [0, -1])

    for i in range(1, 10):
        new_map: dict[tuple[int, int], int] = defaultdict(int)

        for point, values in loc_map.items():

            for direction in directions:
                new_point = (point[0] + direction[0], point[1] + direction[1])
                if grid[new_point] == i:
                    new_map[new_point] += values

        loc_map = new_map

    return sum(loc_map.values())


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 10 - Hoof It")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
