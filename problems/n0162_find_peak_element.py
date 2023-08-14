import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/find-peak-element/
    difficulty: medium
    """

    def findPeakElement(self, nums: list[int]) -> int:
        return self.binary_search(nums)
        # return self.linear_better(nums)
        # return self.linear(nums)

    def binary_search(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low

    def linear_better(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def linear(self, nums: list[int]) -> int:
        """
        This is O(n), but the problem asks for O(log m)
        """
        for i, n2 in enumerate(nums):
            n1 = nums[i - 1] if i > 0 else -float('inf')
            n3 = nums[i + 1] if i < len(nums) - 1 else float('inf')

            if n1 < n2 > n3:
                return i

        return len(nums) - 1


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 2, 3, 1]],
            # expected
            [2],
        )
        yield (
            # params
            [[1, 2, 1, 3, 5, 6, 4]],
            # expected
            [1, 5],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertIn(solution.findPeakElement(*params), expected)


if __name__ == '__main__':
    unittest.main()
