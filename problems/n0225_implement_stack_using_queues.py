import unittest
from collections import deque

from helper.unittest_data_provider import data_provider


class MyStack:
    """
    https://leetcode.com/problems/implement-stack-using-queues
    difficulty: easy
    """

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # it's so weird to do something in such an inefficient way...
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [
                ["MyStack", "push", "push", "top", "pop", "empty"],
                [[], [1], [2], [], [], []],
            ],
            # expected
            [None, None, None, 2, 2, False],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        stack = MyStack()
        for i in range(1, len(params[0])):
            fn = getattr(stack, params[0][i])
            self.assertEqual(expected[i], fn(*params[1][i]))


if __name__ == '__main__':
    unittest.main()
