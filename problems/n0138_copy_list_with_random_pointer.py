import unittest

from ds.ListNode import ListNode
from helper.unittest_data_provider import data_provider


class Node(ListNode):
    def __init__(self, val: int = 0, next=None, random=None):
        """
        :param next: ListNode | None
        :param random: ListNode | None
        """
        self.random: ListNode | None = random
        super().__init__(val, next)

class Solution:
    """
    https://leetcode.com/problems/copy-list-with-random-pointer/
    difficulty: medium
    """

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visited = {}

    def copyRandomList(self, head: Node | None) -> Node | None:
        return self.recursive_graph_traversal(head)
        # return self.lots_of_memory(head)

    def lots_of_memory(self, head: Node | None) -> Node | None:
        if not head:
            return None

        idx_original: list[Node] = []
        idx_copy: list[Node] = []
        curr = head
        while curr:
            new = Node(curr.val)

            if idx_copy:
                idx_copy[-1].next = new

            idx_copy.append(new)
            idx_original.append(curr)

            curr = curr.next

        for i, node in enumerate(idx_original):
            if not node.random:
                continue

            idx_copy[i].random = idx_copy[idx_original.index(node.random)]

        return idx_copy[0]

    def recursive_graph_traversal(self, head: Node | None) -> Node | None:
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        n5 = Node(1)
        n4 = Node(10, next=n5)
        n3 = Node(11, next=n4)
        n2 = Node(13, next=n3)
        n1 = Node(7, next=n2)

        n2.random = n1
        n3.random = n5
        n4.random = n4
        n5.random = n1

        yield (
            # params
            [n1],
            # expected
            n1,
        )

        yield (
            # params
            [None],
            # expected
            None,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected: Node | None):
        solution = Solution()
        self.assertEqual(str(expected), str(solution.copyRandomList(*params)))


if __name__ == '__main__':
    unittest.main()
