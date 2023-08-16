import unittest
from typing import TypeAlias

from helper.unittest_data_provider import data_provider

Point: TypeAlias = tuple[int, int]


class Solution:
    """
    https://leetcode.com/problems/word-search
    difficulty: medium
    """

    def exist(self, board: list[list[str]], word: str) -> bool:
        return self.dfs(board, word)

    def dfs(self, board: list[list[str]], full_word: str) -> bool:
        if not board:
            return False

        m = len(board)
        n = len(board[0])

        if m * n < len(full_word):
            return False

        def recurse(word: str, start: Point) -> bool:
            if not word:
                return True
            if start[0] < 0 or start[0] == m or start[1] < 0 or start[1] == n or board[start[0]][start[1]] != word[0]:
                return False

            board[start[0]][start[1]] = ''
            for direction in ((0, 1), (-1, 0), (0, -1), (1, 0)):
                if recurse(word[1:], (start[0] + direction[0], start[1] + direction[1])):
                    return True
            board[start[0]][start[1]] = word[0]

            return False

        # optimization first:
        # count how many starting or ending letters are there on the board.
        # at the same time, save starting positions to iterate on later.
        # if there are fewer ending letters than starting ones, reverse the word.
        first_c = full_word[0]
        last_c = full_word[-1]
        start_positions: dict[str, list[Point]] = {
            first_c: [],
            last_c: [],
        }
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in start_positions:
                    start_positions[c].append((i, j))

        if len(start_positions[last_c]) < len(start_positions[first_c]):
            full_word = full_word[::-1]
            positions = start_positions[last_c]
        else:
            positions = start_positions[first_c]

        for pos in positions:
            if recurse(full_word, pos):
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"],
            # expected
            True,
        )
        yield (
            # params
            [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
            # expected
            True,
        )
        yield (
            # params
            [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
            # expected
            True,
        )
        yield (
            # params
            [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
            # expected
            True,
        )
        yield (
            # params
            [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.exist(*params))


if __name__ == '__main__':
    unittest.main()
