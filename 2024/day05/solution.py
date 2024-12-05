"""Solution for Day 5 - Print Queue"""

import os
from collections import defaultdict


def process_input(input_data: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    """
    Process the input data into a tuple of two items: rules and updates.

    Rules is a dictionary where the keys are the numbers from the first part of the
    input and the values are sets of numbers from the second part of the input.

    Updates is a list of lists of numbers from the second part of the input.

    The function processes the input data by iterating over the lines. If the line is
    empty, it sets a flag to indicate that it is processing the second part of the
    input. If the flag is set, it appends the line to the updates list. Otherwise, it
    splits the line into two parts and adds the second part as a value to the rules
    dictionary with the first part as the key.
    """
    lines = input_data.splitlines()
    second_part = False
    rules: dict[int, set[int]] = defaultdict(set)
    updates: list[list[int]] = []
    for line in lines:
        if line == "":
            second_part = True
            continue
        if second_part:
            updates.append(list(map(int, line.split(","))))
        else:
            a, b = map(int, line.split("|"))
            rules[a].add(b)
    return rules, updates


def check_update(update: list[int], rules: dict[int, set[int]]) -> int:
    """
    Check if the given list of integers satisfies the rules, and return its middle
    element if it does. Otherwise, return 0.

    Args:
        update (list[int]): The list of integers to be checked.
        rules (dict[int, set[int]]): A dictionary mapping each integer to a set
            of integers it can follow.

    Returns:
        int: The middle element of the given list if it satisfies the rules,
        otherwise 0.
    """
    return (
        0
        if any(update[i - 1] in rules[update[i]] for i in range(1, len(update)))
        else update[len(update) // 2]
    )


def fix_update(update: list[int], rules: dict[int, set[int]]) -> int:
    """
    Adjust the given update list according to the rules until no more swaps
    can be made, and return the middle element if any changes were made.

    Args:
        update (list[int]): The list of integers to be adjusted.
        rules (dict[int, set[int]]): A dictionary mapping each integer to a
            set of integers it can follow.

    Returns:
        int: The middle element of the adjusted list if any changes were
        made, otherwise 0.
    """
    swapped = True
    any_changes = False
    while swapped:
        swapped = False
        for i in range(1, len(update)):
            try:
                if update[i - 1] in rules[update[i]]:
                    update[i], update[i - 1] = update[i - 1], update[i]
                    swapped = True
            except KeyError:
                pass
        if swapped:
            any_changes = True
    return update[len(update) // 2] if any_changes else 0


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    rules, updates = process_input(input_data)
    return sum(check_update(update, rules) for update in updates)


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    rules, updates = process_input(input_data)
    return sum(fix_update(update, rules) for update in updates)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 5 - Print Queue")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
