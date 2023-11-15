import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
    difficulty: medium
    """

    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False
        result = 0
        for i in range(len(colors) - 2):
            if colors[i] == colors[i + 1] == colors[i + 2]:
                result += 1 if colors[i] == 'A' else -1
        return result > 0

        # alice_plays = sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors))
        # bob_plays = sum(len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))

        # return alice_plays > bob_plays


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['AAABABB'],
            # expected
            True,
        )
        yield (
            # params
            ['AA'],
            # expected
            False,
        )
        yield (
            # params
            ['ABBBBBBBAAA'],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.winnerOfGame(*params))


if __name__ == '__main__':
    unittest.main()
