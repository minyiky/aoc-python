"""Solution for Day 18 - RAM Run"""

import os
import heapq

from aoc_tools.helpers import Point


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    walls: set[Point] = set()
    max_x, max_y = 0, 0

    limit = 1024 if len(lines) > 100 else 12
    for i, line in enumerate(lines[:limit]):
        x, y = map(int, line.split(","))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        walls.add(Point(x, y))
    walls = walls.union(
        Point(x, y) for x in [-1, max_x + 1] for y in range(-1, max_y + 2)
    )
    walls = walls.union(
        Point(x, y) for y in [-1, max_y + 1] for x in range(-1, max_x + 2)
    )

    directions: list[Point] = [
        Point(1, 0),
        Point(0, 1),
        Point(-1, 0),
        Point(0, -1),
    ]

    closed_cells: set[Point] = set()
    open_cells: list[tuple[int, Point, list[Point]]] = []

    start = Point(0, 0)
    end = Point(max_x, max_y)

    all_routes = []

    for d in directions:
        if start.add(d) not in walls:
            c = (1 + 2 * end.dist(start.add(d)), start.add(d), [start])
            heapq.heappush(open_cells, c)

    while True:
        cost, next_cell, route = heapq.heappop(open_cells)

        if next_cell == end:
            all_routes = route
            break

        if next_cell in closed_cells:
            continue

        closed_cells.add(next_cell)

        new_route = route + [next_cell]

        for d in directions:
            side_cell = next_cell.add(d)
            if side_cell not in walls and side_cell not in closed_cells:
                c = (cost + 1 + 2 * end.dist(start.add(d)), side_cell, new_route)
                heapq.heappush(open_cells, c)

    all_routes = set(all_routes)

    # for j in range(-1, max_y + 2):
    #     s = ""
    #     for i in range(-1, max_x + 2):
    #         p = Point(i, j)
    #         if p in walls:
    #             s += "█"
    #         elif p == start:
    #             s += "S"
    #         elif p == end:
    #             s += "E"
    #         elif p in all_routes:
    #             s += "•"
    #         else:
    #             s += " "
    #     print(s)

    return len(all_routes)


def find_route(start: Point, end: Point, walls: set[Point]) -> None | set[Point]:
    directions: list[Point] = [
        Point(1, 0),
        Point(0, 1),
        Point(-1, 0),
        Point(0, -1),
    ]

    closed_cells: set[Point] = set()
    open_cells: list[tuple[int, Point, list[Point]]] = []

    for d in directions:
        if start.add(d) not in walls:
            c = (1 + 2 * end.dist(start.add(d)), start.add(d), [start])
            heapq.heappush(open_cells, c)

    try:
        while True:
            cost, next_cell, route = heapq.heappop(open_cells)

            if next_cell == end:
                return set(route)

            if next_cell in closed_cells:
                continue

            closed_cells.add(next_cell)

            new_route = route + [next_cell]

            for d in directions:
                side_cell = next_cell.add(d)
                if side_cell not in walls and side_cell not in closed_cells:
                    c = (cost + 1 + 2 * end.dist(start.add(d)), side_cell, new_route)
                    heapq.heappush(open_cells, c)
    except:
        return None


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    walls: set[Point] = set()
    max_x = 6 if len(lines) < 100 else 70
    max_y = 6 if len(lines) < 100 else 70

    start = Point(0, 0)
    end = Point(max_x, max_y)

    walls = walls.union(
        Point(x, y) for x in [-1, max_x + 1] for y in range(-1, max_y + 2)
    )
    walls = walls.union(
        Point(x, y) for y in [-1, max_y + 1] for x in range(-1, max_x + 2)
    )

    route: None | set[Point] = find_route(start, end, walls)
    if route is None:
        return -1
    # for j in range(-1, max_y + 2):
    #     s = ""
    #     for i in range(-1, max_x + 2):
    #         p = Point(i, j)
    #         if p in walls:
    #             s += "█"
    #         elif p == start:
    #             s += "S"
    #         elif p == end:
    #             s += "E"
    #         elif p in route:
    #             s += "•"
    #         else:
    #             s += " "
    #     print(s)

    byte = 0
    for line_num, line in enumerate(lines):
        # for j in range(-1, max_y + 2):
        #     s = ""
        #     for i in range(-1, max_x + 2):
        #         p = Point(i, j)
        #         if p in walls:
        #             s += "█"
        #         elif p == start:
        #             s += "S"
        #         elif p == end:
        #             s += "E"
        #         elif p in route:
        #             s += "•"
        #         else:
        #             s += " "
        #     print(s)

        # print()

        x, y = map(int, line.split(","))
        walls.add(Point(x, y))
        if Point(x, y) not in route:
            continue
        new_route = find_route(start, end, walls)
        if new_route is None:
            # for j in range(-1, max_y + 2):
            #     s = ""
            #     for i in range(-1, max_x + 2):
            #         p = Point(i, j)
            #         if p in walls:
            #             s += "█"
            #         elif p == start:
            #             s += "S"
            #         elif p == end:
            #             s += "E"
            #         elif p in route:
            #             s += "•"
            #         else:
            #             s += " "
            #     print(s)
            # print(line)
            byte = line_num
            break
        route = new_route

    return byte


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 18 - RAM Run")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
