"""
    Day 15
"""


def get_nth_number_in_sequence(n):
    with open('input.txt', 'rt') as f:
        # dictionary to save the last index of a number
        last_index = {}
        # save the input in a list
        number_list = [int(number) for number in f.read().split(',')]
        counter = 1
        # count the numbers from the list and add them in the dictionary
        for number in number_list:
            last_index[number] = counter
            counter += 1

        # The fun game begins
        current_number = 0
        while counter < n:
            # save the number before it gets modified
            prev_number = current_number
            # If the number was said before, update it with the distance
            if current_number in last_index:
                current_number = counter - last_index[current_number]
            else:
                # If it was new, the next number becomes 0
                current_number = 0
            # Update the index of the number before it got modified
            last_index[prev_number] = counter
            # Increase the index/counter
            counter += 1
        # returns the number on position #n
        return current_number


def part_1():
    return get_nth_number_in_sequence(2020)


def part_2():
    # brute force, but it takes less than 5 seconds
    return get_nth_number_in_sequence(30000000)


if __name__ == '__main__':
    print('Part 1', part_1())
    print('Part 2', part_2())