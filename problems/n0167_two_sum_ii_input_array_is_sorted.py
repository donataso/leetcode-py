import unittest
from typing import Dict

from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
    difficulty: medium
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = len(nums) - 1
        while start < end:
            sum_ = nums[start] + nums[end]
            if sum_ == target:
                return [start + 1, end + 1]

            if sum_ < target:
                start += 1
            else:
                end -= 1

        return []


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[2, 7, 11, 15], 9],
            # expected
            [1, 2],
        )
        yield (
            # params
            [[2, 3, 4], 6],
            # expected
            [1, 3],
        )
        yield (
            # params
            [[-1, 0], -1],
            # expected
            [1, 2],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.twoSum(*params))


if __name__ == '__main__':
    unittest.main()
