import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/sort-colors
    difficulty: medium
    """

    def sortColors(self, nums: list[int]) -> None:
        self.one_pass(nums)
        # self.count(nums)

    def one_pass(self, nums: list[int]) -> None:
        p0 = 0
        curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                continue
            if nums[curr] == 0 and curr > p0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                continue
            curr += 1

    def count(self, nums: list[int]) -> None:
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i = 0
        for n, c in enumerate(counts):
            for _ in range(c):
                nums[i] = n
                i += 1


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[2, 0, 2, 1, 1, 0]],
            # expected
            [0, 0, 1, 1, 2, 2],
        )
        yield (
            # params
            [[2, 0, 1]],
            # expected
            [0, 1, 2],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        nums = params[0]
        solution.sortColors(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
