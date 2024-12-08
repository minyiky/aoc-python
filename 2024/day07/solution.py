"""Solution for Day 7 - Bridge Repair"""

import os


def recursive_check_line_backwards(
    target: str,
    values: list[str],
    part_2: bool = False,
) -> bool:
    if not target:
        return False

    if len(values) == 1:
        return target == values[0]

    if (
        part_2
        and target.endswith(values[-1])
        and recursive_check_line_backwards(
            target[: -len(values[-1])], values[:-1], part_2=part_2
        )
    ):
        return True

    if int(target) % int(values[-1]) == 0 and recursive_check_line_backwards(
        str(int(target) // int(values[-1])), values[:-1], part_2=part_2
    ):
        return True

    return recursive_check_line_backwards(
        str(int(target) - int(values[-1])), values[:-1], part_2=part_2
    )


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    total = 0
    for line in lines:
        target, vals = line.split(": ")[0], line.split(": ")[1].split()
        if recursive_check_line_backwards(target, vals):
            total += int(target)
    return total


def part_two(input_data: str) -> int:
    lines = input_data.splitlines()
    total = 0
    for line in lines:
        target, vals = line.split(": ")[0], line.split(": ")[1].split()
        if recursive_check_line_backwards(target, vals, part_2=True):
            total += int(target)
    return total


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 7 - Bridge Repair")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
