import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/subsets/
    difficulty: medium
    """

    def subsets(self, nums: list[int]) -> list[list[int]]:
        return self.lexicographic_subsets(nums)
        # return self.cascade(nums)
        # return self.backtrack(nums)

    def lexicographic_subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        def mask_to_subset(mask: int) -> list[int]:
            s: list[int] = []
            bit = len(nums) - 1
            while mask:
                if mask & 1:
                    s.append(nums[bit])
                mask >>= 1
                bit -= 1

            return s

        for i in range(2 ** len(nums)):
            result.append(mask_to_subset(i))

            # or like this with a bit more type casting
            # result.append([nums[int(j)] for j in bin(i) if j != ''])

        return result

    def cascade(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = [[]]

        for n in nums:
            result += [s + [n] for s in result]

        return result

    def backtrack(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(curr: list[int], numbers: list[int]):
            result.append(curr.copy())

            for i, n in enumerate(numbers):
                curr.append(n)
                backtrack(curr, numbers[i + 1:])
                curr.pop()

        backtrack([], nums)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 2, 3]],
            # expected
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        )
        yield (
            # params
            [[0]],
            # expected
            [[], [0]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(sorted(expected), sorted([sorted(s) for s in solution.subsets(*params)]))


if __name__ == '__main__':
    unittest.main()
