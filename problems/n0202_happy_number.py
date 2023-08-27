import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/happy-number
    difficulty: easy
    """

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            tmp = 0
            while n > 0:
                n, last = divmod(n, 10)
                tmp += last ** 2
            n = tmp

        return True


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [19],
            # expected
            True,
        )
        yield (
            # params
            [2],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.isHappy(*params))


if __name__ == '__main__':
    unittest.main()
