import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/coin-change-ii/
    difficulty: medium
    """

    def change(self, amount: int, coins: list[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [3, [1, 2]],
            # expected
            2,
        )
        yield (
            # params
            [10, [2, 5]],
            # expected
            2,
        )
        yield (
            # params
            [5, [1, 2, 5]],
            # expected
            4,
        )
        yield (
            # params
            [3, [2]],
            # expected
            0,
        )
        yield (
            # params
            [10, [10]],
            # expected
            1,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.change(*params))


if __name__ == '__main__':
    unittest.main()
