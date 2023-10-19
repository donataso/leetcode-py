import unittest

from ds.ListNode import ListNode
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/split-linked-list-in-parts
    difficulty: medium
    """

    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        if not head:
            return [None] * k

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        part_len, extra = divmod(length, k)
        result: list[ListNode | None] = [None] * k
        for i in range(k):
            if not head:
                break

            result[i] = head
            prev = head
            for _ in range(part_len + (1 if extra > i else 0)):
                if not head:
                    break
                prev = head
                head = head.next

            prev.next = None

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [None, 2],
            # expected
            [None, None],
        )
        yield (
            # params
            [ListNode.from_list([1, 2, 3]), 5],
            # expected
            [[1], [2], [3], None, None],
        )
        yield (
            # params
            [ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3],
            # expected
            [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        actual = solution.splitListToParts(*params)
        self.assertEqual(expected, [item.to_list() if item else item for item in actual])


if __name__ == '__main__':
    unittest.main()
