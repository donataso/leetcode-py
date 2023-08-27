import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/frog-jump/
    difficulty: hard
    """

    def canCross(self, stones: list[int]) -> bool:
        return self.recursive_with_mem(stones)
        # return self.recursive_too_slow(stones)

    def recursive_with_mem(self, stones: list[int]) -> bool:
        mem: set[tuple[int, int]] = set()
        stones_set = set(stones)  # lookups in the set are much faster

        def jump(pos: int, k: int):
            if k < 1 or pos > stones[-1] or pos not in stones_set or (pos, k) in mem:
                return False
            if pos == stones[-1]:
                return True

            mem.add((pos, k))

            return jump(pos + k, k - 1) or jump(pos + k, k) or jump(pos + k, k + 1)

        return jump(0, 1)

    def recursive_too_slow(self, stones: list[int]) -> bool:
        def jump(pos: int, k: int):
            if k < 1 or pos > stones[-1] or pos not in stones:
                return False
            if pos == stones[-1]:
                return True

            return jump(pos + k, k - 1) or jump(pos + k, k) or jump(pos + k, k + 1)

        return jump(0, 1)


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [[0, 1, 3, 5, 6, 8, 12, 17]],
            # expected
            True,
        )
        yield (
            # params
            [[0, 1, 2, 3, 4, 8, 9, 11]],
            # expected
            False,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.canCross(*params))


if __name__ == '__main__':
    unittest.main()
