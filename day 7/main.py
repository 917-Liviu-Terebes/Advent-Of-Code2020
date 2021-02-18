"""
--- Day 7: Handy Haversacks ---
Strategy:
- Use regex to parse the data in an easier way. Then perform a DFS to count the bags
Thanks to sophiebits for the idea of using regex (Without it, the code is much longer and difficult)
"""
import re

# I imagined the bags as trees, but this also works
# Watch out, they are global variables
contained_in = dict()
contains = dict()
bags_holding_gold = set()


def traverse_up_bags(colour):
    """
    Traverse each bag which holds a bag of given colour (and add it to the set of bags which hold gold)
    :param colour: Colour (String)
    """
    # Add each bag that contains the given colour into a set
    # And go up to the next level and also count that
    if colour not in contained_in:
        return
    for bag_colour in contained_in[colour]:
        bags_holding_gold.add(bag_colour)
        traverse_up_bags(bag_colour)


def count_contained_bags(colour):
    """
    Traverse each bag which is contained by the bag of the given colour and count the number of them
    :param colour: Colour (String)
    :return: Count
    """
    # Sum each bag contained by given colour bag
    # And go down to the next level and also count them
    count = 0
    for quantity, bag_color in contains[colour]:
        count += quantity
        count += quantity * count_contained_bags(bag_color)
    return count


def parse_input():
    """
    Parse the input file
    """
    inp_file = open('input.txt', 'rt')

    file_lines = [line.strip() for line in inp_file.readlines()]

    for line in file_lines:
        # god bless regex
        # This gets the color of the bigger bag on the current line
        color = re.match(r'(.+?) bags contain', line)[1]

        # Initialize the empty dictionary
        if color not in contains:
            contains[color] = list()

        # This gets all the bags on the line (which are contained by the bigger bag at the start of the line)
        for quantity, bag_color in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            # Get how many bags of the current color are in the bag
            quantity = int(quantity)

            # Initialize empty dictionary
            if bag_color not in contained_in:
                contained_in[bag_color] = set()

            # Update the dictionaries/ Add the bag relationships
            contained_in[bag_color].add(color)
            contains[color].append((quantity, bag_color))

    inp_file.close()


if __name__ == '__main__':
    parse_input()

    # Part 1
    traverse_up_bags('shiny gold')
    print("Part 1: ", len(bags_holding_gold))

    # Part 2
    print("Part 2: ", count_contained_bags('shiny gold'))
