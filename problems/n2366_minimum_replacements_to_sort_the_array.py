import math
import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
    difficulty: hard
    """

    def minimumReplacement(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            count += num_elements - 1
            nums[i] = nums[i] // num_elements

        return count


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 7, 3]],
            # expected
            2,
        )
        yield (
            # params
            [[368, 112, 2, 282, 349, 127, 36, 98, 371, 79, 309, 221, 175, 262, 224, 215, 230, 250, 84, 269, 384, 328,
              118, 97, 17, 105, 342, 344, 242, 160, 394, 17, 120, 335, 76, 101, 260, 244, 378, 375, 164, 190, 320, 376,
              197, 398, 353, 138, 362, 38, 54, 172, 3, 300, 264, 165, 251, 24, 312, 355, 237, 314, 397, 101, 117, 268,
              36, 165, 373, 269, 351, 67, 263, 332, 296, 13, 118, 294, 159, 137, 82, 288, 250, 131, 354, 261, 192, 111,
              16, 139, 261, 295, 112, 121, 234, 335, 256, 303, 328, 242, 260, 346, 22, 277, 179, 223]],
            # expected
            17748,
        )
        yield (
            # params
            [[3, 9, 3]],
            # expected
            2,
        )
        yield (
            # params
            [[1, 2, 3, 4, 5]],
            # expected
            0,
        )
        yield (
            # params
            [[12, 9, 7, 6, 17, 19, 21]],
            # expected
            6,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.minimumReplacement(*params))


if __name__ == '__main__':
    unittest.main()
