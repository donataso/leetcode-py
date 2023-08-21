import unittest

from helper.unittest_data_provider import data_provider


class Vector2D:
    """
    https://leetcode.com/problems/flatten-2d-vector
    difficulty: medium
    """

    def __init__(self, vec: list[list[int]]):
        """
        Of course, this solution is a bad one, but it's hard to work on something when a given test case is invalid.
        """
        self.items: list[int] = []

        def flatten(x: list | int):
            if type(x) == int:
                self.items.append(x)
                return
            [flatten(n) for n in x]  # type: ignore

        flatten(vec)
        self.current = 0

    def next(self) -> int:
        val = self.items[self.current]
        self.current += 1
        return val

    def hasNext(self) -> bool:
        return self.current < len(self.items)


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [
                ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"],
                [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
            ],
            # expected
            [None, 1, 2, 3, True, True, 4, False],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        vector = Vector2D(params[1])
        for i in range(1, len(params[0])):
            fn = getattr(vector, params[0][i])
            self.assertEqual(expected[i], fn())


if __name__ == '__main__':
    unittest.main()
