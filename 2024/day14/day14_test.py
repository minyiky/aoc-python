"""Tests for Day 14 - Restroom Redoubt"""
import unittest
import os

from .solution import part_one, part_two
from aoc_tools.parser import get_example_data, parse_examples


class TestDay14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """This method runs once for the entire test suite to parse the example file."""
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Store the parsed data for tests
        with open(f"{dir_path}/example.txt", "r") as f:
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
