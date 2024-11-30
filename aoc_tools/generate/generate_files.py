import os
import sys

from ..parser.parser import parse_examples


def create_day_files(year: int, day: int):
    """Create solution and teat files for the day"""
    day_folder = f"day{day:02d}"
    full_folder = f"{year}/{day_folder}"

    example_path = os.path.join(full_folder, "example.txt")

    with open(example_path, "r") as f:
        example_content = f.read()

    title, _ = parse_examples(example_content)

    # Create the __init__.py file in the day folder
    with open(os.path.join(full_folder, "__init__.py"), "w") as f:
        f.write(f"# Day {day} solution\n")

    # Create the solution.py file
    solution_file = os.path.join(full_folder, "solution.py")
    with open(solution_file, "w") as f:
        f.write(
            f'''"""Solution for Day {day} - {title}"""

def part_one(input_data: str) -> int:
    """Implement part one logic"""
    pass

def part_two(input_data: str) -> int:
    """Implement part two logic"""
    pass

if __name__ == "__main__":
    with open("{day_folder}/input.txt") as f:
        input_data = f.read()
    print("Solution for Day {day} - {title}")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
'''
        )

    # Create the test.py file for tests
    test_file = os.path.join(full_folder, "test.py")
    with open(test_file, "w") as f:
        f.write(
            f'''"""Tests for Day Day {day} - {title}"""
import unittest
import os

from .solution import part_one, part_two
from aoc_tools.parser import get_example_data, parse_examples


class TestDay1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """This method runs once for the entire test suite to parse the example file."""
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Store the parsed data for tests
        with open(f"'''
            + "{dir_path}"
            + '''/example.txt", "r") as f:
            example_data = f.read()

        _, cls.examples = parse_examples(example_data)

    def test_part_one(self):
        """Test for part one"""
        input_data, expected_result = get_example_data(self.examples, 1)

        result = part_one(input_data)
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        """Test for part two"""
        input_data, expected_result = get_example_data(self.examples, 2)

        result = part_two(input_data)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
'''
        )

    test_file = os.path.join(full_folder, "__init__.py")
    with open(test_file, "w") as f:
        f.write(f'"""Module for Day {day} - {title}"""')

    print(f"Files for day {day} created successfully!")


def main():
    if len(sys.argv) < 3:
        print(
            "Please specify the year and day number (e.g., python generate_files.py 2024 1)"
        )
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])
    create_day_files(year, day)
    print(f"Template files generated for day {day}")


if __name__ == "__main__":
    main()
