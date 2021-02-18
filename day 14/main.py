"""
--- Day 14: Docking Data ---
It's hard to work with binary numbers in Python
Strategy:
- Simulate the bit work
"""


def part1():
    """
    Part 1 of the problem
    """
    f = open('input.txt', 'rt')
    mem, mask = {}, ""
    for line in f:
        if "mem" in line:
            # Get the address and value from the file
            mem_address = int(line.split(' = ')[0][4:-1])
            mem_value = int(line.split(' = ')[1])

            # Apply the mask on every bit
            for i in range(36):
                if mask[35 - i] == '0':
                    mem_value = mem_value & ~(1 << i)
                elif mask[35 - i] == '1':
                    mem_value = mem_value | (1 << i)

            # Save the value in memory
            mem[mem_address] = mem_value
        else:
            # Update the mask
            mask = line.split('=')[1].strip()
    f.close()
    # In the end, return the sum of all values in memory
    return sum(mem.values())


def generate_every_code(bin_address):
    """
    Generates every number given the float mast bin_address
    :param bin_address: List of strings
    :return: List of int
    """
    result = []
    # Get the positions where 'X' is

    # I see each 'X' as a 0/1. All the combinations can be seen as all the numbers from 0 to 2^len(X) - 1 in binary
    x_pos = [ind for (ind, bit) in enumerate(bin_address) if bit == 'X']
    count = len(x_pos)
    power_2 = 2 ** count
    # For every number in binary
    for bin_num in range(power_2):
        # Add the 'x' bits from the binary number
        copy_address = bin_address
        for bit in range(count):
            if bin_num & (1 << bit):
                copy_address[x_pos[bit]] = '1'
            else:
                copy_address[x_pos[bit]] = '0'

        # convert to base 10
        convert_num = 0
        for i in range(36):
            convert_num += (ord(copy_address[i]) - ord('0')) * (2 ** i)
        result.append(convert_num)
    return result


def part2():
    """
    Part 2 of the problem
    """
    f = open('input.txt', 'rt')
    mem, mask = {}, ""
    for line in f:
        if "mem" in line:
            # get every address and value from the file
            mem_address = int(line.split(' = ')[0][4:-1])
            mem_value = int(line.split(' = ')[1])

            # compute the floating address
            bin_address = []
            for i in range(36):
                if mask[35 - i] == 'X':
                    bin_address.append('X')
                elif mask[35 - i] == '0':
                    if mem_address & (1 << i):
                        bin_address.append('1')
                    else:
                        bin_address.append('0')
                else:
                    bin_address.append('1')

            # update every memory location
            for address in generate_every_code(bin_address):
                mem[address] = mem_value

        else:
            mask = line.split('=')[1].strip()
    f.close()
    return sum(mem.values())


if __name__ == '__main__':
    print("Part 1: ", part1())
    print("Part 2: ", part2())
