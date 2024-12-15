import os
from collections import defaultdict
from bisect import insort, bisect_left, bisect_right

# Directions for movement (up, right, down, left)
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def _find_next(d: int, target: int, walls: list[int]) -> int | None:
    """Find the next position before a wall in the given direction."""
    if d > 0:  # Moving down
        idx = bisect_right(walls, target)
        if idx < len(walls):
            return walls[idx] - 1
    else:  # Moving up
        idx = bisect_left(walls, target)
        if idx > 0:
            return walls[idx - 1] + 1
    return None


class WallMap:
    """Class to manage wall map and handle movements."""

    def __init__(self, lines: list[str]):
        self.x_locs: defaultdict[int, list[int]] = defaultdict(list)
        self.y_locs: defaultdict[int, list[int]] = defaultdict(list)

        self.max_x = len(lines[0])
        self.max_y = len(lines)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.x_locs[x].append(y)
                    self.y_locs[y].append(x)

        # Sort the positions of walls
        for values in self.x_locs.values():
            values.sort()
        for values in self.y_locs.values():
            values.sort()

        jumps: dict[tuple[int, int], dict[tuple[int, int], tuple[int, int]]] = (
            defaultdict(dict[tuple[int, int], tuple[int, int]])
        )

        for j in range(self.max_y):
            for i in range(self.max_x):
                for dx, dy in DIRECTIONS:
                    next_x = _find_next(dx, i, self.y_locs[j]) if dx != 0 else i
                    next_y = _find_next(dy, j, self.x_locs[i]) if dy != 0 else j

                    if next_x is None or next_y is None:
                        continue
                    jumps[(i, j)][(dx, dy)] = (next_x, next_y)

        self.jumps = jumps

    def add_wall(self, x: int, y: int):
        """Add a wall at the given position."""
        insort(self.x_locs[x], y)
        insort(self.y_locs[y], x)

    def next_space_before_wall(
        self, x: int, y: int, direction: tuple[int, int]
    ) -> tuple[int, int] | None:
        """Find the next space before a wall in the given direction."""
        dx, dy = direction
        if dx == 0:  # Vertical movement
            walls = self.x_locs[x]
            new_y = _find_next(dy, y, walls)
            return (x, new_y) if new_y is not None else None
        elif dy == 0:  # Horizontal movement
            walls = self.y_locs[y]
            new_x = _find_next(dx, x, walls)
            return (new_x, y) if new_x is not None else None
        return None

    def copy(self) -> "WallMap":
        """Create a copy of the current WallMap."""
        new_map = WallMap([""])
        new_map.x_locs = defaultdict(
            list, {key: value.copy() for key, value in self.x_locs.items()}
        )
        new_map.y_locs = defaultdict(
            list, {key: value.copy() for key, value in self.y_locs.items()}
        )
        return new_map


def generate_maps(
    lines: list[str],
) -> tuple[tuple[int, int], set[tuple[int, int]], set[tuple[int, int]]]:
    """Generate the map configuration from input lines."""
    walls: set[tuple[int, int]] = set()
    empties: set[tuple[int, int]] = set()
    start = (0, 0)

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == "#":
                walls.add((i, j))
            elif char == "^":
                start = (i, j)
            empties.add((i, j))

    return start, walls, empties


def num_visited_teleport(
    start: tuple[int, int], wall_map: WallMap, max_x: int, max_y: int
) -> int:
    """Find the number of distinct visited positions."""
    visited: set[tuple[int, int]] = {start}
    pos = start
    direction = DIRECTIONS[0]
    turns = 0

    while True:
        next_pos = wall_map.next_space_before_wall(pos[0], pos[1], direction)

        if not next_pos:
            while 0 <= pos[0] < max_x and 0 <= pos[1] < max_y:
                visited.add(pos)
                pos = (pos[0] + direction[0], pos[1] + direction[1])
            break

        while pos != next_pos:
            visited.add(pos)
            pos = (pos[0] + direction[0], pos[1] + direction[1])

        turns += 1
        direction = DIRECTIONS[turns % 4]

    return len(visited)


def has_loop_teleport(start: tuple[int, int], turns: int, wall_map: WallMap) -> bool:
    """Check if there is a loop during the teleportation."""
    visited_walls: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    pos = start
    direction = DIRECTIONS[turns % 4]

    while True:
        next_pos = wall_map.next_space_before_wall(pos[0], pos[1], direction)

        if not next_pos:
            return False

        state = (next_pos, direction)
        if state in visited_walls:
            return True

        visited_walls.add(state)
        pos = next_pos
        turns += 1
        direction = DIRECTIONS[turns % 4]


def num_loops_teleport(
    start: tuple[int, int],
    walls: set[tuple[int, int]],
    empties: set[tuple[int, int]],
    wall_map: WallMap,
) -> int:
    """Count the number of loops in the teleportation."""
    visited: set[tuple[int, int]] = {start}
    pos = start
    turns = 0
    count = 0
    direction = DIRECTIONS[turns % 4]

    while True:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos in walls:
            turns += 1
            direction = DIRECTIONS[turns % 4]
            continue

        if next_pos not in empties:
            break

        if next_pos not in visited:
            new_wall_map = wall_map.copy()
            new_wall_map.add_wall(next_pos[0], next_pos[1])

            if has_loop_teleport(pos, turns, new_wall_map):
                count += 1

        pos = next_pos
        visited.add(pos)

    return count


def part_one(input_data: str) -> int:
    """Solve part one."""
    lines = input_data.splitlines()
    start, _, _ = generate_maps(lines)
    wall_map = WallMap(lines)
    return num_visited_teleport(start, wall_map, len(lines[0]), len(lines))


def part_two(input_data: str) -> int:
    """Solve part two."""
    lines = input_data.splitlines()
    start, walls, empties = generate_maps(lines)
    wall_map = WallMap(lines)
    return num_loops_teleport(start, walls, empties, wall_map)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()

    print("Solution for Day 6 - Guard Gallivant")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
