import unittest

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/redundant-connection
    difficulty: medium
    """

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu = DSU(1001)
        for edge in edges:
            if not dsu.union(*edge):
                return edge

        return []


class DSU:
    """
    Good explanation:
    https://cp-algorithms.com/data_structures/disjoint_set_union.html
    """
    def __init__(self, length: int):
        self.parents = list(range(length))
        self.ranks = [0] * length

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            # path compression
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        # representatives (or leaders) are the top level parents
        x_repr, y_repr = self.find(x), self.find(y)

        if x_repr == y_repr:
            return False

        if self.ranks[x_repr] == self.ranks[y_repr]:
            self.ranks[x_repr] += 1
        elif self.ranks[x_repr] < self.ranks[y_repr]:
            x_repr, y_repr = y_repr, x_repr

        self.parents[y_repr] = x_repr

        return True


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1, 2], [1, 3], [2, 3]]],
            # expected
            [2, 3],
        )
        yield (
            # params
            [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]],
            # expected
            [1, 4],
        )
        yield (
            # params
            [[[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]],
            # expected
            [4, 10],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findRedundantConnection(*params))


if __name__ == '__main__':
    unittest.main()
