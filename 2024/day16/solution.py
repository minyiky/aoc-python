"""Solution for Day 16 - Reindeer Maze"""

from __future__ import annotations

import os
import heapq


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def add(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)

    def dist(self, p: Point) -> int:
        return abs(self.x - p.x) + abs(self.y - p.y)


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


def part_one(input_data: str) -> int:
    """Implement part one logic"""
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

    open_cells: dict[tuple[Point, Point], int] = {}

    if start.add(direction) not in walls:
        open_cells[start.add(direction), direction] = 1
    if start.add(left) not in walls:
        open_cells[start.add(left), left] = 1001
    if start.add(right) not in walls:
        open_cells[start.add(right), right] = 1001

    cost = 0
    while True:
        next_cell, direction = min(open_cells, key=lambda cell: open_cells[cell])
        cost = open_cells[(next_cell, direction)]

        # print(f"looking at {next_cell} with cost {cost}")
        # print_map(lines, next_cell, direction)

        if next_cell == end:
            break

        closed_cells.add((next_cell, direction))
        del open_cells[(next_cell, direction)]

        left, right = lr[direction]

        if next_cell.add(direction) not in walls:
            open_cells[(next_cell.add(direction), direction)] = cost + 1

        new_cost = cost + 1001
        for d in [left, right]:
            side_cell = next_cell.add(d)
            if (
                side_cell not in walls
                and (side_cell, d) not in closed_cells
                and (
                    (side_cell, d) not in open_cells
                    or open_cells[side_cell, d] > new_cost
                )
            ):
                open_cells[(side_cell, d)] = new_cost

    return cost


def part_two(input_data: str) -> int:
    """Implement part two logic"""
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

    open_cells: dict[tuple[Point, Point], tuple[int, set[Point]]] = {}

    if start.add(direction) not in walls:
        open_cells[start.add(direction), direction] = (1, {start})
    if start.add(left) not in walls:
        open_cells[start.add(left), left] = (1001, {start})
    if start.add(right) not in walls:
        open_cells[start.add(right), right] = (1001, {start})

    cost = 0
    all_routes = set()
    while True:
        next_cell, direction = min(open_cells, key=lambda cell: open_cells[cell][0])
        cost, route = open_cells[(next_cell, direction)]

        # print(f"looking at {next_cell} with cost {cost}")
        # print_map(lines, next_cell, direction)

        if next_cell == end:
            all_routes = route
            break

        closed_cells.add((next_cell, direction))
        del open_cells[(next_cell, direction)]

        left, right = lr[direction]

        new_route = {next_cell}.union(route)

        forward_cell = next_cell.add(direction)
        if forward_cell not in walls:
            if (forward_cell, direction) not in open_cells:
                open_cells[(forward_cell, direction)] = (
                    cost + 1,
                    new_route,
                )
            elif open_cells[forward_cell, direction][0] == cost + 1:
                open_cells[forward_cell, direction] = (
                    cost + 1,
                    open_cells[forward_cell, direction][1].union(new_route),
                )
            elif open_cells[forward_cell, direction][0] > cost + 1:
                open_cells[forward_cell, direction] = (
                    cost + 1,
                    new_route,
                )
            # continue

        new_cost = cost + 1001
        for d in [left, right]:
            side_cell = next_cell.add(d)
            if side_cell not in walls and (side_cell, d) not in closed_cells:
                if (side_cell, d) not in open_cells:
                    open_cells[(side_cell, d)] = (new_cost, new_route)
                else:
                    if open_cells[side_cell, d][0] > new_cost:
                        open_cells[side_cell, d] = (new_cost, new_route)
                    elif open_cells[side_cell, d][0] == new_cost:
                        open_cells[side_cell, d] = (
                            new_cost,
                            open_cells[side_cell, d][1].union(new_route),
                        )

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

    return len(all_routes) + 1


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 16 - Reindeer Maze")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
