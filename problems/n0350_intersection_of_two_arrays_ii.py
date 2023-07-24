import unittest
from collections import defaultdict

from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
    difficulty: easy
    """

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        return self.hashmap(nums1, nums2)
        return self.sorted(nums1, nums2)
        return self.bruteforce(nums1, nums2)

    def hashmap(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        hm: dict[int, int] = defaultdict(int)
        for n in nums1:
            hm[n] += 1

        for n in nums2:
            if n in hm and hm[n] > 0:
                result.append(n)
                hm[n] -= 1

        return result

    def sorted(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        result = []

        m = 0
        n = 0
        while m < len(nums1) and n < len(nums2):
            if nums1[m] == nums2[n]:
                result.append(nums1[m])
                m += 1
                n += 1
            elif nums1[m] < nums2[n]:
                m += 1
            elif nums1[m] > nums2[n]:
                n += 1

        return result

    def bruteforce(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for n in nums1:
            if n in nums2:
                result.append(n)
                nums2.remove(n)

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[1, 2, 2, 1], [2, 2]],
            # expected
            [2, 2],
        )
        yield (
            # params
            [[4, 9, 5], [9, 4, 9, 8, 4]],
            # expected
            [4, 9],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, sorted(solution.intersect(*params)))


if __name__ == '__main__':
    unittest.main()
