import unittest
from collections import deque
from typing import TypeAlias, List

from helper.unittest_data_provider import data_provider

Point: TypeAlias = tuple[int, int]

class Solution:
    """
    https://leetcode.com/problems/the-maze/
    difficulty: medium
    """

    NEIGHBOURS: list[Point] = [
        (0, -1),  # left
        (0, 1),  # right
        (-1, 0),  # up
        (1, 0),  # down
    ]

    WALL = 1

    def __init__(self):
        self.maze: list[list[int]] = []

    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        if start == destination:
            return True

        self.maze = maze
        return self.bfs(tuple(start), tuple(destination))  # type: ignore

    def go_direction(self, start: Point, direction: Point) -> Point:
        m, n = start
        while 0 <= m < len(self.maze) and 0 <= n < len(self.maze[m]) and self.maze[m][n] != self.WALL:
            m += direction[0]
            n += direction[1]

        return m - direction[0], n - direction[1]

    def bfs(self, start: Point, final_destination: Point) -> bool:
        visited: set[Point] = {start}
        queue: deque[Point] = deque([start])
        while queue:
            pos = queue.pop()

            for direction in self.NEIGHBOURS:
                dest = self.go_direction(pos, direction)
                if dest == final_destination:
                    return True
                if dest != pos and dest not in visited:
                    visited.add(dest)
                    queue.appendleft(dest)

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [
                [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                [0, 4],
                [4, 4],
            ],
            # expected
            True,
        )
        yield (
            # params
            [
                [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                [0, 4],
                [3, 2],
            ],
            # expected
            False,
        )
        yield (
            # params
            [
                [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                [4, 3],
                [0, 1],
            ],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.hasPath(*params))


if __name__ == '__main__':
    unittest.main()
