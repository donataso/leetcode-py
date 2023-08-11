import sys
import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/increasing-triplet-subsequence
    difficulty: medium
    """

    def increasingTriplet(self, nums: list[int]) -> bool:
        n1 = n2 = sys.maxsize
        for n in nums:
            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n
            else:
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 2, 3, 4, 5]],
            # expected
            True,
        )
        yield (
            # params
            [[5, 4, 3, 2, 1]],
            # expected
            False,
        )
        yield (
            # params
            [[2, 1, 5, 0, 4, 6]],
            # expected
            True,
        )
        yield (
            # params
            [[2, 1, 5, 7, 4, 6, 5]],
            # expected
            True,
        )
        yield (
            # params
            [[1,1,-2,6]],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.increasingTriplet(*params))


if __name__ == '__main__':
    unittest.main()
