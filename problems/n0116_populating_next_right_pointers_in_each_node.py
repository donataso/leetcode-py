import unittest
from unittest_data_provider import data_provider  # type: ignore

from ds.TreeNode import TreeNode


class Node(TreeNode):
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        """
        :param left: Node | None
        :param right: Node | None
        :param next: Node | None
        """
        super().__init__(val, left, right)
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node
    difficulty: medium
    """

    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return None

        return self.recursive(root)
        # return self.bfs(root)
        # return self.better(root)

    def recursive(self, node: Node | None) -> Node | None:
        if not node or not node.left:
            return node

        node.left.next = node.right
        if node.next:
            node.right.next = node.next.left

        self.recursive(node.left)
        self.recursive(node.right)

        return node

    def better(self, root: Node) -> Node:
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root

    def bfs(self, root: Node) -> Node:
        """
        This is not O(1) space, but at least I can write it quickly
        """
        queue: list[Node] = [root]
        while queue:
            previous_node = None
            for i in range(len(queue)):
                node = queue.pop(0)
                node.next = previous_node
                previous_node = node

                if node.right:  # as this is a perfect binary tree, checking only one child is enough
                    queue.append(node.right)
                    queue.append(node.left)

        return root


class SolutionTestCase(unittest.TestCase):
    """
    This test does not test the actual problem, it just ensures that there are no errors during parsing
    """
    @staticmethod
    def dataprovider():
        yield (
            # params
            [Node.from_list([1, 2, 3, 4, 5, 6, 7], cls=Node)],
            # expected
            Node.from_list([1, 2, 3, 4, 5, 6, 7], cls=Node),
        )
        yield (
            # params
            [None],
            # expected
            [],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        if expected:
            self.assertTrue(solution.connect(*params).equals(expected))
        else:
            self.assertIsNone(solution.connect(*params))


if __name__ == '__main__':
    unittest.main()
