import unittest
from collections import deque

from helper.unittest_data_provider import data_provider


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    """
    https://leetcode.com/problems/flatten-nested-list-iterator
    difficulty: medium
    """

    def __init__(self, nested_list: [NestedInteger]):
        self.q = deque(nested_list)
        self.next_val = self._get_next()

    def next(self) -> int:
        next_val = self.next_val
        self.next_val = self._get_next()

        return next_val

    def _get_next(self) -> int | None:
        while self.q:
            ni = self.q.popleft()
            if ni.isInteger():
                return ni.getInteger()
            for i in reversed(ni.getList()):
                if i.isInteger() or i.getList():
                    self.q.appendleft(i)

        return None

    def hasNext(self) -> bool:
        return self.next_val is not None


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [],
            # expected
            [],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.solve(*params))


if __name__ == '__main__':
    unittest.main()
