import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/divide-two-integers
    difficulty: medium
    """

    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        if bool(dividend < 0) ^ bool(divisor < 0):
            sign = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > dividend:
            return 0

        def ret(num: int) -> int:
            num = num if sign else -num
            if num > 0x7FFFFFFF:
                return 0x7FFFFFFF
            elif num < -0x80000000:
                return -0x80000000

            return num

        divisors = [(divisor, 1)]
        while divisors[-1][0] < dividend:
            divisors.append((divisors[-1][0] + divisors[-1][0], divisors[-1][1] + divisors[-1][1]))

        if divisors[-1][0] == dividend:
            return ret(divisors[-1][1])

        divisors.pop()

        result = 0
        while dividend >= divisor:
            if divisors[-1][0] <= dividend:
                result += divisors[-1][1]
                dividend -= divisors[-1][0]
            divisors.pop()

        return ret(result)


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [-2147483648, 1],
            # expected
            -2147483648,
        )
        yield (
            # params
            [-2147483648, -1],
            # expected
            2147483647,
        )
        yield (
            # params
            [10, 3],
            # expected
            3,
        )
        yield (
            # params
            [7, -3],
            # expected
            -2,
        )
        yield (
            # params
            [10, 5],
            # expected
            2,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.divide(*params))


if __name__ == '__main__':
    unittest.main()
