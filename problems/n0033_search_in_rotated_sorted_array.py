import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/
    difficulty: medium
    """

    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:  # left side is sorted
                if nums[low] <= target < nums[mid]:  # is the target in the sorted side (left)?
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right side is sorted
                if nums[mid] < target <= nums[high]:  # is the target in the sorted side (right)?
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[7, 8, 0, 1, 2, 3, 4, 5, 6], 0],
            # expected
            2,
        )
        yield (
            # params
            [[4, 5, 6, 7, 0, 1, 2], 0],
            # expected
            4,
        )
        yield (
            # params
            [[4, 5, 6, 7, 0, 1, 2], 3],
            # expected
            -1,
        )
        yield (
            # params
            [[1], 0],
            # expected
            -1,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.search(*params))


if __name__ == '__main__':
    unittest.main()
