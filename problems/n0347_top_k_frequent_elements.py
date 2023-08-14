import unittest
from collections import defaultdict, Counter
import heapq

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements/
    difficulty: medium
    """

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        return self.power_of_python_2(nums, k)
        # return self.power_of_python_1(nums, k)
        # return self.good_enough(nums, k)

    def power_of_python_1(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def power_of_python_2(self, nums: list[int], k: int) -> list[int]:
        return [n for n, _ in Counter(nums).most_common(k)]

    def good_enough(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = defaultdict(int)
        for n in nums:
            counts[n] += 1

        queue: list[tuple[int, int]] = []
        heapq.heapify(queue)

        for n, c in counts.items():
            heapq.heappush(queue, (c, n))

        return [n for _, n in heapq.nlargest(k, queue)]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 1, 1, 2, 2, 3], 2],
            # expected
            [1, 2],
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
        self.assertEqual(sorted(expected), sorted(solution.topKFrequent(*params)))


if __name__ == '__main__':
    unittest.main()
