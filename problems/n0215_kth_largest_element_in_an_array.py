import heapq
import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/kth-largest-element-in-an-array
    difficulty: medium
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        # return self.count(nums, k)
        return self.heapq_k_size(nums, k)
        # return self.heapq_nlargest(nums, k)

    def count(self, nums: list[int], k: int) -> int:
        min_ = min(nums)
        max_ = max(nums)
        counts = [0] * (max_ - min_ + 1)
        for n in nums:
            counts[n - min_] += 1

        remain = k
        for idx in range(len(counts) - 1, -1, -1):
            remain -= counts[idx]
            if remain <= 0:
                return idx + min_

        return -1

        return boxes[-k] + min_

    def heapq_k_size(self, nums: list[int], k: int) -> int:
        heap: list[int] = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

    def heapq_nlargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[3, 2, 1, 5, 6, 4], 2],
            # expected
            5,
        )
        yield (
            # params
            [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
            # expected
            4,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.findKthLargest(*params))


if __name__ == '__main__':
    unittest.main()
