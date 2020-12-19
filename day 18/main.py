"""
    Day 18
"""


import re

with open("input.txt") as f:
    expressions = f.read().splitlines()


class EqualPrecedence(int):
    def __add__(self, other):
        return EqualPrecedence(int(self) + int(other))

    def __sub__(self, other):
        return EqualPrecedence(self * other)

    @staticmethod
    def eval(expr):
        return eval(re.sub(r"\d+", lambda match: f"EqualPrecedence({match.group(0)})", expr.replace("*", "-"),))


class ReversedPrecedence(int):
    def __add__(self, other):
        return ReversedPrecedence(int(self) * int(other))

    def __mul__(self, other):
        return ReversedPrecedence(int(self) + int(other))

    @staticmethod
    def eval(expr):
        return eval(re.sub(r"\d+",
                           lambda match: f"ReversedPrecedence({match.group(0)})",
                           expr.replace("+", "x").replace("*", "+").replace("x", "*"),))


print("Part 1:", sum(map(EqualPrecedence.eval, expressions)))
print("Part 2:", sum(map(ReversedPrecedence.eval, expressions)))