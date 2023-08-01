import unittest
from unittest_data_provider import data_provider  # type: ignore

from ds.TreeNode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/inorder-successor-in-bst
    difficulty: medium
    """

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        return self.inorder_successor_even_smarter(root, p)
        # return self.inorder_successor_smarter(root, p)
        # return self.inorder_successor_iterative(root, p)
        # return self.inorder_successor_recursive(root, p, [False])

    def inorder_successor_even_smarter(self, node: TreeNode, p: TreeNode) -> TreeNode | None:
        successor = None
        while node:
            if node.val <= p.val:
                # successor on the right
                node = node.right
            else:
                # successor on the left
                successor = node
                node = node.left

        return successor

    def inorder_successor_smarter(self, node: TreeNode, p: TreeNode) -> TreeNode | None:
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            if leftmost:
                return leftmost

        return self.inorder_successor_recursive(node, p, [False])

    def inorder_successor_recursive(self, node: TreeNode, p: TreeNode, found: list[bool]) -> TreeNode | None:
        if not node:
            return None

        left = self.inorder_successor_recursive(node.left, p, found)
        if left:
            return left

        if found[0]:
            return node
        if node.val == p.val:
            found[0] = True

        return self.inorder_successor_recursive(node.right, p, found)

    def inorder_successor_iterative(self, node: TreeNode, p: TreeNode) -> TreeNode | None:
        stack: list[TreeNode] = []
        found = False
        while True:
            if node:
                stack.append(node)
                node = node.left
                if node and node.val < p.val:  # no need to go left anymore
                    node = node.right
            elif stack:
                node = stack.pop()
                if found:
                    return node
                if node.val == p.val:
                    found = True
                node = node.right
            else:
                break

        return None


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        tree = TreeNode.from_list([2, 1, 3])
        yield (
            # params
            [tree, TreeNode(1)],
            # expected
            tree,
        )
        yield (
            # params
            [TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1]), TreeNode(6)],
            # expected
            None,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.inorderSuccessor(*params))


if __name__ == '__main__':
    unittest.main()
