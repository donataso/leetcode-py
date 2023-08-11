import unittest
from helper.unittest_data_provider import data_provider

from ds.TreeNode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    difficulty: medium
    """

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:inorder_idx])
        root.right = self.buildTree(preorder, inorder[inorder_idx + 1:])

        return root


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
            # expected
            TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
        )
        yield (
            # params
            [[-1], [-1]],
            # expected
            TreeNode(-1),
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertTrue(solution.buildTree(*params).equals(expected))


if __name__ == '__main__':
    unittest.main()
