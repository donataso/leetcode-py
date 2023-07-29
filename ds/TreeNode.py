from typing import List, Any


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        """
        :param left: TreeNode | None
        :param right: TreeNode | None
        """
        self.val = val
        self.left = left
        self.right = right

    def equals(self, other):
        """
        :param other: TreeNode | None
        """
        return self.to_list() == other.to_list()

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return str(self.to_list())

    @staticmethod
    def from_list(input: list[int], idx: int = 0, cls=None):
        """
        This function does not support null path terminator, as in [1,null,2,3] binary tree.
        :return: TreeNode | None
        """
        cls = cls if cls else TreeNode
        root = None

        if idx < len(input) and input[idx] is not None:
            root = cls(input[idx] if input[idx] is not None else 0)

            root.left = cls.from_list(input, 2 * idx + 1, cls=cls)
            root.right = cls.from_list(input, 2 * idx + 2, cls=cls)

        return root

    def to_list(self) -> list[list[int]] | None:
        result = []
        level_values: list[int] = []
        previous_level = 0
        queue = [[self, 0]]
        while queue:
            node: TreeNode | None
            level: int
            [node, level] = queue.pop(0)

            if previous_level != level:
                previous_level = level
                result.append(level_values)
                level_values = []

            if node:
                level_values.append(node.val)
            else:
                continue

            queue.append([node.left, level + 1])
            queue.append([node.right, level + 2])

        return result if result else None
