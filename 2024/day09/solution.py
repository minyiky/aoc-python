"""Solution for Day 9 - Disk Fragmenter"""

import math
import os
from collections import defaultdict
from bisect import insort


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    input_data = input_data.strip()
    files: list[int] = []
    try:
        for i in range(0, len(input_data), 2):
            files += [i // 2] * int(input_data[i])
            files += [-1] * int(input_data[i + 1])
    except IndexError:
        pass

    i = 0
    total = 0
    while i < len(files):
        try:
            if files[i] == -1:
                while (v := files.pop()) == -1:
                    pass
                files[i] = v
            total += files[i] * i
        except IndexError:
            pass
        i += 1
    return total


def state(blocks: dict[int, int], empties: dict[int, dict[int, int]]):
    final_state: list[int] = []
    for i in range(max(list(blocks.keys())[-1], sorted(list(empties.keys()))[-1]) + 1):
        if i in blocks:
            for _ in range(blocks[i]):
                final_state += [i // 2]
        elif i in empties:
            for key, value in empties[i].items():
                if key == -1:
                    continue
                final_state += [key] * value
            final_state += [-1] * empties[i][-1]
    return final_state


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    input_data = input_data.strip()
    blocks: dict[int, int] = {}
    empties: dict[int, dict[int, int]] = {}
    gaps: dict[int, list[int]] = defaultdict(list[int])
    try:
        for i in range(0, len(input_data), 2):
            blocks[i] = int(input_data[i])
            empties[i + 1] = {-1: int(input_data[i + 1])}
            gaps[int(input_data[i + 1])].append(i + 1)
    except IndexError:
        pass

    # print(blocks)
    # print(empties)

    keys = list(blocks.keys())
    to_big_to_fit = math.inf
    for key in keys[::-1]:
        # print(gaps)
        # state(blocks, empties)
        if blocks[key] >= to_big_to_fit:
            continue

        possible_gaps: list[int] = []
        for gap, values in gaps.items():
            if gap >= blocks[key] and len(values) > 0:
                possible_gaps.append(values[0])

        if not possible_gaps:
            to_big_to_fit = blocks[key]
            continue

        slot = min(possible_gaps)

        if slot > key:
            to_big_to_fit = blocks[key]
            continue

        size = empties[slot][-1]

        empties[slot][key // 2] = blocks[key]
        empties[slot][-1] -= blocks[key]
        empties[key] = {-1: blocks[key]}
        del blocks[key]

        insort(gaps[empties[slot][-1]], slot)
        gaps[size] = gaps[size][1:]

    final_state: list[int] = state(blocks, empties)
    return sum(i * v if v != -1 else 0 for i, v in enumerate(final_state))


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 9 - Disk Fragmenter")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
