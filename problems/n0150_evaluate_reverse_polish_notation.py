import unittest
from helper.unittest_data_provider import data_provider


class Solution:
    """
    https://leetcode.com/problems/evaluate-reverse-polish-notation
    difficulty: medium
    """

    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: int(a / b),
            '*': lambda a, b: a * b
        }

        for token in tokens:
            if token in operations:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(operations[token](n1, n2))
            else:
                stack.append(int(token))

        # for token in tokens:
        #     if token == '/':
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(int(b / a))
        #     elif token == '*':
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(a * b)
        #     elif token == '+':
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(a + b)
        #     elif token == '-':
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(b - a)
        #     else:
        #         stack.append(int(token))

        return stack[0]


class SolutionTestCase(unittest.TestCase):
    @staticmethod
    def dataprovider():
        yield (
            # params
            [['2', '1', '+', '3', '*']],
            # expected
            9,
        )
        yield (
            # params
            [['4', '13', '5', '/', '+']],
            # expected
            6,
        )
        yield (
            # params
            [['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']],
            # expected
            22,
        )

    @data_provider(dataprovider)
    def test_solution(self, params, expected):
        solution = Solution()
        self.assertEqual(expected, solution.evalRPN(*params))


if __name__ == '__main__':
    unittest.main()
