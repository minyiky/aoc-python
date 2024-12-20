"""Solution for Day 16 - Reindeer Maze"""

import os
import heapq

from collections import defaultdict
from functools import cache

from aoc_tools.helpers import Point

lr: dict[Point, tuple[Point, Point]] = {
    Point(0, 1): (Point(-1, 0), Point(1, 0)),
    Point(0, -1): (Point(-1, 0), Point(1, 0)),
    Point(1, 0): (Point(0, -1), Point(0, 1)),
    Point(-1, 0): (Point(0, -1), Point(0, 1)),
}


def print_map(lines: list[str], current: Point, direction: Point) -> None:
    direction_map: dict[Point, str] = {
        Point(0, 1): "v",
        Point(0, -1): "^",
        Point(1, 0): ">",
        Point(-1, 0): "<",
    }
    for j, line in enumerate(lines):
        if j != current.y:
            print(line)
            continue
        s = ""
        for i, char in enumerate(line):
            if i != current.x:
                s += char
                continue
            s += direction_map[direction]
        print(s)


@cache
def solve(input_data: str) -> tuple[int, int]:
    """
    Solve the Reindeer Maze problem.

    Parameters
    ----------
    input_data : str
        The input data as a string.

    Returns
    -------
    tuple[int, int]
        A tuple of two integers. The first integer is the minimum cost to reach the end.
        The second integer is the number of cells which are part of any shortest route.
    """
    lines = input_data.splitlines()

    walls: set[Point] = set()
    start: Point = Point(0, 0)
    end: Point = Point(0, 0)

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == "#":
                walls.add(Point(i, j))
            elif char == "S":
                start = Point(i, j)
            elif char == "E":
                end = Point(i, j)

    direction = Point(1, 0)

    left, right = lr[direction]

    closed_cells: set[tuple[Point, Point]] = set()

    open_cells: list[tuple[int, Point, Point]] = []
    route_map: dict[tuple[int, Point, Point], list[Point]] = defaultdict(list[Point])

    if start.add(direction) not in walls:
        c = (1, start.add(direction), direction)
        heapq.heappush(open_cells, c)
        route_map[c] += [start]

    for d in [left, right]:
        if start.add(d) not in walls:
            c = (1001, start.add(d), d)
            heapq.heappush(open_cells, c)
            route_map[c] += [start]

    cost = 0
    all_routes = []
    while True:
        cost, next_cell, direction = heapq.heappop(open_cells)
        route = route_map[(cost, next_cell, direction)]

        if next_cell == end:
            all_routes = route
            break

        if (next_cell, direction) in closed_cells:
            continue

        closed_cells.add((next_cell, direction))
        left, right = lr[direction]
        new_route = route + [next_cell]

        forward_cell = next_cell.add(direction)
        if forward_cell not in walls:
            c = (cost + 1, forward_cell, direction)
            heapq.heappush(open_cells, c)
            route_map[c] += new_route

        for d in [left, right]:
            side_cell = next_cell.add(d)
            if side_cell not in walls and (side_cell, d) not in closed_cells:
                c = (cost + 1001, side_cell, d)
                heapq.heappush(open_cells, c)
                route_map[c] += new_route

    all_routes = set(all_routes)

    # for j, line in enumerate(lines):
    #     s = ""
    #     for i, char in enumerate(line):
    #         if char == "S":
    #             s += "S"
    #         elif char == "E":
    #             s += "E"
    #         elif char == "#":
    #             s += "█"
    #         else:
    #             if Point(i, j) in all_routes:
    #                 s += "•"
    #             else:
    #                 s += " "
    #     print(s)

    return cost, len(set(all_routes)) + 1


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    cost, _ = solve(input_data)
    return cost


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    _, all_routes = solve(input_data)
    return all_routes


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 16 - Reindeer Maze")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
