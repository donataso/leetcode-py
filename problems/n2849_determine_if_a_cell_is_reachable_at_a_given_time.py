import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time
    difficulty: medium
    """

    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False

        return max(abs(sx - fx), abs(sy - fy)) <= t


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [2, 4, 7, 7, 6],
            # expected
            True,
        )
        yield (
            # params
            [3, 1, 7, 3, 3],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.isReachableAtTime(*params))


if __name__ == '__main__':
    unittest.main()
