"""
--- Day 13: Shuttle Search ---
Strategy:
- Modular arithmetic (specifically, the Chinese Remainder Theorem)
"""

from functools import reduce


def find_closes_past_time(timestamp, bus_id):
    """
    Compute the first number of the form bus_id * something which is greater than timestamp
    :param timestamp: Int
    :param bus_id: Int
    :return: The smallest number of the form bus_id * k that is bigger than timestamp
    """
    quotient = timestamp // bus_id

    if quotient * bus_id < timestamp:
        return (quotient + 1) * bus_id
    else:
        return quotient * bus_id


def comp_power(base, power, modulo):
    """
    Computes base^power % modulo using rapid exponentiation
    :param base: Int
    :param power: Int
    :param modulo: Int
    :return: base^power % modulo
    """
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        power = power // 2
    return result


def compute_inverse(number, modulo):
    """
    Computes the modular inverse of the given number
    :param number: Int
    :param modulo: Int
    :return: Modular inverse (number^(modulo - 2) mod modulo)
    """
    return comp_power(number, modulo - 2, modulo)


def part1(timestamp, schedule):
    """
    Part 1 of the problem
    """
    # Part 1, simple minimum finding
    min_diff = timestamp
    min_id = 0
    # Go through the schedule and find the minimum difference
    for (bus_id, cnt) in schedule:
        if bus_id != 'x':
            bus_id = int(bus_id)
            diff = find_closes_past_time(timestamp, bus_id) - timestamp
            if diff < min_diff:
                min_diff, min_id = diff, bus_id
    # Return the result
    return min_id * min_diff


def part2(schedule):
    """
    Part 2 of the problem
    """
    # Part 2, Chinese Remainder Theorem (look it up on Wikipedia/Brilliant) ftw
    result = 0
    # Get all equation coefficients
    big_prod = reduce((lambda x, y: x * y), [int(bus_id) for (bus_id, cnt) in schedule if bus_id != 'x'])

    for (bus_id, cnt) in schedule:
        if bus_id != 'x':
            bus_id = int(bus_id)
            cnt = int(cnt)
            # We can see each schedule as the equation
            # x = -cnt (mod bus_id)
            # So we apply CRT
            # result = Sum of (-cnt) * (prod of bus_id / this bus_id) * (bus_id ^-1 mod)
            a = -cnt
            b = big_prod // bus_id
            c = compute_inverse(b, bus_id)
            result = (result + a * b * c) % big_prod

    return result


if __name__ == '__main__':
    f = open('input.txt', 'rt')

    # Get the timestamp and schedule from the file
    timestamp = int(f.readline().strip())
    schedule = f.readline().strip()
    schedule = [(x, cnt) for cnt, x in enumerate(schedule.split(','))]

    print("Part 1: ", part1(timestamp, schedule))
    print("Part 2: ", part2(schedule))

    f.close()
