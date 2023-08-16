import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/jump-game
    difficulty: medium
    """

    def canJump(self, nums: list[int]) -> bool:
        # return self.dp(nums)
        return self.simple_pass(nums)

    def dp(self, nums: list[int]) -> bool:
        length = len(nums)
        if length < 2:
            return True

        mem: set[int] = set()

        def reach(idx: int) -> bool:
            if idx >= length - 1:
                return True

            for step in range(nums[idx], 0, -1):
                if idx + step in mem:
                    continue
                mem.add(idx + step)
                if reach(idx + step):
                    return True

            return False

        return reach(0)

    def simple_pass(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return True

        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
            if max_reach >= len(nums) - 1:
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[2, 3, 1, 1, 4]],
            # expected
            True,
        )
        yield (
            # params
            [[3, 2, 1, 0, 4]],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.canJump(*params))


if __name__ == '__main__':
    unittest.main()
