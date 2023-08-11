import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/3sum-closest/
    difficulty: medium
    """

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == target:
                    return target
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                if curr_sum < target:
                    low += 1
                else:
                    high -= 1

        return closest

        # the following didn't work with all test cases, abandoning it in favor of a two pointer approach
        #
        # closest = sum(nums[:3])
        # seen: list[int] = []
        # heapq.heapify(seen)
        # for i, n1 in enumerate(nums):
        #     for j, n2 in enumerate(nums[i + 1:]):
        #         if supplement in seen:
        #             return target
        #
        #         # binary search 'seen' for the closest number
        #         low = 0
        #         high = len(seen)
        #         while low < high:
        #             mid = low + (high - low) // 2
        #             curr_sum = n1 + n2 + seen[mid]
        #             diff = target - curr_sum
        #             if abs(diff) < abs(target - closest):
        #                 closest = curr_sum
        #             if diff < 0:
        #                 low = mid + 1
        #             else:
        #                 high = mid - 1
        #
        #         if n2 not in seen:
        #             heapq.heappush(seen, n2)
        #
        # return closest


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[40, -53, 36, 89, -38, -51, 80, 11, -10, 76, -30, 46, -39, -15, 4, 72, 83, -25, 33, -69, -73, -100, -23,
              -37, -13, -62, -26, -54, 36, -84, -65, -51, 11, 98, -21, 49, 51, 78, -58, -40, 95, -81, 41, -17, -70, 83,
              -88, -14, -75, -10, -44, -21, 6, 68, -81, -1, 41, -61, -82, -24, 45, 19, 6, -98, 11, 9, -66, 50, -97, -2,
              58, 17, 51, -13, 88, -16, -77, 31, 35, 98, -2, 0, -70, 6, -34, -8, 78, 22, -1, -93, -39, -88, -77, -65,
              80, 91, 35, -15, 7, -37, -96, 65, 3, 33, -22, 60, 1, 76, -32, 22], 292],
            # expected
            291,
        )
        yield (
            # params
            [[1, 1, 1, 0], -100],
            # expected
            2,
        )
        yield (
            # params
            [[-1, 2, 1, -4], 1],
            # expected
            2,
        )
        yield (
            # params
            [[0, 0, 0], 1],
            # expected
            0,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.threeSumClosest(*params))


if __name__ == '__main__':
    unittest.main()
