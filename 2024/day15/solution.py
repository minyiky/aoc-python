"""Solution for Day 15 - Warehouse Woes"""

import os


directions: dict[str, tuple[int, int]] = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def can_move(
    start: tuple[int, int],
    direction: tuple[int, int],
    walls: set[tuple[int, int]],
    boxes: set[tuple[int, int]],
):
    new_point = (start[0] + direction[0], start[1] + direction[1])
    if new_point in walls:
        return False
    if new_point in boxes:
        if can_move(new_point, direction, walls, boxes):
            boxes.add((new_point[0] + direction[0], new_point[1] + direction[1]))
            boxes.remove(new_point)
            return True
        else:
            return False
    return True


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    walls: set[tuple[int, int]] = set()
    boxes: set[tuple[int, int]] = set()
    start: tuple[int, int] = (0, 0)

    gap_index: int = 0

    lines = input_data.splitlines()

    for gap_index, line in enumerate(lines):
        if line == "":
            break
        for i, char in enumerate(line):
            if char == "#":
                walls.add((i, gap_index))
            elif char == "O":
                boxes.add((i, gap_index))
            elif char == "@":
                start = (i, gap_index)

    instructions: str = ""
    for line in lines[gap_index + 1 :]:
        instructions += line

    for instruction in instructions:
        direction = directions[instruction]
        if can_move(start, direction, walls, boxes):
            start = (start[0] + direction[0], start[1] + direction[1])

    # Print the map
    # for j in range(gap_index):
    #     line = ""
    #     for i in range(len(lines[0])):
    #         if (i, j) in walls:
    #             line += "#"
    #         elif (i, j) in boxes:
    #             line += "O"
    #         elif (i, j) == start:
    #             line += "@"
    #         else:
    #             line += "."
    #     print(line)

    return sum(100 * box[1] + box[0] for box in boxes)


def can_move_lr(
    start: tuple[int, int],
    direction: tuple[int, int],
    walls: set[tuple[int, int]],
    boxes_l: set[tuple[int, int]],
    boxes_r: set[tuple[int, int]],
) -> bool:
    new_point = (start[0] + direction[0], start[1] + direction[1])
    if new_point in walls:
        return False
    if new_point in boxes_l:
        if can_move_lr(new_point, direction, walls, boxes_l, boxes_r):
            boxes_l.add((new_point[0] + direction[0], new_point[1] + direction[1]))
            boxes_l.remove(new_point)
            return True
        else:
            return False
    elif new_point in boxes_r:
        if can_move_lr(new_point, direction, walls, boxes_l, boxes_r):
            boxes_r.add((new_point[0] + direction[0], new_point[1] + direction[1]))
            boxes_r.remove(new_point)
            return True
        else:
            return False
    return True


def can_move_ud(
    start: tuple[int, int],
    direction: tuple[int, int],
    walls: set[tuple[int, int]],
    boxes_l: set[tuple[int, int]],
    boxes_r: set[tuple[int, int]],
    old_boxes_l: set[tuple[int, int]],
    old_boxes_r: set[tuple[int, int]],
    new_boxes_l: set[tuple[int, int]],
    new_boxes_r: set[tuple[int, int]],
) -> bool:
    new_point = (start[0] + direction[0], start[1] + direction[1])
    if new_point in walls:
        return False
    if new_point in boxes_l or new_point in boxes_r:
        left_point = (
            new_point if new_point in boxes_l else (new_point[0] - 1, new_point[1])
        )
        right_point = (
            new_point if new_point in boxes_r else (new_point[0] + 1, new_point[1])
        )
        old_boxes_l.add(left_point)
        old_boxes_r.add(right_point)
        if can_move_ud(
            left_point,
            direction,
            walls,
            boxes_l,
            boxes_r,
            old_boxes_l,
            old_boxes_r,
            new_boxes_l,
            new_boxes_r,
        ) and can_move_ud(
            right_point,
            direction,
            walls,
            boxes_l,
            boxes_r,
            old_boxes_l,
            old_boxes_r,
            new_boxes_l,
            new_boxes_r,
        ):
            new_boxes_l.add(
                (left_point[0] + direction[0], left_point[1] + direction[1])
            )
            new_boxes_r.add(
                (right_point[0] + direction[0], right_point[1] + direction[1])
            )
            return True
        else:
            return False
    return True


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    walls: set[tuple[int, int]] = set()
    boxes_l: set[tuple[int, int]] = set()
    boxes_r: set[tuple[int, int]] = set()
    start: tuple[int, int] = (0, 0)

    gap_index: int = 0

    lines = input_data.splitlines()

    for gap_index, line in enumerate(lines):
        if line == "":
            break
        for i, char in enumerate(line):
            if char == "#":
                walls.add((2 * i, gap_index))
                walls.add((2 * i + 1, gap_index))
            elif char == "O":
                boxes_l.add((2 * i, gap_index))
                boxes_r.add((2 * i + 1, gap_index))
            elif char == "@":
                start = (2 * i, gap_index)

    instructions: str = ""
    for line in lines[gap_index + 1 :]:
        instructions += line

    for instruction in instructions:
        direction = directions[instruction]
        if instruction == "<" or instruction == ">":
            if can_move_lr(start, direction, walls, boxes_l, boxes_r):
                start = (start[0] + direction[0], start[1] + direction[1])
        else:
            old_boxes_l: set[tuple[int, int]] = set()
            old_boxes_r: set[tuple[int, int]] = set()
            new_boxes_l: set[tuple[int, int]] = set()
            new_boxes_r: set[tuple[int, int]] = set()
            if can_move_ud(
                start,
                direction,
                walls,
                boxes_l=boxes_l,
                boxes_r=boxes_r,
                old_boxes_l=old_boxes_l,
                old_boxes_r=old_boxes_r,
                new_boxes_l=new_boxes_l,
                new_boxes_r=new_boxes_r,
            ):
                for box in old_boxes_l:
                    boxes_l.remove(box)
                for box in old_boxes_r:
                    boxes_r.remove(box)
                for box in new_boxes_l:
                    boxes_l.add(box)
                for box in new_boxes_r:
                    boxes_r.add(box)
                start = (start[0] + direction[0], start[1] + direction[1])

    # Print the map
    # for j in range(gap_index):
    #     line = ""
    #     for i in range(len(lines[0]) * 2):
    #         if (i, j) in walls:
    #             line += "#"
    #         elif (i, j) in boxes_l:
    #             line += "["
    #         elif (i, j) in boxes_r:
    #             line += "]"
    #         elif (i, j) == start:
    #             line += "@"
    #         else:
    #             line += "."
    #     print(line)

    return sum(100 * box[1] + box[0] for box in boxes_l)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 15 - Warehouse Woes")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
