import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/pascals-triangle/
    difficulty: easy
    """

    def generate(self, numRows: int) -> list[list[int]]:
        result: list[list[int]] = [[1] for _ in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])
            result[i].append(1)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [5],
            # expected
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )
        yield (
            # params
            [1],
            # expected
            [[1]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.generate(*params))


if __name__ == '__main__':
    unittest.main()
