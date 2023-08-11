import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-substring
    difficulty: medium
    """

    def longestPalindrome(self, s: str) -> str:
        return self.expandFromCenters(s)
        # return self.bruteforce(s)

    def expandFromCenters(self, s: str) -> str:
        """
        O(n^2)
        """
        strlen = len(s)
        if not strlen:
            return ""

        def expand(left: int, right: int) -> list[int]:
            while left >= 0 and right < strlen and s[left] == s[right]:
                left -= 1
                right += 1
            return [left + 1, right - 1]

        result: list[int] = [0, 0]
        max_length = 1

        for i in range(strlen):
            # check even length
            cur_range = expand(i, i + 1)
            cur_length = cur_range[1] - cur_range[0] + 1
            if cur_length > max_length:
                max_length = cur_length
                result = cur_range

            # check odd length
            cur_range = expand(i, i)
            cur_length = cur_range[1] - cur_range[0] + 1
            if cur_length > max_length:
                max_length = cur_length
                result = cur_range

            # a bit of optimization:
            # if half of our longest palindrome is longer than what's left in the string, we have the result
            if max_length // 2 > strlen - i:
                break

        return s[result[0]:result[1] + 1]

    def bruteforce(self, s: str) -> str:
        """
        O(n^3) :(
        but at least I thought of it myself :)
        """
        def isPalindrome(low: int, high: int) -> bool:
            while low < high:
                if s[low] != s[high - 1]:
                    return False
                low += 1
                high -= 1
            return True

        strlen = len(s)
        substrlen = strlen
        while substrlen > 0:
            for start in range(strlen - substrlen + 1):
                if isPalindrome(start, start + substrlen):
                    return s[start:start + substrlen]
            substrlen -= 1

        return ""


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ["babad"],
            # expected
            "bab",
        )
        yield (
            # params
            ["cbbd"],
            # expected
            "bb",
        )
        yield (
            # params
            ["ac"],
            # expected
            "a",
        )
        yield (
            # params
            ["bb"],
            # expected
            "bb",
        )
        yield (
            # params
            ["ababababa"],
            # expected
            "ababababa",
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.longestPalindrome(*params))


if __name__ == '__main__':
    unittest.main()
