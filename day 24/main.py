"""
--- Day 24: Lobby Layout ---
- Strategy:
For part 1, calculate each position and use a set to remember the tiles. Use a hex grid representation
For part 2, play the game of life, using the tiles in a set representation
"""


def part1():
    """
    Part 1 of the problem
    """
    black_tiles = set()     # Use a set to keep the tiles

    for line in lines:
        # I used the (x, y, z) representation from here
        # https://www.redblobgames.com/grids/hexagons/
        x, y, z = 0, 0, 0

        while line:
            if line.startswith('e'):
                x += 1
                y -= 1
                line = line[1:]
            elif line.startswith('se'):
                y -= 1
                z += 1
                line = line[2:]
            elif line.startswith('sw'):
                x -= 1
                z += 1
                line = line[2:]
            elif line.startswith('w'):
                x -= 1
                y += 1
                line = line[1:]
            elif line.startswith('nw'):
                z -= 1
                y += 1
                line = line[2:]
            elif line.startswith('ne'):
                x += 1
                z -= 1
                line = line[2:]
            else:
                assert False

        # Add/Remove the tile, according to the rules
        if (x, y, z) in black_tiles:
            black_tiles.remove((x, y, z))
        else:
            black_tiles.add((x, y, z))

    return black_tiles


def part2(black_tiles):
    """
    Part 2 of the problem
    :param black_tiles: Set of tiles coordinates
    """
    # Simulate 100 days
    for _ in range(100):
        new_black_tiles = set()         # Set to keep the black tiles from the next day
        possible_tiles = set()          # Set to keep the tiles and neighboring ones, for checking

        for (x, y, z) in black_tiles:
            # Add each black tile and its neighbours
            possible_tiles.add((x, y, z))
            for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                possible_tiles.add((x + dx, y + dy, z + dz))

        for (x, y, z) in possible_tiles:
            neighbor_number = 0         # Counter for neighbors

            for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                if (x + dx, y + dy, z + dz) in black_tiles:
                    neighbor_number += 1

            # Add only the tiles which respect the Game of Life rule
            if (x, y, z) in black_tiles and (neighbor_number == 1 or neighbor_number == 2):
                new_black_tiles.add((x, y, z))
            if (x, y, z) not in black_tiles and neighbor_number == 2:
                new_black_tiles.add((x, y, z))
        # Update the old set with the new one
        black_tiles = new_black_tiles

    return len(black_tiles)


if __name__ == '__main__':
    # Open the file and read the lines
    f = open('input.txt', 'rt')
    lines = f.read().strip().split('\n')
    f.close()

    part1_tiles = part1()
    print("Part 1: ", len(part1_tiles))
    print("Part 2:", part2(part1_tiles))
