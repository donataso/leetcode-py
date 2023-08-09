import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/diagonal-traverse/
    difficulty: medium
    """

    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        return self.easier_solution_adapted_from_1224_problem(mat)
        # return self.my_original_solution(mat)

    def easier_solution_adapted_from_1224_problem(self, mat: list[list[int]]) -> list[int]:
        result: list[list[int]] = []

        for m in range(len(mat)):
            for n in range(len(mat[m])):
                if m + n == len(result):
                    result.append([])

                if (m + n) % 2 == 1:
                    result[m + n].append(mat[m][n])
                else:
                    result[m + n].insert(0, mat[m][n])

        return [num for i, row in enumerate(result) for num in row]

    def my_original_solution(self, mat: list[list[int]]) -> list[int]:
        n_rows = len(mat)
        n_cols = len(mat[0])
        result: list[int] = []

        for d in range(n_rows + n_cols - 1):
            diag: list[int] = []
            m = min(d, n_rows - 1)  # once we reach the last row, we stay at it
            start_col = max(0, d - n_rows + 1)  # once we reach the last row, our starting column shifts right
            for n in range(start_col, n_cols):
                if m < 0:
                    break
                diag.append(mat[m][n])
                m -= 1

            if d % 2 == 1:
                diag.reverse()
            result.extend(diag)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            # expected
            [1, 2, 4, 7, 5, 3, 6, 8, 9],
        )
        yield (
            # params
            [[[1, 2], [3, 4]]],
            # expected
            [1, 2, 3, 4],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findDiagonalOrder(*params))


if __name__ == '__main__':
    unittest.main()
