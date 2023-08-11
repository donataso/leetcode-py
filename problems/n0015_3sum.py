import unittest

from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/3sum
    difficulty: medium
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # return self.unsorted_better(nums)
        # return self.sorted(nums)
        return self.unsorted(nums)

    def unsorted_better(self, nums: list[int]) -> list[list[int]]:
        result, dups = set(), set()
        seen: dict[int, int] = {}
        for i, val1 in enumerate(nums):
            if val1 in dups:
                continue

            dups.add(val1)
            for j, val2 in enumerate(nums[i + 1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    result.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i

        return [list(x) for x in result]

    def sorted(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results: list[list[int]] = []
        cnt = len(nums)

        for m in range(cnt - 2):
            if nums[m] > 0:
                break  # the list is sorted, there's no way to get zero when the current number is positive
            if m > 0 and nums[m - 1] == nums[m]:
                continue  # skip duplicate values

            low = m + 1
            high = cnt - 1
            while low < high:
                sum_ = nums[m] + nums[low] + nums[high]
                if sum_ == 0:
                    results.append([nums[m], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1  # skip duplicate values
                    continue
                if sum_ < 0:
                    low += 1
                else:
                    high -= 1

        return results

    def unsorted(self, nums: list[int]) -> list[list[int]]:
        results: list[list[int]] = []
        cnt = len(nums)
        for m in range(cnt - 2):
            hm: dict[int, int] = {}
            target = 0 - nums[m]
            for n in range(m + 1, cnt):
                if nums[n] in hm:
                    result = sorted([nums[m], hm[nums[n]], nums[n]])
                    if result not in results:
                        results.append(result)
                else:
                    hm[target - nums[n]] = nums[n]
        return results


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[-1, 0, 1, 2, -1, -4]],
            # expected
            [[-1, 0, 1], [-1, -1, 2]],
        )
        yield (
            # params
            [[0, 1, 1]],
            # expected
            [],
        )
        yield (
            # params
            [[0, 0, 0]],
            # expected
            [[0, 0, 0]],
        )
        yield (
            # params
            [[-2, 0, 0, 2, 2]],
            # expected
            [[-2, 0, 2]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        actual = [sorted(x) for x in solution.threeSum(*params)]
        actual.sort()

        expected = [sorted(x) for x in expected]
        expected.sort()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
