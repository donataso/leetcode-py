import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/majority-element
    difficulty: easy
    """

    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        score = 0
        for num in nums:
            if not score:
                candidate = num
            score += 1 if candidate == num else -1

        return candidate


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[3, 2, 3]],
            # expected
            3,
        )
        yield (
            # params
            [[2, 2, 1, 1, 1, 2, 2]],
            # expected
            2,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.majorityElement(*params))


if __name__ == '__main__':
    unittest.main()
