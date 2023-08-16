import unittest

from ds.ListNode import ListNode
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/partition-list
    difficulty: medium
    """

    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head:
            return head

        left = ListNode()
        left_head = left
        right = ListNode()
        right_head = right

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        left.next = right_head.next
        right.next = None

        return left_head.next


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [ListNode.from_list([1, 4, 3, 0, 2, 5, 2]), 3],
            # expected
            ListNode.from_list([1, 0, 2, 2, 4, 3, 5]),
        )
        yield (
            # params
            [ListNode.from_list([1, 4, 3, 2, 5, 2]), 3],
            # expected
            ListNode.from_list([1, 2, 2, 4, 3, 5]),
        )
        yield (
            # params
            [ListNode.from_list([2, 1]), 2],
            # expected
            ListNode.from_list([1, 2]),
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertTrue(solution.partition(*params).equals(expected))


if __name__ == '__main__':
    unittest.main()
