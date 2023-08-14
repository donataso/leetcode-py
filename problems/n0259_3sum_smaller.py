import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/3sum-smaller/
    difficulty: medium
    """

    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.two_sum_smaller(nums, i + 1, target - nums[i])

        return count

    def two_sum_smaller(self, nums: list[int], start_idx: int, target: int) -> int:
        result = 0
        low = start_idx
        high = (len(nums)) - 1
        while low < high:
            if nums[low] + nums[high] < target:
                # there are (high - low) pairs, because nums[low] + (all nums[low < idx <= high]) will match
                result += high - low
                low += 1
            else:
                high -= 1

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[-2, 0, 1, 3], 2],
            # expected
            2,
        )
        yield (
            # params
            [[], 0],
            # expected
            0,
        )
        yield (
            # params
            [[0], 0],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.threeSumSmaller(*params))


if __name__ == '__main__':
    unittest.main()
