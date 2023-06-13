import unittest
from collections import defaultdict

from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/group-anagrams/
    difficulty: medium
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: dict[tuple[str], list[str]] = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            result[key].append(word)

        return list(result.values())


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [["eat", "tea", "tan", "ate", "nat", "bat"]],
            # expected
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
        )
        yield (
            # params
            [["a"]],
            # expected
            [["a"]],
        )
        yield (
            # params
            [[""]],
            # expected
            [[""]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.groupAnagrams(*params))


if __name__ == '__main__':
    unittest.main()
