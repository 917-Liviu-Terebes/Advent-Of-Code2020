# Day 6

f = open("input.txt", "rt")


# for part 1
def get_count_of_answers(group_answers):
    """
    Gets the number of distinct letters/answers of a group
    :param group_answers: String of all the answers given by a certain group
    :return: Number of distinct answers given by a grou[
    """
    # get every letter
    group_answers = [letter for letter in group_answers if letter.isalpha()]
    # the set will keep only one instance of each letter
    return len(set(group_answers))


# for part 2
def get_count_of_same_answers(group_answers):
    """
    Gets the number of questions answered by everyone in a group
    :param group_answers: String of all the answers given by a certain group
    :return: Number of questions answered by everyone
    """
    # get number of group members and a list with each answer
    number_of_group_members = len(group_answers.split('\n'))
    group_answers = [letter for letter in group_answers if letter.isalpha()]
    # just get the count of each letter and see if it is equal to the number of members
    letter_freq = {}
    for letter in group_answers:
        if letter not in letter_freq:
            letter_freq[letter] = 0
        letter_freq[letter] += 1
    ans_counter = 0
    for letter in letter_freq:
        if letter_freq[letter] == number_of_group_members:
            ans_counter += 1
    return ans_counter


if __name__ == '__main__':
    file_info = f.read().split('\n\n')
    counter = 0
    for group in file_info:
        counter += get_count_of_same_answers(group)
    print(counter)