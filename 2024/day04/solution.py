"""Solution for Day 4 - Ceres Search"""

import os


def find_xmas(x: int, y: int, direction: tuple[int, int], lines: list[str]) -> bool:
    """
    Count the occurrences of the word "XMAS" in all possible directions
    from a starting point in a 2D grid of characters.

    Args:
        x (int): The x-coordinate of the starting point.
        y (int): The y-coordinate of the starting point.
        direction (tuple): The direction to search in (dx, dy).
        lines (list of str): The 2D grid of characters.

    Returns:
        bool: Whether the word "XMAS" can be found starting from (x, y)
        in the specified direction. Returns False if an IndexError occurs.
    """
    word = "XMAS"
    if not (
        0 <= y + direction[1] * 3 < len(lines)
        and (0 <= x + direction[0] * 3 < len(lines[0]))
    ):
        return False
    return all(
        lines[y + direction[1] * i][x + direction[0] * i] == word[i]
        for i in range(1, 4)
    )


def find_x_mas(x: int, y: int, lines: list[str]) -> bool:
    """
    Find the number of occasions where the word "MAS" occurs in an X shape
    in the given lines.

    Args:
        x (int): x-coordinate
        y (int): y-coordinate
        lines (str[]): 2D list of Characters

    Returns:
        int: The number of diagonals where "MAS" occurs
    """
    word = "MAS"

    diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    return any(
        all(
            lines[y + direction[1] * i][x + direction[0] * i] == word[i + 1]
            for i in [-1, 1]
        )
        for direction in diagonals[:2]
    ) and any(
        all(
            lines[y + direction[1] * i][x + direction[0] * i] == word[i + 1]
            for i in [-1, 1]
        )
        for direction in diagonals[2:]
    )


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    width = len(lines[0])
    height = len(lines)

    directions = [
        (1, 0),
        (1, 1),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
    ]

    return sum(
        lines[j][i] == "X" and find_xmas(i, j, direction, lines)
        for i in range(width)
        for j in range(height)
        for direction in directions
    )


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    width = len(lines[0])
    height = len(lines)
    return sum(
        lines[j][i] == "A" and find_x_mas(i, j, lines)
        for i in range(1, width - 1)
        for j in range(1, height - 1)
    )


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 4 - Ceres Search")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
