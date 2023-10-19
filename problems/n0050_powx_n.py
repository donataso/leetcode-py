import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/powx-
    difficulty: medium
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1.0 / x
            n *= -1

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [2.0, 10],
            # expected
            1024,
        )
        yield (
            # params
            [2.1, 3],
            # expected
            9.261,
        )
        yield (
            # params
            [2.0, -2],
            # expected
            0.25,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.myPow(*params))


if __name__ == '__main__':
    unittest.main()
