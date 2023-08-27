import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/text-justification
    difficulty: hard
    """

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def add_spaces(row: list[str], row_length: int, last: bool) -> str:
            if last:
                return ' '.join(row) + ' ' * (maxWidth - row_length - len(row) + 1)

            justified = ''
            word_cnt = len(row)
            spaces = maxWidth - row_length
            spacing = 0 if word_cnt == 1 else spaces // (word_cnt - 1)
            extra_spaces = spaces - spacing * (word_cnt - 1)
            for idx, word in enumerate(row):
                if idx + 1 == len(row):
                    return justified + word + ' ' * extra_spaces

                justified += word + ' ' * (spacing + 1 if extra_spaces > 0 else spacing)
                extra_spaces -= 1

            return justified

        result: list[str] = []
        row = []
        row_length = 0
        for word in words:
            if row_length + len(word) + len(row) <= maxWidth:
                row.append(word)
                row_length += len(word)
                continue

            result.append(add_spaces(row, row_length, False))
            row = [word]
            row_length = len(word)

        if row:
            result.append(add_spaces(row, row_length, True))

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [["This", "is", "an", "example", "of", "text", "justification."], 16],
            # expected
            [
                "This    is    an",
                "example  of text",
                "justification.  "
            ],
        )
        yield (
            # params
            [["What", "must", "be", "acknowledgment", "shall", "be"], 16],
            # expected
            [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ],
        )
        yield (
            # params
            [["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
              "Art", "is", "everything", "else", "we", "do"], 20],
            # expected
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
            ],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.fullJustify(*params))


if __name__ == '__main__':
    unittest.main()
