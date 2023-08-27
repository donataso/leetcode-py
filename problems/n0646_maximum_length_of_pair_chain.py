import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    url
    difficulty: easy|medium|hard
    """

    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr = -2000
        result = 0

        for pair in pairs:
            if pair[0] > curr:
                result += 1
                curr = pair[1]

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1,2],[2,3],[3,4]]],
            # expected
            2,
        )
        yield (
            # params
            [[[1,2],[7,8],[4,5]]],
            # expected
            3,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findLongestChain(*params))


if __name__ == '__main__':
    unittest.main()
