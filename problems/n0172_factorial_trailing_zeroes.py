import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/factorial-trailing-zeroes
    difficulty: medium
    """

    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [3],
            # expected
            0,
        )
        yield (
            # params
            [5],
            # expected
            1,
        )
        yield (
            # params
            [0],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.trailingZeroes(*params))


if __name__ == '__main__':
    unittest.main()
