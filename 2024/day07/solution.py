"""Solution for Day 7 - Bridge Repair"""

import os
import math
from functools import lru_cache

from typing import Callable


part_one_operations: list[Callable[[int, int], int]] = [
    lambda x, y: x + y,  # Addition
    lambda x, y: x * y,  # Multiplication
]


@lru_cache(maxsize=None)
def int_len(num: int):
    return 1 + math.floor(math.log10(num))


concatenation: Callable[[int, int], int] = lambda x, y: x * 10 ** (int_len(y)) + y

part_two_operations = part_one_operations + [concatenation]


def recursive_check_line(
    current: int,
    values: list[int],
    target: int,
    ops: list[Callable[[int, int], int]] = part_two_operations,
) -> int:
    if len(values) == 0:
        return target if current == target else 0
    if current > target:
        return 0
    return (
        target
        if any(
            target
            == recursive_check_line(op(current, values[0]), values[1:], target, ops)
            for op in ops
        )
        else 0
    )


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    total = 0
    for line in lines:
        target, other = line.split(": ")
        vals = list(map(int, other.split()))
        total += recursive_check_line(
            vals[0], vals[1:], int(target), part_one_operations
        )
    return total


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    total = 0
    for line in lines:
        target, other = line.split(": ")
        vals = list(map(int, other.split()))
        if sum(vals) > int(target):
            continue
        total += recursive_check_line(
            vals[0], vals[1:], int(target), part_two_operations
        )
    return total


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 7 - Bridge Repair")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
