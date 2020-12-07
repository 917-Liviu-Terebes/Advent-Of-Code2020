# Day 7
# the regex might be stolen from sophiebits because it makes the code shorter

import re

f = open('input.txt', 'rt')
f = [line.strip() for line in f.readlines()]

# I imagined the bags as trees, but this also works
contained_in = dict()
contains = dict()

bags_holding_gold = set()
number_of_bags = 0


def count_bags_which_hold_colour(colour):
    # add each bag that contains the given colour into a set
    # and go up to the next level and also count that
    if colour not in contained_in:
        return
    for bag_colour in contained_in[colour]:
        bags_holding_gold.add(bag_colour)
        count_bags_which_hold_colour(bag_colour)


def count_contained_bags(colour):
    # sum each bag contained by given colour bag
    # and go down to the next level and also count them
    count = 0
    for quantity, bagcolor in contains[colour]:
        count += quantity
        count += quantity * count_contained_bags(bagcolor)
    return count


if __name__ == '__main__':
    for line in f:
        # god bless regex
        # this gets the color of the bag on the current line
        color = re.match(r'(.+?) bags contain', line)[1]
        # for empty dict
        if color not in contains:
            contains[color] = list()
        # this gets all the bags on the line, which are contained by the bigger bag at the start of the line
        for quantity, bagcolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            quantity = int(quantity)
            # for empty dict
            if bagcolor not in contained_in:
                contained_in[bagcolor] = set()

            # update the dictionaries
            contained_in[bagcolor].add(color)
            contains[color].append((quantity, bagcolor))

    # part 1
    # count_bags_which_hold_colour('shiny gold')
    # print(len(bags_holding_gold))

    # part 2
    print(count_contained_bags('shiny gold'))