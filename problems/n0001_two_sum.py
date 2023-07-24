import unittest
from typing import Dict

from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/two-sum/
    difficulty: easy
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diffs: dict[int, int] = {}
        for idx, n in enumerate(nums):
            if n in diffs:
                return [diffs[n], idx]
            else:
                diffs[target - n] = idx

        return []


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[2, 7, 11, 15], 9],
            # expected
            [0, 1],
        )
        yield (
            # params
            [[3, 2, 4], 6],
            # expected
            [1, 2],
        )
        yield (
            # params
            [[3, 3], 6],
            # expected
            [0, 1],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.twoSum(*params))


if __name__ == '__main__':
    unittest.main()
