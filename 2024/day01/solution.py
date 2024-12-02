"""Solution for Day 1 - Historian Hysteria"""

import os
from collections import Counter


def parse_input(input_data: str) -> tuple[list[int], list[int]]:
    """Parse input into separate left and right lists of integers."""
    left, right = zip(*(map(int, line.split()) for line in input_data.splitlines()))
    return list(left), list(right)


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    left, right = parse_input(input_data)
    return sum(abs(r - l) for l, r in zip(sorted(left), sorted(right)))


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    left, right = parse_input(input_data)
    right_counter = Counter(right)
    return sum(l * right_counter[l] for l in left)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 1 - Historian Hysteria")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
