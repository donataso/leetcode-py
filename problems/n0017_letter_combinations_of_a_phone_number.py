import unittest
from unittest_data_provider import data_provider  # type: ignore


class Solution:
    """
    https://leetcode.com/problems/letter-combinations-of-a-phone-number
    difficulty: medium
    """
    numbers_map: dict[str, list[str]] = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        return self.zip_it(digits)
        # return self.queue_it(digits)

    def zip_it(self, digits: str) -> list[str]:
        result: list[str] = self.numbers_map[digits[0]].copy()

        for idx in range(1, len(digits)):
            letters = self.numbers_map[digits[idx]]

            # multiply each existing string in the result by the number of letters under the next digit
            # and zip the groups with the new letters
            zipped = [zip([letter] * len(letters), letters) for letter in result]
            # zipped: [[('a', 'd'), ('a', 'e'), ('a', 'f')], [('b', 'd'), ...], ...]
            # flatten the result
            result = [''.join(t) for r in zipped for t in r]

        return result

    def queue_it(self, digits: str) -> list[str]:
        result: list[str] = self.numbers_map[digits[0]].copy()

        for idx in range(1, len(digits)):
            for i in range(len(result)):
                base_letter = result.pop(0)
                result.extend([base_letter + letter for letter in self.numbers_map[digits[idx]]])

        return result


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            ['23'],
            # expected
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
        )
        yield (
            # params
            [''],
            # expected
            [],
        )
        yield (
            # params
            ['2'],
            # expected
            ['a', 'b', 'c'],
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.letterCombinations(*params))


if __name__ == '__main__':
    unittest.main()
