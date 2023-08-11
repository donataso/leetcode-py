import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/number-of-islands
    difficulty: medium
    """

    LAND = '1'
    WATER = '0'

    NEIGHBOURS = [
        [0, -1],  # left
        [0, 1],  # right
        [-1, 0],  # up
        [1, 0],  # down
    ]

    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_islands = 0
        count_row = len(grid)
        count_col = len(grid[0])

        for m in range(count_row):
            for n in range(count_col):
                if grid[m][n] == self.LAND:
                    num_islands += 1
                    # self.removeIslandBfsIterative(grid, m, n)
                    self.removeIslandRecursive(grid, m, n)

        return num_islands

    def removeIslandRecursive(self, grid: list[list[str]], m: int, n: int):
        if m < 0 or m >= len(grid) \
                or n < 0 or n >= len(grid[m]) \
                or grid[m][n] != self.LAND:
            return

        grid[m][n] = self.WATER

        self.removeIslandRecursive(grid, m, n - 1)
        self.removeIslandRecursive(grid, m, n + 1)
        self.removeIslandRecursive(grid, m - 1, n)
        self.removeIslandRecursive(grid, m + 1, n)

    def removeIslandBfsIterative(self, grid: list[list[str]], m: int, n: int) -> None:
        """
        Remove island using BFS
        """
        queue: list[tuple[int, int]] = [(m, n)]
        grid[m][n] = self.WATER
        while queue:
            m, n = queue.pop(0)
            # enqueue neighbours that are land
            for delta in self.NEIGHBOURS:
                m_neighbour = m + delta[0]
                n_neighbour = n + delta[1]

                if 0 <= m_neighbour < len(grid) \
                        and 0 <= n_neighbour < len(grid[m_neighbour]) \
                        and grid[m_neighbour][n_neighbour] == self.LAND:
                    queue.append((m_neighbour, n_neighbour))

                    # clear the queued cell
                    grid[m_neighbour][n_neighbour] = self.WATER


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]],
            # expected
            1,
        )
        yield (
            # params
            [[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]],
            # expected
            3,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.numIslands(*params))


if __name__ == '__main__':
    unittest.main()
