
inp = open("input.txt", "rt")
out = open("output.txt", "wt")
value_hash = {}

if __name__ == '__main__':
    for line in inp.readlines():
        number = int(line)

        if 2020 - number in value_hash:
            out.write(str(number * (2020 - number)))
            break
        else:
           value_hash[number] = 1

