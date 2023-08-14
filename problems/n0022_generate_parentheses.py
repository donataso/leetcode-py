import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/generate-parentheses
    difficulty: medium
    """

    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        def backtrack(string, left_count, right_count):
            if len(string) == 2 * n:
                result.append(string)
                return
            if left_count < n:
                backtrack(string + '(', left_count + 1, right_count)
            if left_count > right_count:
                backtrack(string + ')', left_count, right_count + 1)

        backtrack('', 0, 0)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [3],
            # expected
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        yield (
            # params
            [1],
            # expected
            ["()"],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.generateParenthesis(*params))


if __name__ == '__main__':
    unittest.main()
