import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/diagonal-traverse-ii/
    difficulty: medium
    """

    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        result: list[list[int]] = []

        for m in range(len(nums)):
            for n in range(len(nums[m])):
                if m + n == len(result):
                    result.append([])
                result[m + n].append(nums[m][n])

        return [num for row in result for num in reversed(row)]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            # expected
            [1, 4, 2, 7, 5, 3, 8, 6, 9],
        )
        yield (
            # params
            [[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]],
            # expected
            [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findDiagonalOrder(*params))


if __name__ == '__main__':
    unittest.main()
