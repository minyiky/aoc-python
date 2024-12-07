import os

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def generate_maps(
    lines: list[str],
) -> tuple[tuple[int, int], set[tuple[int, int]], set[tuple[int, int]]]:
    """
    Generate the initial map configuration from the input lines.

    This function processes a list of strings representing a grid, where each
    character in the string indicates either an empty space, a wall, or the
    starting position. It categorizes each position into walls, empty spaces,
    or the start position.

    Args:
        lines (list of str): The grid representation where each string is a row.

    Returns:
        tuple: A tuple containing the starting position as a tuple of integers
        (x, y), a set of tuples representing wall positions, and a set of tuples
        representing empty positions.
    """
    walls: set[tuple[int, int]] = set({})
    empties: set[tuple[int, int]] = set({})
    start = (0, 0)
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == "#":
                walls.add((i, j))
                continue
            elif char == "^":
                start = (i, j)
            empties.add((i, j))
    return start, walls, empties


def num_visited(
    start: tuple[int, int],
    walls: set[tuple[int, int]],
    empties: set[tuple[int, int]],
) -> int:
    """
    Find the number of visited positions.

    Given a starting position, a set of walls, and a set of empty spaces, find the
    number of positions that can be visited by walking in the given direction.

    Args:
        start (tuple[int, int]): The starting position.
        walls (set[tuple[int, int]]): The set of walls.
        empties (set[tuple[int, int]]): The set of empty spaces.

    Returns:
        int: The number of visited positions.
    """
    visited_set: set[tuple[int, int]] = {(start)}
    turns = 0
    direction = directions[turns % 4]
    pos = start

    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos in walls:
            turns += 1
            direction = directions[turns % 4]
            continue

        if next_pos not in empties:
            break

        pos = next_pos
        visited_set.add(pos)
    return len(visited_set)


def has_loop(
    start: tuple[int, int],
    turns: int,
    walls: set[tuple[int, int]],
    empties: set[tuple[int, int]],
) -> bool:
    """
    Check if a loop is formed.

    Given a starting position, a turn count, a set of walls, and a set of
    empty spaces, check if a loop is formed by walking in the given
    direction.

    Args:
        start (tuple[int, int]): The starting position.
        turns (int): The turn count.
        walls (set[tuple[int, int]]): The set of walls.
        empties (set[tuple[int, int]]): The set of empty spaces.

    Returns:
        bool: Whether a loop is formed.
    """
    visited_walls: set[tuple[tuple[int, int], tuple[int, int]]] = set({})
    direction = directions[turns % 4]
    pos = start

    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos in walls:
            if (next_pos, direction) in visited_walls:
                return True
            visited_walls.add((next_pos, direction))
            turns += 1
            direction = directions[turns % 4]
            continue

        if next_pos not in empties:
            break

        pos = next_pos

    return False


def num_loops(
    start: tuple[int, int],
    walls: set[tuple[int, int]],
    empties: set[tuple[int, int]],
) -> int:
    """
    Find the number of loops that can be formed by walking in the given direction
    from the starting position if obstacles were to be placed in the way.

    Args:
        start (tuple[int, int]): The starting position.
        walls (set[tuple[int, int]]): The set of walls.
        empties (set[tuple[int, int]]): The set of empty spaces.

    Returns:
        int: The number of loops that can be formed.
    """
    visited: set[tuple[int, int]] = {(start)}

    turns = 0
    direction = directions[turns % 4]
    pos = start

    count = 0

    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos in walls:
            turns += 1
            direction = directions[turns % 4]
            continue

        if next_pos not in empties:
            break

        if next_pos not in visited:
            new_walls = walls.copy()
            new_walls.add(next_pos)
            if has_loop(pos, turns, new_walls, empties):
                count += 1
        pos = next_pos
        visited.add(pos)
    return count


def part_one(input_data: str) -> int:
    """Solve part one."""
    lines = input_data.splitlines()
    start, walls, empties = generate_maps(lines)
    return num_visited(start, walls, empties)


def part_two(input_data: str) -> int:
    """Solve part two."""
    lines = input_data.splitlines()
    start, walls, empties = generate_maps(lines)
    return num_loops(start, walls, empties)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()

    print("Solution for Day 6 - Guard Gallivant")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
