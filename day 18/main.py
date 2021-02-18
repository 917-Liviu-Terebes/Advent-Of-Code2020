"""
--- Day 18: Operation Order ---
- Strategy:
Rewrite the numbers as objects and overwrite the -+* operators
"""

import re


class EqualPrecedence(int):
    def __add__(self, other):
        return EqualPrecedence(int(self) + int(other))

    def __sub__(self, other):
        return EqualPrecedence(self * other)

    @staticmethod
    def eval(expr):
        # Replace each number in the string by EqualPrecedence(number) and * by -
        # Then evaluate the sum and return it
        return eval(re.sub(r"\d+", lambda match: f"EqualPrecedence({match.group(0)})", expr.replace("*", "-")))


class ReversedPrecedence(int):
    def __add__(self, other):
        return ReversedPrecedence(int(self) * int(other))

    def __mul__(self, other):
        return ReversedPrecedence(int(self) + int(other))

    @staticmethod
    def eval(expr):
        # Replace * by + and evaluate the expression
        return eval(re.sub(r"\d+",
                           lambda match: f"ReversedPrecedence({match.group(0)})",
                           expr.replace("+", "x").replace("*", "+").replace("x", "*"),))


if __name__ == '__main__':
    # Read the contents
    f = open('input.txt', 'rt')
    expressions = f.read().splitlines()

    print("Part 1:", sum(map(EqualPrecedence.eval, expressions)))
    print("Part 2:", sum(map(ReversedPrecedence.eval, expressions)))

    f.close()
