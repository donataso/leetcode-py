import unittest

from unittest_data_provider import data_provider  # type: ignore

from ds.ListNode import ListNode


class Solution:
    """
    https://leetcode.com/problems/add-two-numbers
    difficulty: medium
    """

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = ListNode(0)
        cur_node = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            sum = val1 + val2 + carry
            carry = sum // 10
            cur_node.next = ListNode(sum % 10)
            cur_node = cur_node.next

        return result.next


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [ListNode.from_list([2, 4, 3]), ListNode.from_list([5, 6, 4])],
            # expected
            ListNode.from_list([7, 0, 8]),
        )
        yield (
            # params
            [ListNode.from_list([0]), ListNode.from_list([0])],
            # expected
            ListNode.from_list([0]),
        )
        yield (
            # params
            [ListNode.from_list([9, 9, 9, 9, 9, 9, 9]), ListNode.from_list([9, 9, 9, 9])],
            # expected
            ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1]),
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertTrue(solution.addTwoNumbers(*params).equals(expected))


if __name__ == '__main__':
    unittest.main()
