import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/fraction-to-recurring-decimal
    difficulty: medium
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 or denominator == 1:
            return str(numerator)
        elif denominator == -1:
            return str(-numerator)

        remainders: list[int] = []
        sign = ''
        if bool(numerator < 0) ^ bool(denominator < 0):
            sign = '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

        result = [numerator // denominator]
        numerator = numerator % denominator

        if not numerator:
            return sign + str(result[0])

        result.append('.')

        while numerator and numerator not in remainders:
            remainders.append(numerator)
            numerator *= 10
            result.append(numerator // denominator)
            numerator = numerator % denominator

        if not numerator:
            return sign + ''.join(map(str, result))

        idx = remainders.index(numerator)

        return '{}{}({})'.format(
            sign,
            ''.join(map(str, result[:2 + idx])),
            ''.join(map(str, result[2 + idx:])),
        )


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [-2147483648, 1],
            # expected
            '-2147483648',
        )
        yield (
            # params
            [0, -1],
            # expected
            '0',
        )
        yield (
            # params
            [-50, 8],
            # expected
            '-6.25',
        )
        yield (
            # params
            [1, 2],
            # expected
            '0.5',
        )
        yield (
            # params
            [2, 1],
            # expected
            '2',
        )
        yield (
            # params
            [4, 333],
            # expected
            '0.(012)',
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.fractionToDecimal(*params))


if __name__ == '__main__':
    unittest.main()
