import unittest

from ds.ListNode import ListNode
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list-ii/
    difficulty: medium
    """

    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or not head.next or left == right:
            return head

        prev = None
        before_first = None
        first = None
        after_last = None
        last = None
        pos = 0
        curr = head
        while curr:
            pos += 1
            if pos < left:
                pass
            elif pos > right:
                break
            elif pos == left:
                first = curr
                before_first = prev
            elif pos == right:
                last = curr
                after_last = curr.next

            if pos > left:
                next = curr.next
                curr.next = prev

                prev = curr
                curr = next
                continue

            prev = curr
            curr = curr.next

        first.next = after_last
        if before_first:
            before_first.next = last
        else:
            head = last

        return head


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [ListNode.from_list([3, 5]), 1, 2],
            # expected
            [5, 3],
        )
        yield (
            # params
            [ListNode.from_list([1, 2, 3, 4, 5]), 2, 4],
            # expected
            [1, 4, 3, 2, 5],
        )
        yield (
            # params
            [ListNode.from_list([5]), 1, 1],
            # expected
            [5],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        head = solution.reverseBetween(*params)
        self.assertEqual(expected, head.to_list() if head else head)


if __name__ == '__main__':
    unittest.main()
