import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    url
    difficulty: easy|medium|hard
    """

    def solve(self, *args):
        pass


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [],
            # expected
            [],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.solve(*params))


if __name__ == '__main__':
    unittest.main()
