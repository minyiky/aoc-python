from __future__ import annotations


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

    def __lt__(self, other: Point) -> bool:
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __gt__(self, other: Point) -> bool:
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def add(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)

    def dist(self, p: Point) -> int:
        return abs(self.x - p.x) + abs(self.y - p.y)
