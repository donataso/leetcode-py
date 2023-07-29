import unittest
from unittest_data_provider import data_provider  # type: ignore

from ds.TreeNode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/binary-tree-inorder-traversal/
    difficulty: easy
    """

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.inorderRecursive(root)
        # return self.inorderIterative(root)

    def inorderIterative(self, root: TreeNode) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode] = []
        node = root

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                result.append(node.val)
                node = node.right
            else:
                break

        return result

    def inorderRecursive(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result: list[int] = []

        result.extend(self.inorderRecursive(root.left))
        result.append(root.val)
        result.extend(self.inorderRecursive(root.right))

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [TreeNode(1, right=TreeNode(2, left=TreeNode(3)))],
            # expected
            [1, 3, 2],
        )
        yield (
            # params
            [None],
            # expected
            [],
        )
        yield (
            # params
            [TreeNode(1)],
            # expected
            [1],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.inorderTraversal(*params))


if __name__ == '__main__':
    unittest.main()
