class ListNode:
    def __init__(self, val: int = 0, next=None):
        """
        :param next: ListNode | None
        """
        self.val: int = val
        self.next: ListNode | None = next

    def equals(self, other):
        """
        :param other: ListNode | None
        """
        return self.val == other.val and (
            (self.next and other.next and self.next.equals(other.next)) or
            (self.next is None and other.next is None)
        )

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return str(self.to_list())

    @staticmethod
    def from_list(input: list[int]):
        """
        :return: ListNode | None
        """
        if not input:
            return None

        return ListNode(input.pop(0), ListNode.from_list(input))

    def to_list(self) -> list[int]:
        result: list[int] = []
        head: ListNode | None = self
        while head:
            result.append(head.val)
            head = head.next

        return result

    def nth(self, n: int):
        """
        :return: ListNode | None
        """
        head: ListNode | None = self
        while head and n > 0:
            head = head.next
            n -= 1

        return head
