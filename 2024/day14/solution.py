"""Solution for Day 14 - Restroom Redoubt"""

import os
import re

from collections import defaultdict
from dataclasses import dataclass
from math import prod


@dataclass
class Robot:
    p: tuple[int, int]  # Position
    v: tuple[int, int]  # Velocity


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    robots: dict[tuple[int, int], int] = defaultdict(int)
    max_x, max_y = 0, 0
    n_iters = 100
    for line in lines:
        x, y, v_x, v_y = map(
            int,
            re.findall(
                r"-?\d+",  # Matches integers, including negative numbers
                line,
            ),
        )
        r_x = x + n_iters * v_x
        r_y = y + n_iters * v_y
        robots[(r_x, r_y)] += 1
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    contained_robots: dict[tuple[int, int], int] = defaultdict(int)
    for pos, num in robots.items():
        contained_robots[(pos[0] % (max_x + 1), pos[1] % (max_y + 1))] += num

    quads = [0, 0, 0, 0]
    for pos, num in contained_robots.items():
        if pos[0] == max_x / 2 or pos[1] == max_y / 2:
            continue
        quad = 0
        if pos[0] > max_x / 2:
            quad += 1
        if pos[1] > max_y / 2:
            quad += 2
        quads[quad] += num

    return prod(quads)


def check_for_unique(
    robots: dict[tuple[int, int], tuple[int, int]],
    max_x: int,
    max_y: int,
    iteration: int,
) -> bool:
    contained_robots: dict[tuple[int, int], int] = defaultdict(bool)

    for (x, y), (v_x, v_y) in robots.items():
        r_x = (x + iteration * v_x) % (max_x + 1)
        r_y = (y + iteration * v_y) % (max_y + 1)
        if (r_x, r_y) in contained_robots:
            return False
        contained_robots[(r_x, r_y)] = True

    return True


def part_two(input_data: str) -> int:
    lines = input_data.splitlines()
    robots: dict[tuple[int, int], tuple[int, int]] = {}
    max_x, max_y = 0, 0
    for line in lines:
        x, y, v_x, v_y = map(
            int,
            re.findall(
                r"-?\d+",  # Matches integers, including negative numbers
                line,
            ),
        )
        robots[(x, y)] = (v_x, v_y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    iteration = 1
    while True:
        if not check_for_unique(robots, max_x, max_y, iteration):
            iteration += 1
            continue

        # Uncomment to print the tree
        # print(f"iter: {iteration}")
        # for j in range(max_y + 1):
        #     print(
        #         "".join(
        #             str(contained_robots[i, j]) if contained_robots[i, j] > 0 else "."
        #             for i in range(max_x + 1)
        #         )
        #     )

        break

    return iteration


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 14 - Restroom Redoubt")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
