"""
--- Day 12: Rain Risk ---
Strategy:
- We represent coordinates and direction on a complex plane.
This way, the rotations are achieved by multiplying by i or -i.
"""


def execute_commands(commands, part_2=True):
    """
    Executes the command list
    :param commands: List of commands (List of strings)
    :param part_2: Is part 2?
    """
    # Compass with directions
    simple_compass = {'N': 0 + 1j, 'S': 0 - 1j, 'W': -1 + 0j, 'E': 1 + 0j}
    ship_pos = 0 + 0j
    # Facing east
    direction = 1 + 0j
    # Waypoint for part 2
    waypoint = 10 + 1j

    for line in commands:
        # Get the command and argument
        command = line[0]
        data = int(line[1:])

        if command in simple_compass:
            # Add the vector of the command direction multiplied by the argument
            if part_2:
                waypoint += simple_compass[command] * data
            else:
                ship_pos += simple_compass[command] * data

        elif command == 'R':
            # Each clockwise 90 degree turn is equivalent to multiplying the complex number by -i
            turns = data // 90
            for _ in range(turns):
                if part_2:
                    waypoint *= -1j
                else:
                    direction *= -1j
        elif command == 'L':
            # Each counterclockwise 90 degree turn is equivalent to multiplying the complex number by i
            turns = data // 90
            for _ in range(turns):
                if part_2:
                    waypoint *= 1j
                else:
                    direction *= 1j
        elif command == 'F':
            # Go in the direction
            if part_2:
                ship_pos += waypoint * data
            else:
                ship_pos += direction * data

    return int(abs(ship_pos.real) + abs(ship_pos.imag))


def part1(input_lines):
    """
    The first part of the problem
    """
    return execute_commands(input_lines, False)


def part2(input_lines):
    """
    The second part of the problem
    """
    return execute_commands(input_lines)


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    input_files = [line.strip() for line in f]

    print("Part 1: ", part1(input_files))
    print("Part 2: ", part2(input_files))

    f.close()