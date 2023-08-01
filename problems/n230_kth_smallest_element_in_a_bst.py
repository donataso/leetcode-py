import unittest
from unittest_data_provider import data_provider  # type: ignore

from ds.TreeNode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/kth-smallest-element-in-a-bst
    difficulty: medium
    """

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # return self.inorder_iterative_dfs(root, k)
        return self.inorder_recursive(root, [k])

    def inorder_recursive(self, node: TreeNode | None, k: list[int]) -> int | None:
        """
        Here I'm passing k in as [k] to pass it by reference
        """
        if node is None:
            return None

        left = self.inorder_recursive(node.left, k)
        if left is not None:
            return left

        if k[0] == 1:
            return node.val
        k[0] -= 1

        return self.inorder_recursive(node.right, k)

    def inorder_iterative_dfs(self, node: TreeNode | None, k: int) -> int:
        stack: list[TreeNode] = []

        while k:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                if k == 1:
                    return node.val
                k -= 1
                node = node.right
            else:
                break

        return -1


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [TreeNode.from_list([3, 1, 4, None, 2]), 1],
            # expected
            1,
        )
        yield (
            # params
            [TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1]), 3],
            # expected
            3,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.kthSmallest(*params))


if __name__ == '__main__':
    unittest.main()
