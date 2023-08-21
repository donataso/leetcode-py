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
    def from_list(input: list[int], cls=None):
        cls = cls if cls else TreeNode

        nodes = [cls(val) if val is not None else None for val in input]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
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
