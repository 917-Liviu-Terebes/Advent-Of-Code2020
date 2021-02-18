"""
--- Day 1: Report Repair ---
    - Python
    - Hashing algorithms for 2SUM and 3SUM problems
"""


def part1(value_hash):
    """
    Part 1 of the problem, O(n) 2SUM solution
    """
    # Search the first number for which 2020-number is in the list of numbers
    for number in value_hash.keys():
        if 2020 - number in value_hash:
            return number * (2020 - number)


def part2(numbers, value_hash):
    """
    Part 2 of the problem
    This is basically 3SUM, the best algorithm should take O(n^2) time (according to wikipedia)
    """
    # Double for to search for a triple (i, j, 2020-num[i]-num[j]) and print the first one
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                # Found the pair
                if 2020 - numbers[i] - numbers[j] in value_hash:
                    return numbers[i] * numbers[j] * (2020 - numbers[i] - numbers[j])


if __name__ == '__main__':
    inp = open("input.txt", "rt")

    # Store the numbers in a list and a dict/hash table
    numbers = []
    value_hash = {}
    for line in inp.readlines():
        numbers.append(int(line))
        value_hash[int(line)] = 1

    # Don't forget to close the file
    inp.close()

    print(part1(value_hash))
    print(part2(numbers, value_hash))


