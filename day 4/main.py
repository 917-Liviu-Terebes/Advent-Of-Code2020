"""
--- Day 4: Passport Processing ---
Strategy:
- Awful string splitting and checking each property of the passport
(Sorry, I didn't know regex and I wanted to keep it without it)
"""

import string


def check_passport(passport):
    """
    Checks if a passport has all the fields
    :param passport: Passport string
    :return: True/False
    """
    counter = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in fields:
        if field in passport:
            counter += 1
    return counter == 7


def get_field_data(passport, field):
    """
    Gets the data of a certain field
    :param passport: Passport (String)
    :param field: Field to be searched (String)
    :return: Data of the field (String)
    """
    return [fie for fie in passport if fie.startswith(field)][0][4:]


def check_valid_passport(data_string):
    """
    Checks if a given passport is valid
    :param data_string: Passport (String)
    :return: True/False
    """
    data_string = sorted(data_string.split(' '))

    # Check the date of birth
    if not 1920 <= int(get_field_data(data_string, "byr")) <= 2002:
        return False
    # Check the issue year
    if not 2010 <= int(get_field_data(data_string, "iyr")) <= 2020:
        return False
    # Check the expiration year
    if not 2020 <= int(get_field_data(data_string, "eyr")) <= 2030:
        return False

    # Check the height
    hs = get_field_data(data_string, "hgt")
    if 'cm' in hs:
        # Check the height in cm
        height = int(hs[:-2])
        if not 150 <= height <= 193:
            return False
    else:
        # Check the height in inches
        if len(hs) < 4:
            return False
        height = int(hs[:-2])
        if not 59 <= height <= 76:
            return False

    # Check the hair colour (It has to start with # and contain hexa digits)
    hair_color = get_field_data(data_string, "hcl")
    if hair_color[0] != '#':
        return False
    if not all(c in string.hexdigits for c in hair_color[1:]):
        return False

    # Check the eye color
    ecl_data = get_field_data(data_string, "ecl")
    if ecl_data not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    # Check the passport id
    if not (len(get_field_data(data_string, "pid")) == 9 and get_field_data(data_string, "pid").isdigit()):
        return False

    return True


def part1(pass_data):
    """
    Part 1 of the program
    :param pass_data: List of passport strings
    """
    count = 0
    for passport in pass_data:
        if check_passport(passport):
            count += 1
    return count


def part2(pass_data):
    """
    Part 2 of the program
    :param pass_data: List of passport strings
    """
    count = 0
    for passport in pass_data:
        if check_passport(passport):
            if check_valid_passport(passport):
                count += 1
    return count


if __name__ == '__main__':
    f = open('input.txt', 'rt')

    read_data = [passport.strip().replace('\n', ' ') for passport in f.read().split('\n\n')]

    print("Part 1: ", part1(read_data))
    print("Part 2: ", part2(read_data))

    f.close()
