f = open("input.txt", "rt")

if __name__ == '__main__':
    tree_map = []
    tree_map_copy = []
    len_line = 0
    for line in f:
        if not len_line:
            len_line = len(line)
        tree_map.append(line[:-1])
        tree_map_copy.append(line[:-1])

    counter = 0
    posx = 0
    posy = 0
    while posx != len(tree_map):
        if tree_map_copy[posx][posy] == '#':
            counter += 1
        posx += 1
        posy += 3
        posy %= 31
    print(counter)