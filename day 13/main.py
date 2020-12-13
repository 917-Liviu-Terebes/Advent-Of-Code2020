# Day 13, a lot of modular arithmetic

from functools import reduce

f = open('input.txt', 'rt')


def find_closes_past_time(timestamp, bus_id):
    # compute the first number of the form bus_id * something which is greater than timestamp
    quotient = timestamp // bus_id

    if quotient * bus_id < timestamp:
        return (quotient + 1) * bus_id
    else:
        return quotient * bus_id


def comp_power(base, power, modulo):
    # logarithmic exponentiation
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        power = power // 2
    return result


def compute_inverse(number, modulo):
    # inverse is number^(modulo - 2) mod modulo
    return comp_power(number, modulo - 2, modulo)


if __name__ == '__main__':
    timestamp = int(f.readline().strip())
    schedule = f.readline().strip()
    schedule = [(x, cnt) for cnt, x in enumerate(schedule.split(','))]

    # Part 1, simple minimum finding
    min_diff = timestamp
    min_id = 0
    for (bus_id, cnt) in schedule:
        if bus_id != 'x':
            bus_id = int(bus_id)
            diff = find_closes_past_time(timestamp, bus_id) - timestamp
            if diff < min_diff:
                min_diff, min_id = diff, bus_id

    print("Part 1: ", min_id * min_diff)

    # Part 2, Chinese Remainder Theorem ftw
    result = 0
    # get all equation coefficients
    big_prod = reduce((lambda x, y: x * y), [int(bus_id) for (bus_id, cnt) in schedule if bus_id != 'x'])
    for (bus_id, cnt) in schedule:
        if bus_id != 'x':
            bus_id = int(bus_id)
            cnt = int(cnt)
            # we can see each schedule as the equation
            # x = -cnt (mod bus_id)
            # so we apply CRT
            # result = sum of (-cnt) * (prod of bus_id / this bus_id) * (bus_id ^-1 mod)
            a = -cnt
            b = big_prod // bus_id
            c = compute_inverse(b, bus_id)
            result = (result + a * b * c) % big_prod
    print("Part 2: ", result)
    # 598411311431841
