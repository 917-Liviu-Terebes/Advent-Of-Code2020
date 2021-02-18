"""
--- Day 3: Toboggan Trajectory ---
Strategy:
- Simulating the movement and then checking every position (you don't need to copy the map to the right,
the modulo operator makes it easier and you only need a copy of the map)
"""


def simulate_moving(slope_x, slope_y):
    """
    Simulates a run through the forest if you have the slopes given as parameters
    x/y axis is rotated (x means up-down | y means left-right)
    :param slope_x: Change in x axis (Int)
    :param slope_y: Change in y axis (Int)
    :return: Number of trees hit along the run (Int)
    """
    counter = 0         # Counter for the trees
    position = (0, 0)   # Position of the sledge

    num_lines = len(tree_map)
    num_columns = len(tree_map[0])

    # Repeat until we hit the last line of the map
    while position[0] < num_lines:
        # If we hit a tree, count it
        if tree_map[position[0]][position[1]] == '#':
            counter += 1
        # Update the position (Remember than we use modulo for the y axis)
        position = (position[0] + slope_x, (position[1] + slope_y) % num_columns)

    return counter


def part1():
    """
    First part of the problem
    """
    return simulate_moving(1, 3)


def part2():
    """
    Second part of the problem
    """
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    tree_product = 1
    # For each slope, simulate a movement and multiply it to the total product
    for slope in slopes:
        tree_product *= simulate_moving(*slope)
    return tree_product


if __name__ == '__main__':
    f = open("input.txt", "rt")
    tree_map = [line.strip() for line in f.readlines()]

    print(part1())
    print(part2())
