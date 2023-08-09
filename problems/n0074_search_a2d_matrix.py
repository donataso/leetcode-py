import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/search-a-2d-matrix/
    difficulty: medium
    """

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return self.two_bs(matrix, target)
        # return self.one_bs(matrix, target)

    def two_bs(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        # find the row
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (high - low) // 2 + low

            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][0]:
                if len(matrix) == mid + 1:  # the last row
                    break
                if target == matrix[mid + 1][0]:
                    return True
                if target > matrix[mid + 1][0]:
                    low = mid + 1
                else:
                    break

        if high == -1:
            return False

        # search inside the row
        row_idx = mid
        low = 0
        high = len(matrix[low]) - 1
        while low <= high:
            mid = (high - low) // 2 + low

            if target == matrix[row_idx][mid]:
                return True
            if target < matrix[row_idx][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def one_bs(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (high - low) // 2 + low
            num = matrix[mid // n][mid % n]
            if target < num:
                high = mid - 1
            elif target > num:
                low = mid + 1
            else:
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11],
            # expected
            True,
        )
        yield (
            # params
            [[[10]], 2],
            # expected
            False,
        )
        yield (
            # params
            [[[1, 3]], 3],
            # expected
            True,
        )
        yield (
            # params
            [[[1]], 2],
            # expected
            False,
        )
        yield (
            # params
            [[[1]], 1],
            # expected
            True,
        )
        yield (
            # params
            [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
            # expected
            True,
        )
        yield (
            # params
            [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.searchMatrix(*params))


if __name__ == '__main__':
    unittest.main()
