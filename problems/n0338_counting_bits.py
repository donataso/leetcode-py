import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/counting-bits/
    difficulty: easy
    """

    def countBits(self, n: int) -> list[int]:
        return [i.bit_count() for i in range(n + 1)]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [2],
            # expected
            [0, 1, 1],
        )
        yield (
            # params
            [5],
            # expected
            [0, 1, 1, 2, 1, 2],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.countBits(*params))


if __name__ == '__main__':
    unittest.main()
