import os
import sys

from ..parser import parse_examples
from .formatting import _format_day, _format_path


def create_day_files(year: int, day: int):
    """Create solution and test files for the day."""
    full_folder = _format_path(year, day)

    os.makedirs(full_folder, exist_ok=True)  # Ensure the folder exists

    example_path = os.path.join(full_folder, "example.txt")
    if not os.path.exists(example_path):
        print(f"Error: {example_path} does not exist. Please provide this file.")
        return

    with open(example_path, "r") as f:
        example_content = f.read()

    title, _ = parse_examples(example_content)

    # File paths
    init_file = os.path.join(full_folder, "__init__.py")
    solution_file = os.path.join(full_folder, "solution.py")
    test_file = os.path.join(full_folder, f"{_format_day(day)}_test.py")

    # Create files only if they don't already exist
    if not os.path.exists(init_file):
        with open(init_file, "w") as f:
            f.write(f"# Day {day} solution\n")
        print(f"Created: {init_file}")

    if not os.path.exists(solution_file):
        with open(solution_file, "w") as f:
            f.write(
                f'''"""Solution for Day {day} - {title}"""

import os


def part_one(input_data: str) -> int:
    """Implement part one logic"""
    pass


def part_two(input_data: str) -> int:
    """Implement part two logic"""
    pass


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"'''
                + "{dir_path}"
                + """/input.txt", "r") as f:
        input_data = f.read()
    print("Solution for Day {day} - {title}")
    print(part_one(input_data))  # Run part one
    print(part_two(input_data))  # Run part two
"""
            )
        print(f"Created: {solution_file}")
    else:
        print(f"Skipped: {solution_file} already exists.")

    if not os.path.exists(test_file):
        with open(test_file, "w") as f:
            f.write(
                f'''"""Tests for Day {day} - {title}"""
import unittest
import os

from .solution import part_one, part_two
from aoc_tools.parser import get_example_data, parse_examples


class TestDay{day}(unittest.TestCase):
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
        print(f"Created: {test_file}")
    else:
        print(f"Skipped: {test_file} already exists.")


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
