import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/merge-intervals
    difficulty: medium
    """

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        return self.better(intervals)
        # return self.my_solution(intervals)

    def better(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result: list[list[int]] = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals.
                result[-1][1] = max(result[-1][1], interval[1])

        return result

    def my_solution(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result: list[list[int]] = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                if intervals[i][1] < result[-1][1]:
                    continue
                result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])

        return result

class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[1,4],[2,3]]],
            # expected
            [[1, 4]],
        )
        yield (
            # params
            [[[1, 3], [2, 6], [8, 10], [15, 18]]],
            # expected
            [[1, 6], [8, 10], [15, 18]],
        )
        yield (
            # params
            [[[1, 4], [4, 5]]],
            # expected
            [[1, 5]],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.merge(*params))


if __name__ == '__main__':
    unittest.main()
