import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/missing-ranges/
    difficulty: easy
    """

    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        return self.kindOfHardToRead(nums, lower, upper)

    def kindOfCleaner(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]

        result: list[list[int]] = []
        if nums[0] != lower:
            result.append([lower, nums[1] - 1])

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                result.append([nums[i] + 1, nums[i + 1]])

        if nums[-1] != upper:
            result.append([nums[-1] + 1, upper])

        return result

    def kindOfHardToRead(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        missing_range = [lower, upper]
        if not nums:
            return [missing_range]

        result: list[list[int]] = []

        for n in nums:
            if n < lower:
                continue
            if missing_range[0] == n:
                missing_range[0] += 1
            else:
                missing_range[1] = n - 1
                result.append(missing_range)
                missing_range = [n + 1, upper]

        if missing_range[1] != n:
            result.append(missing_range)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[], 1, 1],
            # expected
            [[1, 1]],
        )
        yield (
            # params
            [[0, 1, 3, 50, 75], 0, 99],
            # expected
            [[2, 2], [4, 49], [51, 74], [76, 99]],
        )
        yield (
            # params
            [[-1], -1, -1],
            # expected
            [],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findMissingRanges(*params))


if __name__ == '__main__':
    unittest.main()
