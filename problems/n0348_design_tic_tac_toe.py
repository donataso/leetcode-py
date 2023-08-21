import unittest
from helper.unittest_data_provider import data_provider


class TicTacToe:
    """
    https://leetcode.com/problems/design-tic-tac-toe
    difficulty: medium
    """

    def __init__(self, n: int):
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag1 = [0, 0]
        self.diag2 = [0, 0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][player - 1] += 1
        self.cols[col][player - 1] += 1
        if row == col:
            self.diag1[player - 1] += 1
        if row + col == self.n - 1:
            self.diag2[player - 1] += 1

        if self.rows[row][player - 1] == self.n:
            return player
        if self.cols[col][player - 1] == self.n:
            return player
        if self.diag1[player - 1] == self.n:
            return player
        if self.diag2[player - 1] == self.n:
            return player

        return 0


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [1, 1, 2], [2, 2, 1], [0, 2, 2], [0, 1, 1], [2, 0, 2]],
            ],
            # expected
            [None, 0, 0, 0, 0, 0, 2],
        )
        yield (
            # params
            [
                ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"],
                [[4], [0, 3, 1], [3, 3, 2], [3, 0, 1], [0, 0, 2], [2, 1, 1], [2, 2, 2], [1, 2, 1]],
            ],
            # expected
            [None, 0, 0, 0, 0, 0, 0, 1],
        )
        yield (
            # params
            [
                ["TicTacToe", "move", "move", "move"],
                [[2], [0, 0, 2], [0, 1, 1], [1, 1, 2]],
            ],
            # expected
            [None, 0, 0, 2],
        )
        yield (
            # params
            [
                ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]],
            ],
            # expected
            [None, 0, 0, 0, 0, 0, 0, 1],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        ttt = TicTacToe(params[1][0][0])
        for i in range(1, len(params[0])):
            fn = getattr(ttt, params[0][i])
            self.assertEqual(expected[i], fn(*params[1][i]))


if __name__ == '__main__':
    unittest.main()
