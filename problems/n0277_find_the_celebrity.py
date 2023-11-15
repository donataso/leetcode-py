import unittest
from functools import lru_cache

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/find-the-celebrity/
    difficulty: medium
    """

    @lru_cache(maxsize=None)
    def knows_c(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        def is_celebrity(a: int) -> int:
            for b in range(n):
                if a == b:
                    continue
                if self.knows_c(a, b) or not self.knows_c(b, a):
                    return False
            return True

        candidate = 0
        for i in range(n):
            if candidate == n:
                continue
            if knows(candidate, i):
                candidate = i

        if is_celebrity(candidate):
            return candidate

        return -1


graph: list[list[int]] = []


def knows(a: int, b: int) -> bool:
    return graph[a][b] == 1


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 0, 1], [0, 1, 1], [0, 0, 1]]],
            # expected
            2,
        )
        yield (
            # params
            [[[1, 1], [1, 1]]],
            # expected
            -1,
        )
        yield (
            # params
            [[[1, 1, 0], [0, 1, 0], [1, 1, 1]]],
            # expected
            1,
        )
        yield (
            # params
            [[[1, 0, 1], [1, 1, 0], [0, 1, 1]]],
            # expected
            -1,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        global graph
        graph = params[0]
        solution = Solution()
        self.assertEqual(expected, solution.findCelebrity(len(graph)))


if __name__ == '__main__':
    unittest.main()
