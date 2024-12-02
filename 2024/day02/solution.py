"""Solution for Day 2 - Red-Nosed Reports"""

import os

def check_line(vals: list[int], try_again: bool = False) -> int:
    max_dif, min_dif = 0, 0    
    for i in range(len(vals)-1):
        this, prev = vals[i+1], vals[i]
        if max_dif == 0 and min_dif == 0:
            if this > prev:
                max_dif = 3
                min_dif = 1
            else:
                max_dif = -1
                min_dif = -3
        if (this - prev) > max_dif or (this - prev) < min_dif:
            if try_again:
                # Check a subset of lists with one of the issue numbers removed
                for j in range(min(i-1, 0),max(i+1, len(vals))):
                    if check_line(vals[:j]+vals[j+1:], False) == 1:
                        return 1
            return 0
    return 1
            

def part_one(input_data: str) -> int:
    """Implement part one logic"""
    lines = input_data.splitlines()
    return sum(check_line(list(map(int, line.split()))) for line in lines)    

def part_two(input_data: str) -> int:
    """Implement part two logic"""
    lines = input_data.splitlines()
    return sum(check_line(list(map(int, line.split())), try_again=True) for line in lines)    

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day {day} - {title}")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
