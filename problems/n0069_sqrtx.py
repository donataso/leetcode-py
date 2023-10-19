import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/sqrtx
    difficulty: easy
    """

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1

        hi = x // 2
        lo = 2
        while lo < hi:
            mid = (hi - lo) // 2 + lo + 1
            pw = mid ** 2
            if pw == x:
                return mid
            if pw > x:
                hi = mid - 1
            else:
                lo = mid

        return lo


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [6],
            # expected
            2,
        )
        yield (
            # params
            [0],
            # expected
            0,
        )
        yield (
            # params
            [4],
            # expected
            2,
        )
        yield (
            # params
            [8],
            # expected
            2,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.mySqrt(*params))


if __name__ == '__main__':
    unittest.main()
