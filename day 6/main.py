"""
--- Day 6: Custom Customs ---
Strategy:
- Split the data into groups and count the letters in each of them (simple parsing)
"""
from collections import defaultdict


def get_count_of_answers(group_answers):
    """
    Gets the number of distinct letters/answers of a group
    :param group_answers: String of all the answers given by a certain group
    :return: Number of distinct answers given by a group
    """
    # Get every letter in the answers
    group_answers = [letter for letter in group_answers if letter.isalpha()]
    # The set will keep only one instance of each letter, and the length is the number of distinct letters
    return len(set(group_answers))


def get_count_of_same_answers(group_answers):
    """
    Gets the number of questions answered by everyone in a group
    :param group_answers: String of all the answers given by a certain group
    :return: Number of questions answered by everyone
    """
    # Get number of group members and a list with each answer
    number_of_group_members = len(group_answers.split('\n'))
    group_answers = [letter for letter in group_answers if letter.isalpha()]

    # Just get the count of each letter and see if it is equal to the number of members
    letter_freq = defaultdict(lambda: 0)    # <- defaultdict with base value 0
    for letter in group_answers:
        letter_freq[letter] += 1

    ans_counter = 0
    for letter in letter_freq:
        if letter_freq[letter] == number_of_group_members:
            ans_counter += 1

    return ans_counter


def part1(input_data):
    """
    Part 1 of the problem
    """
    return sum(get_count_of_answers(group) for group in input_data)


def part2(input_data):
    """
    Part 2 of the problem
    """
    return sum(get_count_of_same_answers(group) for group in input_data)


if __name__ == '__main__':
    f = open("input.txt", "rt")
    file_info = f.read().split('\n\n')
    print("Part 1: ", part1(file_info))
    print("Part 2: ", part2(file_info))
