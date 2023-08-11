import unittest
from helper.unittest_data_provider import data_provider

from ds.ListNode import ListNode


class Solution:
    """
    https://leetcode.com/problems/intersection-of-two-linked-lists
    difficulty: easy
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # return self.mySolution(headA, headB)
        return self.officialSolution(headA, headB)


    def officialSolution(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA

    def mySolution(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        len_a = self.getListLength(headA)
        len_b = self.getListLength(headB)

        while headA and headB and len_a != len_b:
            if len_a > len_b:
                headA = headA.next
                len_a -= 1
            elif len_b > len_a:
                headB = headB.next
                len_b -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getListLength(self, lst: ListNode | None) -> int:
        cnt = 0
        while lst:
            cnt += 1
            lst = lst.next

        return cnt

class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        l1 = ListNode.from_list([4, 1])
        l2 = ListNode.from_list([5, 6, 1])
        same = ListNode.from_list([8, 4, 5])
        l1.next = same
        l2.next = same
        yield (
            # params
            [l1, l2],
            # expected
            same,
        )

        l1 = ListNode.from_list([1,9,1])
        l2 = ListNode.from_list([3])
        same = ListNode.from_list([2,4])
        l1.next = same
        l2.next = same
        yield (
            # params
            [l1, l2],
            # expected
            same,
        )
        yield (
            # params
            [
                ListNode.from_list([2, 6, 4]),
                ListNode.from_list([1, 5]),
            ],
            # expected
            None,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.getIntersectionNode(*params))


if __name__ == '__main__':
    unittest.main()
