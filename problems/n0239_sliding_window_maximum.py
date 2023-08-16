import unittest
from collections import deque

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/sliding-window-maximum/
    difficulty: hard
    """

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        length = len(nums)
        if k == length:
            return [max(nums)]
        if k == 1:
            return nums

        result: list[int] = []
        q: deque[int] = deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:  # keep the queue descending
                q.pop()
            q.append(i)

        result.append(nums[q[0]])

        for i in range(k, length):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:  # keep the queue descending
                q.pop()

            q.append(i)
            result.append(nums[q[0]])

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[7, 2, 4], 2],
            # expected
            [7, 4],
        )
        yield (
            # params
            [[1, 3, -1, -3, 5, 3, 6, 7], 3],
            # expected
            [3, 3, 5, 5, 6, 7],
        )
        yield (
            # params
            [[1], 1],
            # expected
            [1],
        )
        

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.maxSlidingWindow(*params))


if __name__ == '__main__':
    unittest.main()
