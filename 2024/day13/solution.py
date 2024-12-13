"""Solution for Day 13 - Claw Contraption"""

import os
import re


def calc_matrix(
    x_a: int, x_b: int, x_t: int, y_a: int, y_b: int, y_t: int
) -> tuple[int, int, int]:
    a = x_t * y_b - y_t * x_b
    b = y_t * x_a - x_t * y_a

    det = x_a * y_b - x_b * y_a

    return a, b, det


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()

    total = 0

    for i in range(0, len(lines), 4):
        x_a, y_a = list(map(int, re.findall(r"[-+]?\d+", lines[i])))
        x_b, y_b = list(map(int, re.findall(r"[-+]?\d+", lines[i + 1])))
        x_t, y_t = list(map(int, re.findall(r"[-+]?\d+", lines[i + 2])))

        a, b, det = calc_matrix(x_a, x_b, x_t, y_a, y_b, y_t)

        if (
            a % det != 0
            or b % det != 0
            or (red_a := a // det) > 100
            or (red_b := b // det) > 100
        ):
            continue

        total += 3 * red_a + red_b

    return total


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()

    total = 0

    for i in range(0, len(lines), 4):
        x_a, y_a = list(map(int, re.findall(r"[-+]?\d+", lines[i])))
        x_b, y_b = list(map(int, re.findall(r"[-+]?\d+", lines[i + 1])))
        x_t, y_t = list(map(int, re.findall(r"[-+]?\d+", lines[i + 2])))

        x_t += 10000000000000
        y_t += 10000000000000

        a, b, det = calc_matrix(x_a, x_b, x_t, y_a, y_b, y_t)

        if a % det != 0 or b % det != 0:
            continue

        total += 3 * (a // det) + (b // det)

    return total


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 13 - Claw Contraption")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
