# Day 12
# Each vector is represented as a complex number
f = open('input.txt', 'rt')
f = [line.strip() for line in f]

if __name__ == '__main__':
    # Compass with directions
    simple_compass = {'N': 0 + 1j, 'S': 0 - 1j, 'W': -1 + 0j, 'E': 1 + 0j}
    ship_pos = 0 + 0j
    # facing east
    direction = 1 + 0j

    for line in f:
        # Get the command and argument
        command = line[0]
        data = int(line[1:])

        if command in simple_compass:
            # just add the vector of the command direction multiplied by the argument
            ship_pos += simple_compass[command] * data
        elif command == 'R':
            # each clockwise 90 degree turn is equivalent to multiplying the complex number by -i
            turns = data // 90
            for _ in range(turns):
                direction *= -1j
        elif command == 'L':
            # each counterclockwise 90 degree turn is equivalent to multiplying the complex number by i
            turns = data // 90
            for _ in range(turns):
                direction *= 1j
        elif command == 'F':
            # go in the direction
            ship_pos += direction * data
    # print(dir_x, dir_y)
    print("Part 1", abs(ship_pos.real) + abs(ship_pos.imag))

    ship_pos = 0 + 0j
    waypoint = 10 + 1j

    for line in f:
        # Get the command and argument
        command = line[0]
        data = int(line[1:])

        # the direction is replaced by the waypoint
        if command in simple_compass:
            waypoint += simple_compass[command] * data
        elif command == 'R':
            turns = data // 90
            for _ in range(turns):
                waypoint *= -1j
        elif command == 'L':
            turns = data // 90
            for _ in range(turns):
                waypoint *= 1j
        elif command == 'F':
            # go in the direction of the waypoint
            ship_pos += waypoint * data
    # print(dir_x, dir_y)
    print("Part 2", abs(ship_pos.real) + abs(ship_pos.imag))