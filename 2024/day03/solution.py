"""Solution for Day 3 - Mull It Over"""

import os
import re


def calc_muls(input_data: str) -> int:
    """Calculate the sum of products from multiplication operations in the input data.

    This function extracts pairs of numbers from the input string that are specified in
    the format 'mul(x, y)' and computes the sum of their products. It is designed to
    process a string containing multiple multiplication operations.

    Args:
        input_data (str): A string containing multiplication operations in the format 'mul(x, y)'.

    Returns:
        int: The total sum of the products of the extracted pairs of numbers.
    """
    return sum(
        int(match[1]) * int(match[0])
        for match in re.findall(r"mul\((\d+),(\d+)\)", input_data)
    )


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    return calc_muls(input_data)


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    input_data = "".join(input_data.splitlines())
    dont_regex = r"don't\(\).*?(do\(\)|$)"
    input_data = re.sub(dont_regex, "", input_data)
    return calc_muls(input_data)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 3 - Mull It Over")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
