import unittest
import heapq
from typing import TypeAlias

from helper.unittest_data_provider import data_provider

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
        # return self.bs_bfs(heights)
        return self.dijkstra(heights)

    def bs_bfs(self, heights: list[list[int]]) -> int:
        """
        This is supposedly a lot faster than the Dijkstra approach, but it takes a lot longer to run official tests.
        """
        start: Point = (0, 0)
        destination: Point = (len(heights) - 1, len(heights[0]) - 1)

        def can_reach_destination(pos: Point, threshold: int, visited: set[Point]) -> bool:
            if pos == destination:
                return True

            for diff in self.NEIGHBOURS:
                adj: Point = (pos[0] + diff[0], pos[1] + diff[1])

                if adj in visited or adj[0] < 0 or adj[0] > destination[0] or adj[1] < 0 or adj[1] > destination[1]:
                    continue

                if abs(heights[pos[0]][pos[1]] - heights[adj[0]][adj[1]]) <= threshold:
                    if adj == destination:
                        return True

                    visited.add(adj)
                    if can_reach_destination(adj, threshold, visited):
                        return True

            return False

        low = 0
        high = 10 ** 6
        while low < high:
            mid = low + (high - low) // 2
            if can_reach_destination(start, mid, {start}):
                high = mid
            else:
                low = mid + 1

        return low

    def dijkstra(self, heights: list[list[int]]) -> int:
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
                adj: Point = (s[0] + diff[0], s[1] + diff[1])
                if adj[0] < 0 or adj[0] > destination[0] or adj[1] < 0 or adj[1] > destination[1]:
                    continue

                # the essence of the approach: track the largest height differences
                dist = max(d, abs(heights[s[0]][s[1]] - heights[adj[0]][adj[1]]))
                if adj not in distances or dist < distances[adj]:
                    distances[adj] = dist
                    heapq.heappush(queue, (dist, adj))

        return distances[destination]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[3]]],
            # expected
            0,
        )
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
