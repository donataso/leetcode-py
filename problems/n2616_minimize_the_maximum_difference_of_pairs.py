import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
    difficulty: medium
    """

    def minimizeMax(self, nums: list[int], p: int) -> int:
        if not nums or not p:
            return 0

        nums.sort()
        n = len(nums)

        def count_pairs(threshold):
            """
            Find the number of pairs with difference not higher than threshold
            """
            idx, count = 0, 0
            while idx < n - 1:
                if nums[idx + 1] - nums[idx] <= threshold:
                    count += 1
                    idx += 1
                idx += 1
            return count

        # use binary search to find the lowest threshold that has at least p pairs
        low = 0
        high = nums[-1] - nums[0]  # max difference between numbers
        while low < high:
            mid = low + (high - low) // 2

            # if there are enough pairs, look for a smaller threshold.
            # otherwise, look for a larger threshold.
            if count_pairs(mid) >= p:
                high = mid
            else:
                low = mid + 1

        return low


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[10, 1, 2, 7, 1, 3], 2],
            # expected
            1,
        )
        yield (
            # params
            [[4, 2, 1, 2], 1],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.minimizeMax(*params))


if __name__ == '__main__':
    unittest.main()
