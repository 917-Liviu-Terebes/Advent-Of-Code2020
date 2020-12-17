# """
#     Day 16
# """
# import math
# import re
#
#
# if __name__ == '__main__':
#     f = open('input.txt', 'rt')
#
#     lines = [line.strip() for line in f.readlines()]
#     line_counter = 1
#
#     # search the values using regex
#     ranges = [list(map(int, re.findall('\d+', x))) for x in lines[:20]]
#     my_ticket = [int(x) for x in lines[22].split(',')]
#     nearby_tickets = [list(map(int, re.findall('\d+', x))) for x in lines[25:]]
#
#     # compute all the possible valid values for numbers
#     valid = set()
#     for r1, r2, r3, r4 in ranges:
#         valid |= set(range(r1, r2 + 1))
#         valid |= set(range(r3, r4 + 1))
#
#     # print the sum for part 1
#     print("Part one:", sum(number for ticket in nearby_tickets for number in ticket if number not in valid))
#
#     # compute valid tickets
#     valid_tickets = [ticket for ticket in nearby_tickets if all(num in valid for num in ticket)]
#     field_index = dict()
#
#     # find every possible field index for every field
#     for ind, (t1, t2, t3, t4) in enumerate(ranges):
#         for i in range(20):
#             if all((t1 <= ticket[i] <= t2) or (t3 <= ticket[i] <= t4) for ticket in valid_tickets):
#                 if ind not in field_index:
#                     field_index[ind] = list()
#                 field_index[ind].append(i)
#
#     # We can see that some fields have less possible indexes than others
#     # A greedy approach to sort the dict by this length and take a new index each time may give us the result we wanted
#     # I think this can also be proved using set theory but hey, it worked
#     true_index = dict()
#     for k, values in sorted(field_index.items(), key=lambda x: len(x[1])):
#         true_index[k] = next(number for number in values if number not in true_index.values())
#
#     print('Part two:', math.prod(my_ticket[v] for k, v in true_index.items() if k < 6))

import re

def solve(p1):
    ON = set()
    f = open('input.txt', 'rt')
    L = list([l.strip() for l in f.readlines()])
    for r,l in enumerate(L):
        for c,ch in enumerate(l):
            if ch == '#':
                ON.add((r,c,0,0))

    for _ in range(6):
        NEW_ON = set()
        CHECK = set()
        for (x,y,z,w) in ON:
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            if w+dw==0 or (not p1):
                                CHECK.add((x+dx, y+dy, z+dz, w+dw))

        for (x,y,z,w) in CHECK:
            nbr = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                                if (x+dx, y+dy, z+dz, w+dw) in ON:
                                    nbr += 1
            if (x,y,z,w) not in ON and nbr == 3:
                NEW_ON.add((x,y,z,w))
            if (x,y,z,w) in ON and nbr in [2,3]:
                NEW_ON.add((x,y,z,w))
        ON = NEW_ON
    f.close()
    return len(ON)

print(solve(True))
print(solve(False))