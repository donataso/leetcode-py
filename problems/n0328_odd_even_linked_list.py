import unittest
from helper.unittest_data_provider import data_provider

from ds.ListNode import ListNode


class Solution:
    """
    https://leetcode.com/problems/odd-even-linked-list/
    difficulty: medium
    """

    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # return self.officialHardToRead(head)
        return self.mineEasyToRead(head)

    def mineEasyToRead(self, head: ListNode | None) -> ListNode | None:
        odd_head = ListNode()
        even_head = ListNode()

        odd_cur = odd_head
        even_cur = even_head

        is_odd = True
        while head:
            if is_odd:
                odd_cur.next = head
                odd_cur = odd_cur.next
            else:
                even_cur.next = head
                even_cur = even_cur.next

            is_odd = not is_odd
            head = head.next

        even_cur.next = None
        odd_cur.next = even_head.next

        return odd_head.next

    def officialHardToRead(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [ListNode.from_list([1, 2, 3, 4, 5])],
            # expected
            ListNode.from_list([1, 3, 5, 2, 4]),
        )
        yield (
            # params
            [ListNode.from_list([2, 1, 3, 5, 6, 4, 7])],
            # expected
            ListNode.from_list([2, 3, 6, 7, 1, 5, 4]),
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertTrue(solution.oddEvenList(*params).equals(expected))


if __name__ == '__main__':
    unittest.main()
