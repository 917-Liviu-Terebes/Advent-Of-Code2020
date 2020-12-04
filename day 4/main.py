import string

f = open('input.txt', 'rt')


# for part 1
def check_passport(data_string):
    counter = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in fields:
        if field in data_string:
            counter += 1
    return 1 if counter == 7 else 0


def get_specific_part(data_string, substring):
    return [string for string in data_string if string.startswith(substring)][0][4:]


def check_valid_passport(data_string):
    data_string = sorted(data_string.split(' '))
    if '\n' in data_string[1]:
        data_string = data_string[2:]
    else:
        data_string = data_string[1:]
    for i in range(0, len(data_string)):
        if "\n" in data_string[i]:
            data_string[i] = data_string[i][:-1]
    if not 1920 <= int(get_specific_part(data_string, "byr")) <= 2002:
        return 0
    if not 2010 <= int([string for string in data_string if string.startswith("iyr")][0][4:]) <= 2020:
        return 0
    if not 2020 <= int([string for string in data_string if string.startswith("eyr")][0][4:]) <= 2030:
        return 0

    # height
    hs = get_specific_part(data_string, "hgt")
    if 'cm' in hs:
        height = int(hs[:-2])
        if not 150 <= height <= 193:
            return 0
    else:
        if len(hs) < 4:
            return 0
        height = int(hs[:-2])
        if not 59 <= height <= 76:
            return 0

    # hair color
    hair_color = get_specific_part(data_string, "hcl")
    if hair_color[0] != '#':
        return 0
    if not all(c in string.hexdigits for c in hair_color[1:]):
        return 0

    ecl_data = get_specific_part(data_string, "ecl")
    if ecl_data not in ["amb", "blu" ,"brn", "gry", "grn", "hzl", "oth"]:
        return 0
    if not (len(get_specific_part(data_string, "pid")) == 9 and get_specific_part(data_string, "pid").isdigit()):
        return 0
    return 1


if __name__ == '__main__':
    count = 0
    text_data = ''
    for line in f:
        text_data += " " + line
        if line == '\n':
            if check_passport(text_data):
                count += check_valid_passport(text_data)
            text_data = ''
    if check_passport(text_data):
        count += check_valid_passport(text_data)
    print(count)