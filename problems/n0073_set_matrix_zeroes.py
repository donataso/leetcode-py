import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/set-matrix-zeroes
    difficulty: medium
    """

    @staticmethod
    def setZeroes(matrix: list[list[int]]) -> None:
        """
        Worst case scenario O(m) additional space, the problem asked for O(1)
        """

        clear_columns = set()

        for idx_row, row in enumerate(matrix):
            new_row = None
            for idx_column, value in enumerate(row):
                if value == 0:
                    clear_columns.add(idx_column)
                    matrix[idx_row] = [0] * len(row) if new_row is None else new_row

            if new_row:
                matrix[idx_row] = [0] * len(row)

        if not clear_columns:
            return

        for idx_row, row in enumerate(matrix):
            for idx_column in clear_columns:
                matrix[idx_row][idx_column] = 0

    @staticmethod
    def setZeroesBetter(matrix: list[list[int]]):
        """
        O(1) additional space, got the idea from the official solution
        """
        m = len(matrix)
        n = len(matrix[0])

        # matrix[0][0] will be used to track row, gotta track the first column separately
        clear_first_col = False

        for idx_row in range(0, m):
            if (matrix[idx_row][0]) == 0:
                clear_first_col = True

            for idx_column in range(1, n):
                if matrix[idx_row][idx_column] == 0:
                    matrix[idx_row][0] = 0
                    matrix[0][idx_column] = 0

        # do not change the first row/column
        for idx_row in range(1, m):
            for idx_column in range(1, n):
                if not matrix[idx_row][0] or not matrix[0][idx_column]:
                    matrix[idx_row][idx_column] = 0

        # fix the first row
        if matrix[0][0] == 0:
            matrix[0] = [0] * n

        # fix the first column
        if clear_first_col:
            for idx_row in range(m):
                matrix[idx_row][0] = 0


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        )
        yield (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        )
        yield (
            [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]],
            [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        )

    @data_provider(dataprovider)
    def test_solution(self, matrix, expected):
        Solution.setZeroes(matrix)
        self.assertEqual(expected, matrix)


if __name__ == '__main__':
    unittest.main()
