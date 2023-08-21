import unittest
from math import factorial, comb

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/unique-paths/
    difficulty: medium
    """

    def uniquePaths(self, m: int, n: int) -> int:
        return self.more_python(m, n)
        # return self.binomial(m, n)
        # return self.dp(m, n)

    def dp(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[-1][-1]

    def more_python(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

    def binomial(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [3, 7],
            # expected
            28,
        )
        yield (
            # params
            [3, 2],
            # expected
            3,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.uniquePaths(*params))


if __name__ == '__main__':
    unittest.main()
