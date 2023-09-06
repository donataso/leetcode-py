import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/minimum-penalty-for-a-shop/
    difficulty: medium
    """

    def bestClosingTime(self, customers: str) -> int:
        return self.even_faster(customers)
        # return self.faster(customers)
        # return self.too_slow(customers)

    def even_faster(self, customers: str) -> int:
        min_fine = fine = closing_hour = 0

        for i, c in enumerate(customers):
            if c == 'N':
                fine += 1
            else:
                fine -= 1

                if fine < min_fine:
                    min_fine = fine
                    closing_hour = i + 1

        return closing_hour

    def faster(self, customers: str) -> int:
        min_fine = fine = customers.count('Y')
        closing_hour = 0

        for i, c in enumerate(customers):
            if c == 'N':
                fine += 1
            else:
                fine -= 1

            if fine < min_fine:
                min_fine = fine
                closing_hour = i + 1

        return closing_hour

    def too_slow(self, customers: str) -> int:
        min_fine = 10 ** 5 + 1
        closing_hour = -1

        for i in range(len(customers) + 1):
            fine = customers.count('N', 0, i) + customers.count('Y', i)
            if fine == 0:
                return i
            if fine < min_fine:
                min_fine = fine
                closing_hour = i

        return closing_hour


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['YYNY'],
            # expected
            2,
        )
        yield (
            # params
            ['NNNNN'],
            # expected
            0,
        )
        yield (
            # params
            ['YYYY'],
            # expected
            4,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.bestClosingTime(*params))


if __name__ == '__main__':
    unittest.main()
