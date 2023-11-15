import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank
    difficulty: medium
    """

    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        return max(
            max(left) if left else 0,
            n - min(right) if right else 0,
        )


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [4, [4, 3], [0, 1]],
            # expected
            4,
        )
        yield (
            # params
            [7, [], [0, 1, 2, 3, 4, 5, 6, 7]],
            # expected
            7,
        )
        yield (
            # params
            [7, [0, 1, 2, 3, 4, 5, 6, 7], []],
            # expected
            7,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.getLastMoment(*params))


if __name__ == '__main__':
    unittest.main()
