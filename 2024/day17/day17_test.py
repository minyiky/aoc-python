"""Tests for Day 17 - Reindeer Maze"""

import unittest

from .solution import part_one


class TestDay17(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """This method runs once for the entire test suite to parse the example file."""
        # Store the parsed data for tests
        cls.input_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

    def test_part_one(self):
        """Test for part one"""
        result = part_one(self.input_data)
        self.assertEqual(result, "4,6,3,5,6,3,5,2,1,0")

    def test_part_two(self):
        """Test for part two"""
        pass


if __name__ == "__main__":
    unittest.main()
