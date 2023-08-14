import heapq
import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/meeting-rooms-ii/
    difficulty: medium
    """
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        return self.better_with_heapq(intervals)
        # return self.not_so_great(intervals)

    def better_with_heapq(self, intervals: list[list[int]]) -> int:
        rooms: list[int] = []
        intervals.sort()
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])

        return len(rooms)

    def not_so_great(self, intervals: list[list[int]]) -> int:
        rooms: list[list[list[int]]] = []
        intervals.sort()
        for interval in intervals:
            has_free_room = False
            for room in rooms:
                if interval[0] < room[-1][1]:
                    has_free_room = False
                else:
                    has_free_room = True
                    room.append(interval)
                    break
            if not has_free_room:
                rooms.append([interval])

        return len(rooms)


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[[0, 30], [5, 10], [15, 20]]],
            # expected
            2,
        )
        yield (
            # params
            [[[7, 10], [2, 4]]],
            # expected
            1,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.minMeetingRooms(*params))


if __name__ == '__main__':
    unittest.main()
