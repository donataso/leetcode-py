import unittest
from collections import deque
from typing import Generator

from helper.unittest_data_provider import data_provider

class Solution:
    """
    https://leetcode.com/problems/01-matrix/
    difficulty: medium
    """

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        queue: deque[tuple[int, int, int]] = deque()
        seen: set[tuple[int, int]] = set()
        result: list[list[int]] = [[-1] * n for _ in range(m)]

        def get_neighbours(row: int, col: int) -> Generator[tuple[int, int], None, None]:
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx = row + direction[0]
                yy = col + direction[1]
                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen:
                    yield xx, yy

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    queue.append((0, i, j))

        while queue:
            d, i, j = queue.popleft()
            result[i][j] = d
            for x, y in get_neighbours(i, j):
                seen.add((x, y))
                queue.append((d + 1, x, y))

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]],
            # expected
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        )
        yield (
            # params
            [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]],
            # expected
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
        )
        # mat = [[1] * 1000 for _ in range(1000)]
        # mat[500][500] = 0
        # yield (
        #     # params
        #     [mat],
        #     # expected is not important, I just need this to be processed in a reasonable time
        #     [],
        # )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.updateMatrix(*params))


if __name__ == '__main__':
    unittest.main()
