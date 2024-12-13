"""Solution for Day 12 - Garden Groups"""

import os

from functools import cache


@cache
def parse_grid(input_data: str) -> dict[tuple[int, int], str]:
    """Parse input data into a grid representation."""
    return {
        (i, j): char
        for j, line in enumerate(input_data.splitlines())
        for i, char in enumerate(line)
    }


def traverse_tree(
    point: tuple[int, int],
    char: str,
    grid: dict[tuple[int, int], str],
    seen: set[tuple[int, int]],
) -> tuple[int, set[tuple[tuple[int, int], tuple[int, int]]]]:
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    stack = [point]
    area = 0
    perimeter: set[tuple[tuple[int, int], tuple[int, int]]] = set()

    while stack:
        current = stack.pop()
        if current in seen:
            continue

        seen.add(current)
        area += 1

        for dx, dy in DIRECTIONS:
            next_point = (current[0] + dx, current[1] + dy)
            if next_point in grid and grid[next_point] == char:
                if next_point not in seen:
                    stack.append(next_point)
            else:
                perimeter.add((next_point, (dx, dy)))

    return area, perimeter


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    grid = parse_grid(input_data)

    total = 0
    seen: set[tuple[int, int]] = set()

    for point, char in grid.items():
        if point in seen:
            continue
        empty_seen: set[tuple[int, int]] = set()
        area, perimeter = traverse_tree(point, char, grid, empty_seen)
        seen = seen.union(empty_seen)
        total += area * len(perimeter)

    return total


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    grid = parse_grid(input_data)

    total = 0
    seen: set[tuple[int, int]] = set()

    for point, char in grid.items():
        if point in seen:
            continue
        empty_seen: set[tuple[int, int]] = set()
        area, perimeter_points = traverse_tree(point, char, grid, empty_seen)
        seen = seen.union(empty_seen)

        perimeter: int = 0

        for point, dir in perimeter_points:
            new_point = (
                (point[0] + 1, point[1]) if dir[0] == 0 else (point[0], point[1] + 1)
            )
            if (new_point, dir) not in perimeter_points:
                perimeter += 1

        total += area * perimeter

    return total


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 12 - Garden Groups")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
