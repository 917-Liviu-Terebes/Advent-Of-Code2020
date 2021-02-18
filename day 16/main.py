"""
--- Day 16: Ticket Translation ---
Strategy:
Maximum bipartite matching
- For the first part, extract the values from the input file and create a set with all possible valid values. Then
sum the numbers not belonging to this set.
For the second part, I stored for each field the ranges (from the all 20) that would match. Then, by a greedy approach
I kept selecting the fields with the most matches. And it worked...so no Ford-Fulkserson?
"""

import math
import re


if __name__ == '__main__':
    f = open('input.txt', 'rt')

    lines = [line.strip() for line in f.readlines()]
    line_counter = 1

    # Search the values using regex
    ranges = [list(map(int, re.findall('\d+', x))) for x in lines[:20]]
    my_ticket = [int(x) for x in lines[22].split(',')]
    nearby_tickets = [list(map(int, re.findall('\d+', x))) for x in lines[25:]]

    # Compute all the possible valid values for numbers
    valid = set()
    for r1, r2, r3, r4 in ranges:
        valid |= set(range(r1, r2 + 1))
        valid |= set(range(r3, r4 + 1))

    # Print the sum for part 1
    print("Part one:", sum(number for ticket in nearby_tickets for number in ticket if number not in valid))

    # Compute valid tickets
    valid_tickets = [ticket for ticket in nearby_tickets if all(num in valid for num in ticket)]
    field_index = dict()

    # Find every possible field index for every field
    for ind, (t1, t2, t3, t4) in enumerate(ranges):
        for i in range(20):
            if all((t1 <= ticket[i] <= t2) or (t3 <= ticket[i] <= t4) for ticket in valid_tickets):
                if ind not in field_index:
                    field_index[ind] = list()
                field_index[ind].append(i)

    # We can see that some fields have less possible indexes than others
    # A greedy approach to sort the dict by this length and take a new index each time may give us the result we wanted
    # Hey, it may not work in the general case but it worked here so...
    true_index = dict()
    for k, values in sorted(field_index.items(), key=lambda x: len(x[1])):
        true_index[k] = next(number for number in values if number not in true_index.values())

    # Print the product for part 2
    print('Part two:', math.prod(my_ticket[v] for k, v in true_index.items() if k < 6))
