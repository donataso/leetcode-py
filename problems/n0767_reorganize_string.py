import collections
import heapq
import itertools
import unittest
from collections import deque

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/reorganize-string/
    difficulty: medium
    """

    def reorganizeString(self, s: str) -> str:
        return self.proper(s)
        # return self.crazy(s)

    def proper(self, s: str) -> str:
        result = ''
        counts = [(-n, c) for c, n in collections.Counter(s).items()]
        heapq.heapify(counts)
        while counts:
            n1, c1 = heapq.heappop(counts)
            if not result or result[-1] != c1:
                result += c1
                if n1 + 1 < 0:
                    heapq.heappush(counts, (n1 + 1, c1))
                continue

            if not counts:
                return  ''

            n2, c2 = heapq.heappop(counts)
            result += c2
            if n2 + 1 < 0:
                heapq.heappush(counts, (n2 + 1, c2))

            heapq.heappush(counts, (n1, c1))

        return result

    def crazy(self, s: str) -> str:
        groups = {c: len(list(g)) for c, g in itertools.groupby(sorted([*s]))}
        result = ''
        while groups:
            groups = dict(sorted(groups.items(), key=lambda x: x[1], reverse=True))
            keys = groups.keys()
            char = result[-1] if result else None
            for c in keys:
                if c != char and c in groups:
                    char = c
                    break

            if char is None:
                break

            if result and result[-1] == char:
                return ''

            result += char

            groups[char] -= 1
            if groups[char] == 0:
                groups.pop(char)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['aabbcc'],
            # expected
            'abcabc',
        )
        yield (
            # params
            ['vvvlo'],
            # expected
            'vlvov',
        )
        yield (
            # params
            ['aab'],
            # expected
            'aba',
        )
        yield (
            # params
            ['aaab'],
            # expected
            '',
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.reorganizeString(*params))


if __name__ == '__main__':
    unittest.main()
