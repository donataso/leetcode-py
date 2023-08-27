import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/excel-sheet-column-title/
    difficulty: easy
    """

    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber:
            columnNumber -= 1
            result = chr(65 + columnNumber % 26) + result
            columnNumber //= 26

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [26],
            # expected
            'Z',
        )
        yield (
            # params
            [1],
            # expected
            'A',
        )
        yield (
            # params
            [28],
            # expected
            'AB',
        )
        yield (
            # params
            [701],
            # expected
            'ZY',
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.convertToTitle(*params))


if __name__ == '__main__':
    unittest.main()
