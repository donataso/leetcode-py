import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/repeated-substring-pattern/
    difficulty: easy
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.clever(s)
        # return self.simple(s)

    def clever(self, s: str) -> bool:
        t = s + s
        if s in t[1:-1]:
            return True
        return False

    def simple(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i != 0:
                continue
            if s[:i] * (length // i) == s:
                return True
        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['abab'],
            # expected
            True,
        )
        yield (
            # params
            ['aba'],
            # expected
            False,
        )
        yield (
            # params
            ['abcabcabcabc'],
            # expected
            True,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.repeatedSubstringPattern(*params))


if __name__ == '__main__':
    unittest.main()
