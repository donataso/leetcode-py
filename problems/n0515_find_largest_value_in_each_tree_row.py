import unittest

from ds.TreeNode import TreeNode
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/find-largest-value-in-each-tree-row
    difficulty: medium
    """

    def largestValues(self, root: TreeNode | None) -> list[int]:
        result = []

        def recurse(node: TreeNode | None, level: int) -> None:
            if not node:
                return

            if len(result) <= level:
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)

            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root, 0)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [TreeNode.from_list([1, 3, 2, 5, 3, None, 9])],
            # expected
            [1, 3, 9],
        )
        yield (
            # params
            [TreeNode.from_list([1, 2, 3])],
            # expected
            [1, 3],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.largestValues(*params))


if __name__ == '__main__':
    unittest.main()
