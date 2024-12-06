import os

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def find_start(lines: list[str]) -> tuple[int, int]:
    """Find the starting position marked with `^`."""
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == "^":
                return (i, j)
    raise KeyError("Start not found")


def visited(
    start: tuple[int, int],
    lines: list[str],
) -> set[tuple[int, int]]:
    """Track visited positions."""
    visited_set: set[tuple[tuple[int, int], tuple[int, int]]] = {(start, directions[0])}
    turns = 0
    direction = directions[turns % 4]
    pos = start

    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if not (0 <= next_pos[1] < len(lines) and 0 <= next_pos[0] < len(lines[0])):
            break

        if lines[next_pos[1]][next_pos[0]] == "#":
            turns += 1
            direction = directions[turns % 4]
            continue

        pos = next_pos
        if (pos, direction) in visited_set:
            raise ValueError("Infinite loop detected")

        visited_set.add((pos, direction))

    return {pos for pos, _ in visited_set}


def part_one(input_data: str) -> int:
    """Solve part one."""
    lines = input_data.splitlines()
    start = find_start(lines)
    return len(visited(start, lines))


def part_two(input_data: str) -> int:
    """Solve part two."""
    lines = input_data.splitlines()
    start = find_start(lines)
    possibles = visited(start, lines)
    count = 0

    for pos in possibles:
        if pos == start:
            continue

        new_lines = lines.copy()
        line = new_lines[pos[1]]
        new_lines[pos[1]] = f"{line[: pos[0]]}#{line[pos[0] + 1 :]}"

        try:
            visited(start, new_lines)
        except ValueError:
            count += 1

    return count


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()

    print("Solution for Day 6 - Guard Gallivant")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
