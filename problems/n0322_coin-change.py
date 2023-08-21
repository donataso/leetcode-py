import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/coin-change/
    difficulty: medium
    """

    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1  # type: ignore


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[186, 419, 83, 408], 6249],
            # expected
            20,
        )
        yield (
            # params
            [[1, 2, 5], 11],
            # expected
            3,
        )
        yield (
            # params
            [[2], 3],
            # expected
            -1,
        )
        yield (
            # params
            [[1], 0],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.coinChange(*params))


if __name__ == '__main__':
    unittest.main()
