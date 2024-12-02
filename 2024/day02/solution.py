"""Solution for Day 2 - Red-Nosed Reports"""

import os


def check_line(vals: list[int], allow_retry: bool = False) -> bool:
    min_dif, max_dif = (1, 3) if vals[1] > vals[0] else (-3, -1)
    for i in range(len(vals) - 1):
        diff = vals[i + 1] - vals[i]
        if not (min_dif <= diff <= max_dif):
            return (
                any(
                    check_line(vals[:j] + vals[j + 1 :], False)
                    for j in range(i - 1, i + 1)
                )
                if allow_retry
                else False
            )
    return True


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    return sum(check_line(list(map(int, line.split()))) for line in lines)


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    return sum(
        check_line(list(map(int, line.split())), allow_retry=True) for line in lines
    )


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 2 - Red-Nosed Reports")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
