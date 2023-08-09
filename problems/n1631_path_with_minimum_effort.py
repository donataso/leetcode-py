import unittest
import heapq
from typing import TypeAlias

from unittest_data_provider import data_provider  # type: ignore

Point: TypeAlias = tuple[int, int]


class Solution:
    """
    https://leetcode.com/problems/path-with-minimum-effort
    difficulty: medium
    """

    NEIGHBOURS: list[Point] = [
        (0, -1),  # left
        (0, 1),  # right
        (-1, 0),  # up
        (1, 0),  # down
    ]

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Here I use Dijkstra's algorithm to traverse and use max height diff as a distance
        """
        distances: dict[Point, int] = {(0, 0): 0}
        queue: list[tuple[int, Point]] = []
        heapq.heappush(queue, (0, (0, 0)))
        destination: Point = (len(heights) - 1, len(heights[0]) - 1)

        while queue:
            d, s = heapq.heappop(queue)
            if s not in distances or distances[s] < d:
                continue
            elif s == destination:
                return d

            for diff in self.NEIGHBOURS:
                pos: Point = (s[0] + diff[0], s[1] + diff[1])
                if pos[0] < 0 or pos[0] > destination[0] or pos[1] < 0 or pos[1] > destination[1]:
                    continue

                # the essence of the approach: track the largest height differences
                dist = max(d, abs(heights[s[0]][s[1]] - heights[pos[0]][pos[1]]))
                if pos not in distances or dist < distances[pos]:
                    distances[pos] = dist
                    heapq.heappush(queue, (dist, pos))

        return distances[destination]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 10, 6, 7, 9, 10, 4, 9]]],
            # expected
            9,
        )
        yield (
            # params
            [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]],
            # expected
            2,
        )
        yield (
            # params
            [[[1, 2, 3], [3, 8, 4], [5, 3, 5]]],
            # expected
            1,
        )
        yield (
            # params
            [[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.minimumEffortPath(*params))


if __name__ == '__main__':
    unittest.main()
