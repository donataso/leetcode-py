import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/excel-sheet-column-number
    difficulty: easy
    """

    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            result *= 26
            result += ord(c) - 65 + 1

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['A'],
            # expected
            1,
        )
        yield (
            # params
            ['AB'],
            # expected
            28,
        )
        yield (
            # params
            ['ZY'],
            # expected
            701,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.titleToNumber(*params))


if __name__ == '__main__':
    unittest.main()
