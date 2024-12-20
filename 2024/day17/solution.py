"""Solution for Day 16 - Reindeer Maze"""

from __future__ import annotations

import os


def combo(op: int, registers: list[int]) -> int:
    return op if op < 4 else registers[op - 4]


def part_one(input_data: str) -> str:
    """Implement part one logic"""
    lines = input_data.splitlines()
    registers: list[int] = [0, 0, 0]
    for i in range(3):
        registers[i] = int(lines[i].split()[-1])

    opcode = list(map(int, lines[4].split()[-1].split(",")))

    def dv(i: int):
        c = combo(opcode[i + 1], registers)
        return registers[0] // (2**c)

    i = 0
    output: list[int] = []
    n_opcode = len(opcode)
    while i < n_opcode:
        if opcode[i] == 0:
            registers[0] = dv(i)
        elif opcode[i] == 1:
            registers[1] = registers[1] ^ opcode[i + 1]
        elif opcode[i] == 2:
            registers[1] = combo(opcode[i + 1], registers) % 8
        elif opcode[i] == 3:
            i = opcode[i + 1] - 2 if registers[0] != 0 else i
        elif opcode[i] == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode[i] == 5:
            output.append(combo(opcode[i + 1], registers) % 8)
        elif opcode[i] == 6:
            registers[1] = dv(i)
        elif opcode[i] == 7:
            registers[2] = dv(i)
        i += 2

    return ",".join(str(o) for o in output)


def calc(opcode: list[int], registers: list[int], target: list[int]) -> bool:
    def dv(i: int):
        c = combo(opcode[i + 1], registers)
        return registers[0] // (2**c)

    i = 0
    output: list[int] = []
    n_opcode = len(opcode)
    while i < n_opcode:
        if opcode[i] == 0:
            registers[0] = dv(i)
        elif opcode[i] == 1:
            registers[1] = registers[1] ^ opcode[i + 1]
        elif opcode[i] == 2:
            registers[1] = combo(opcode[i + 1], registers) % 8
        elif opcode[i] == 3:
            i = opcode[i + 1] - 2 if registers[0] != 0 else i
        elif opcode[i] == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode[i] == 5:
            output.append(combo(opcode[i + 1], registers) % 8)
            if output == target:
                return True
            elif len(output) > len(target):
                return False
        elif opcode[i] == 6:
            registers[1] = dv(i)
        elif opcode[i] == 7:
            registers[2] = dv(i)
        i += 2
    return False


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    registers: list[int] = [0, 0, 0]
    for i in range(3):
        registers[i] = int(lines[i].split()[-1])

    opcode = list(map(int, lines[4].split()[-1].split(",")))

    works: list[str] = ["0"]
    for j in range(len(opcode)):
        new_works: list[str] = []
        for i in range(8):
            for w in works:
                registers[0] = int(f"{w}{i}", 8)
                if calc(opcode, registers, opcode[-(j + 1) :]):
                    new_works.append(f"{w}{i}")
        works = new_works

    return min(int(o, 8) for o in works)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day 16 - Reindeer Maze")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
    print()  # Add a new line to separate solutions
