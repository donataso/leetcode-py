import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    difficulty: medium
    """

    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        def trim_matching_numbers() -> bool:
            """
            Ignore matching numbers at the start and end of the array, they confuse binary search.
            Return True if the target was found.
            """
            nonlocal low, high
            while low < high and nums[low] == nums[high]:
                if nums[low] == target:
                    return True
                low += 1
                high -= 1

            return False

        while low <= high:
            if trim_matching_numbers():
                return True

            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            if nums[mid] >= nums[low]:  # left side is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right side is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1], 0],
            # expected
            False,
        )
        yield (
            # params
            [[1, 0, 1, 1, 1], 0],
            # expected
            True,
        )
        yield (
            # params
            [[2, 5, 6, 0, 0, 1, 2], 0],
            # expected
            True,
        )
        yield (
            # params
            [[2, 5, 6, 0, 0, 1, 2], 3],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.search(*params))


if __name__ == '__main__':
    unittest.main()
