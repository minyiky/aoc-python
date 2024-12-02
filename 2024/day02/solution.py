"""Solution for Day 2 - Red-Nosed Reports"""

import os


def check_line(vals: list[int], allow_retry: bool = False) -> bool:
    max_dif, min_dif = 0, 0
    for i in range(len(vals) - 1):
        curr, prev = vals[i + 1], vals[i]
        if max_dif == 0 and min_dif == 0:
            min_dif, max_dif = (1, 3) if curr > prev else (-3, -1)

        diff = curr - prev
        if not (min_dif <= diff <= max_dif):
            if allow_retry:
                return any(
                    check_line(vals[:j] + vals[j + 1 :], False)
                    for j in range(min(i - 1, 0), max(i + 1, len(vals)))
                )
            return False
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
    print("Solution for Day {day} - {title}")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
