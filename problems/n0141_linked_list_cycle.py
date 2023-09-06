import unittest

from ds.ListNode import ListNode
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle/
    difficulty: easy
    """

    def hasCycle(self, head: ListNode | None) -> bool:
        return self.floyd(head)
        # return self.iteration(head)

    def floyd(self, head: ListNode | None) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def iteration(self, head: ListNode | None) -> bool:
        if not head:
            return False

        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        lst = ListNode.from_list([3, 2, 0, -4])
        lst.nth(3).next = lst.next
        yield (
            # params
            [lst],
            # expected
            True,
        )
        lst = ListNode.from_list([1, 2])
        lst.nth(1).next = lst
        yield (
            # params
            [lst],
            # expected
            True,
        )
        yield (
            # params
            [ListNode.from_list([1])],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.hasCycle(*params))


if __name__ == '__main__':
    unittest.main()
