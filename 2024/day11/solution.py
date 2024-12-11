"""Solution for Day 11 - Plutonian Pebbles"""

import os
import math

from functools import lru_cache


@lru_cache(None)
def blink_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    if ((num_len := math.floor(math.log10(stone))) + 1) % 2 == 0:
        return [stone // 10 ** ((num_len // 2) + 1), stone % 10 ** ((num_len // 2) + 1)]

    return [stone * 2024]


@lru_cache(None)
def blink_stones(stone: int, num_left: int = 25) -> int:
    if num_left == 0:
        return 1
    return sum(blink_stones(stone, num_left - 1) for stone in blink_stone(stone))


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    input_data = input_data.strip()
    stones: list[int] = list(map(int, input_data.split()))
    return sum(blink_stones(stone, 25) for stone in stones)


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    input_data = input_data.strip()
    stones: list[int] = list(map(int, input_data.split()))
    return sum(blink_stones(stone, 75) for stone in stones)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 11 - Plutonian Pebbles")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
