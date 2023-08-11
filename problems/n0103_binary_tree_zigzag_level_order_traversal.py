import unittest

from helper.unittest_data_provider import data_provider

from ds.TreeNode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
    difficulty: medium
    """

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        result: list[list[int]] = []
        queue: list = [[0, root]]

        while queue:
            level, node = queue.pop(0)

            if not node:
                continue

            # sure, I could use collections.defaultdict(), but I don't want to
            if level == len(result):
                result.append([])

            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)

            level += 1
            queue.append([level, node.left])
            queue.append([level, node.right])

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [TreeNode.from_list([1, 2, 3, 4, None, None, 5])],
            # expected
            [[1], [3, 2], [4, 5]],
        )
        yield (
            # params
            [TreeNode.from_list([3, 9, 20, None, None, 15, 7])],
            # expected
            [[3], [20, 9], [15, 7]],
        )
        yield (
            # params
            [TreeNode(1)],
            # expected
            [[1]],
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
        self.assertEqual(expected, solution.zigzagLevelOrder(*params))


if __name__ == '__main__':
    unittest.main()
