import itertools
import re
import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/count-and-say/
    difficulty: medium
    """

    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(n - 1):
            result = self.expandItertools(result)
            # result = self.expandRe(result)
            # result = self.expandManual(result)

        return result

    def expandRe(self, s: str) -> str:
        # m.group(0) is the entire match, m.group(1) is its first digit
        return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

    def expandItertools(self, s: str) -> str:
        res: list[str] = []
        for k, g in itertools.groupby(s):
            res.append(str(len(list(g))) + k)

        return ''.join(res)

    def expandManual(self, s: str) -> str:
        result = ''
        last_c = ''
        count = 0
        for c in s:
            if c == last_c:
                count += 1
            else:
                if last_c != '':
                    result += str(count) + last_c

                last_c = c
                count = 1

        result += str(count) + last_c

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [1],
            # expected
            "1",
        )
        yield (
            # params
            [4],
            # expected
            "1211",
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.countAndSay(*params))


if __name__ == '__main__':
    unittest.main()
