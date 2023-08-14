import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/permutation
    difficulty: medium
    """

    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        length = len(nums)

        def backtrack(curr: list[int]):
            nonlocal length
            if len(curr) == length:
                result.append(curr.copy())
                return
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()

        backtrack([])

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 2, 3]],
            # expected
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )
        yield (
            # params
            [[0, 1]],
            # expected
            [[0, 1], [1, 0]],
        )
        yield (
            # params
            [[1]],
            # expected
            [[1]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.permute(*params))


if __name__ == '__main__':
    unittest.main()
