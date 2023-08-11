import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters
    difficulty: medium
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length: int = 0
        substr: dict[str, int] = {}
        start: int = 0
        for idx in range(len(s)):
            c = s[idx]
            if c in substr:
                start = max(substr[s[idx]], start)

            max_length = max(max_length, idx - start + 1)
            substr[c] = idx + 1

        return max_length

    def lengthOfLongestSubstringABitWorse(self, s: str) -> int:
        max_length: int = 0
        substr: list[str] = []
        for c in s:
            if c in substr:
                substr = substr[substr.index(c) + 1:]
            substr.append(c)
            max_length = max(max_length, len(substr))

        return max_length


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['abcabcbb'],
            # expected
            3,
        )
        yield (
            # params
            ['bbb'],
            # expected
            1,
        )
        yield (
            # params
            ['pwwkew'],
            # expected
            3,
        )
        yield (
            # params
            ['aabaab!bb'],
            # expected
            3,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.lengthOfLongestSubstring(*params))


if __name__ == '__main__':
    unittest.main()
