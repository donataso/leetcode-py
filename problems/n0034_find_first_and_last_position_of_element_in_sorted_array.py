import unittest
from bisect import bisect_left, bisect_right

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    difficulty: medium
    """

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return self.much_python(nums, target)
        # return self.two_binary_searches(nums, target)

    def much_python(self, nums: list[int], target: int) -> list[int]:
        start = bisect_left(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, bisect_right(nums, target) - 1]

    def two_binary_searches(self, nums: list[int], target: int) -> list[int]:
        # first look for the start position
        low = 0
        high = len(nums) - 1
        target_start = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                target_start = mid
                break
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        if target_start == -1:
            return [-1, -1]

        low = target_start
        high = len(nums) - 1
        target_end = high
        while low <= high:
            mid = low + (high - low + 1) // 2  # right from the middle im case of even number of elements
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                target_end = mid
                break
            if nums[mid] > target:  # cut the right only when strictly greater
                high = mid - 1
            else:
                low = mid + 1

        return [target_start, target_end]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[0, 0, 0, 1, 2, 3], 0],
            # expected
            [0, 2],
        )
        yield (
            # params
            [[0, 0, 1, 2, 2], 0],
            # expected
            [0, 1],
        )
        yield (
            # params
            [[5, 7, 7, 8, 8, 10], 8],
            # expected
            [3, 4],
        )
        yield (
            # params
            [[5, 7, 7, 8, 8, 10], 6],
            # expected
            [-1, -1],
        )
        yield (
            # params
            [[], 0],
            # expected
            [-1, -1],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.searchRange(*params))


if __name__ == '__main__':
    unittest.main()
