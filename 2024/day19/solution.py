"""Solution for Day 19 - Linen Layout"""

import os

from functools import cache


def check_towels(stripes: list[str], towel: str) -> bool:
    if towel == "":
        return True
    return any(
        (
            check_towels(stripes, towel[len(stripe) :])
            if towel.startswith(stripe)
            else False
        )
        for stripe in stripes
    )


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    stripes = lines[0].split(", ")
    return sum(check_towels(stripes, towel) for towel in lines[2:])


@cache
def count_towels(stripes: tuple[str], towel: str) -> int:
    if not towel:
        return 1
    return sum(
        (count_towels(stripes, towel[len(stripe) :]) if towel.startswith(stripe) else 0)
        for stripe in stripes
    )


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    stripes = tuple(lines[0].split(", "))
    return sum(count_towels(stripes, towel) for towel in lines[2:])


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 19 - Linen Layout")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
