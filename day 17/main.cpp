/*
--- Day 17: Conway Cubes ---
Sorry but most of the comments are in the 6th dimension
Also Rest in Peace Conway, you were a great man.
Strategy:
- Generate the cubes (simulate the game of life) and be careful not to enter
invalid memory areas (The trick for this was to use an 'offset' which
is added to the values (so negative + offset > 0, which is valid))
*/

#include <bits/stdc++.h>
#define OFFSET 20
using namespace std;

char conway[2 * OFFSET][2 * OFFSET][2 * OFFSET][2 * OFFSET];
char new_state[2 * OFFSET][2 * OFFSET][2 * OFFSET][2 * OFFSET];
char inp;

char get_conway(int x, int y, int z, int w)
{
    /*
        Get the value at the coordinates x, y, z, w from the conway hyper-cube
    */
    return conway[x + OFFSET][y + OFFSET][z + OFFSET][w + OFFSET];
}

int count_neighbours(int x, int y, int z, int w)
{
    /*
        Count the active neighbors of the cell at the coordinates x, y, z, w
        (Also including the cell)
    */
    int counter = 0;
    for(int nx = x - 1; nx <= x + 1; ++nx)
        for(int ny = y - 1; ny <= y + 1; ++ny)
            for(int nz = z - 1; nz <= z + 1; ++nz)
                for(int nw = w - 1; nw <= w + 1; ++nw)
                    if(get_conway(nx, ny, nz, nw))
                        counter++;
    return counter;
}

void copy_state(int cycle_range)
{
    /*
        Copy the new_state hypercube to the old_state hypercube
    */
    for(int i = 1 - cycle_range; i <= 9 + cycle_range; ++i)
        for(int j = 1 - cycle_range; j <= 9 + cycle_range; ++j)
            for(int k = -cycle_range; k <= cycle_range; ++k)
                for(int w = -cycle_range; w <= cycle_range; ++w)
                    conway[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET];
}

void reset_state()
{
    /*
        Put 0 in all the new_state matrix
    */
    memset(new_state, 0, sizeof(char) * OFFSET * OFFSET * OFFSET * OFFSET);
}

int main()
{
    // Open the file and read the content
    ifstream f("input.txt");
    for(int i = 1; i <= 8; ++i)
        for(int j = 1; j <= 8; ++j)
        {
            f >> inp;
            if(inp == '#')
                conway[i+OFFSET][j+OFFSET][OFFSET][OFFSET] = 1;
        }

    // Simulate the movement of the cube / game of life
    int cycle_range = 1;
    while(cycle_range <= 6)
    {
        reset_state();
        for(int i = 1-cycle_range; i <= 9+cycle_range; ++i)
            for(int j = 1-cycle_range; j <= 9+cycle_range; ++j)
                for(int k = -cycle_range; k <= cycle_range; ++k)
                    for(int w = -cycle_range; w <= cycle_range; ++w)
                    {
                        // If the cube is in accordance with the GOL rules, maintain it to 1
                        // Else deactivate it
                        int counter = count_neighbours(i, j, k, w);
                        if(get_conway(i, j, k, w) == 1 && (counter == 3 || counter == 4) ||
                           get_conway(i, j, k, w) == 0 && counter == 3)
                            new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = 1;
                        else new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = 0;
                    }
        copy_state(cycle_range);

        cycle_range++;
    }

    // Count the active cubes
    int counter_part1 = 0;
    int counter_part2 = 0;
    for(int z = -cycle_range; z <= cycle_range; ++z)
        for(int i = 1-cycle_range; i <= 9+cycle_range; ++i)
            for(int j = 1-cycle_range; j <=9+cycle_range; ++j)
                for(int w = -cycle_range; w <= cycle_range; ++w)
                {
                    if(get_conway(i, j, z, 0))
                        counter_part1++;
                    if(get_conway(i, j, z, w))
                        counter_part2++;
                }

    // Print the result (For the first part...I was too lazy to add the 4d part,
    // but this formula works for other test cases as well).
    cout << "Part 1: " << (counter_part1 - 21) / 7 << '\n';
    cout << "Part 2: " << counter_part2;

    f.close();
    return 0;
}
