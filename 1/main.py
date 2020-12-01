import sys

inp = open("input.txt", "rt")
out = open("output.txt", "wt")
value_hash = {}

# main for part 1
# if __name__ == '__main__':
#     for line in inp.readlines():
#         number = int(line)
#
#         if 2020 - number in value_hash:
#             out.write(str(number * (2020 - number)))
#             break
#         else:
#            value_hash[number] = 1

# main for part 2 (O(n^2) but it works)
if __name__ == '__main__':
    numbers = []
    for line in inp.readlines():
        numbers.append(int(line))
        value_hash[int(line)] = 1

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                if 2020 - numbers[i] - numbers[j] in value_hash:
                    out.write(str(numbers[i] * numbers[j] * (2020 - numbers[i] - numbers[j])))
                    sys.exit()

