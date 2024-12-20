"""Solution for Day 20 - Race Condition"""

import os
import itertools
from aoc_tools.helpers import Point
from collections import defaultdict
from functools import cache

DIRECTIONS = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]


@cache
def point_map(dist: int) -> set[Point]:
    """Generate a set of points within the Manhattan distance constraints."""
    return {
        Point(i, j)
        for i, j in itertools.product(range(-dist, dist + 1), repeat=2)
        if 1 < abs(i) + abs(j) <= dist and not (abs(i) == 1 and abs(j) == 1)
    }


@cache
def parse_input(input_data: str) -> tuple[Point, Point, set[Point]]:
    """Parse the input data into start, end, and walls."""
    start, end = Point(0, 0), Point(0, 0)
    walls: set[Point] = set()
    for y, line in enumerate(input_data.splitlines()):
        for x, char in enumerate(line):
            point = Point(x, y)
            if char == "#":
                walls.add(point)
            elif char == "S":
                start = point
            elif char == "E":
                end = point
    return start, end, walls


def get_track(start: Point, end: Point, walls: set[Point]) -> dict[Point, int]:
    """Determine the shortest path track from start to end avoiding walls."""
    track = {start: 0}
    queue = [start]

    while queue:
        current = queue.pop(0)
        current_dist = track[current]
        for direction in DIRECTIONS:
            next_point = current.add(direction)
            if next_point not in walls and next_point not in track:
                track[next_point] = current_dist + 1
                queue.append(next_point)
                if next_point == end:
                    return track
    return track


def find_cheats(
    step: int, track: dict[Point, int], max_cheat_len: int, target: int
) -> dict[int, int]:
    """Find possible cheats and their frequency."""
    cheats: dict[int, int] = defaultdict(int)
    pos = list(track.keys())[step]
    for move in point_map(max_cheat_len):
        new_pos = pos.add(move)
        if new_pos in track:
            dist = pos.dist(new_pos)
            saving = track[new_pos] - track[pos] - dist
            if saving >= target:
                cheats[saving] += 1
    return cheats


def solve(input_data: str, max_cheat_len: int, target: int) -> int:
    """Generalized solution function for both parts."""
    start, end, walls = parse_input(input_data)
    track = get_track(start, end, walls)
    cheats: dict[int, int] = defaultdict(int)

    for i in range(len(track) - target):
        point_cheats = find_cheats(i, track, max_cheat_len, target)
        for saving, num in point_cheats.items():
            cheats[saving] += num

    return sum(num for saving, num in cheats.items() if saving >= target)


def part_one(input_data: str) -> int:
    """Solve Part One."""
    return solve(
        input_data,
        max_cheat_len=2,
        target=20 if len(input_data.splitlines()) < 20 else 100,
    )


def part_two(input_data: str) -> int:
    """Solve Part Two."""
    return solve(
        input_data,
        max_cheat_len=20,
        target=50 if len(input_data.splitlines()) < 20 else 100,
    )


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()

    print("Solution for Day 20 - Race Condition")
    print(f"Part One: {part_one(input_data)}")
    print(f"Part Two: {part_two(input_data)}")
