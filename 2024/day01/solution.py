"""Solution for Day 1 - Historian Hysteria"""

import os

from collections import Counter

def separate_sides(input_data: str) -> tuple[list[int], list[int]]:
    lines = input_data.splitlines()
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return left, right

def part_one(input_data: str) -> int:
    """Implement part one logic"""
    left, right = separate_sides(input_data)
        
    left.sort()
    right.sort()
    return sum(abs(r - l) for l, r in zip(left, right))

def part_two(input_data: str) -> int:
    """Implement part two logic"""
    left, right = separate_sides(input_data)
    
    right_counter = Counter(right)
    
    return sum(l * right_counter[l] for l in left)

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 1 - Historian Hysteria")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
