/*
Day 17
Sorry but most of the comments are in the 6th dimension
Also Rest in Peace Conway, you were a great man
*/

#include <bits/stdc++.h>
#define OFFSET 20
using namespace std;

typedef long long lint;
char conway[2 * OFFSET][2 * OFFSET][2 * OFFSET][2 * OFFSET];
char new_state[2 * OFFSET][2 * OFFSET][2 * OFFSET][2 * OFFSET];
char inp;

char get_conway(int x, int y, int z, int w)
{
    return conway[x + OFFSET][y + OFFSET][z + OFFSET][w + OFFSET];
}

int count_neighbours(int i, int j, int k, int w)
{
    int counter = 0;
    for(int nx = i-1; nx <= i+1; ++nx)
        for(int ny = j-1; ny <= j+1; ++ny)
            for(int nz = k-1; nz <= k+1; ++nz)
                for(int nw = w-1; nw <= w+1; ++nw)
                {
                    if(get_conway(nx, ny, nz, nw))
                        counter++;
                }
    return counter;
}

void copy_state(int cycle_range)
{
    for(int i = 1 - cycle_range; i <= 9 + cycle_range; ++i)
        for(int j = 1 - cycle_range; j <= 9 + cycle_range; ++j)
            for(int k = -cycle_range; k <= cycle_range; ++k)
                for(int w = -cycle_range; w <= cycle_range; ++w)
                    conway[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET];
}

void reset_state()
{
    memset(new_state, 0, sizeof(char) * OFFSET * OFFSET * OFFSET * OFFSET);
}

int main()
{
    ifstream f("input.txt");
    for(int i = 1; i <= 8; ++i)
        for(int j = 1; j <= 8; ++j)
        {
            f >> inp;
            if(inp == '#')
                conway[i+OFFSET][j+OFFSET][OFFSET][OFFSET] = 1;
        }
    int cycle_range = 1;
    while(cycle_range <= 6)
    {
        reset_state();
        for(int i = 1-cycle_range; i <= 9+cycle_range; ++i)
            for(int j = 1-cycle_range; j <= 9+cycle_range; ++j)
                for(int k = -cycle_range; k <= cycle_range; ++k)
                    for(int w = -cycle_range; w <= cycle_range; ++w)
                    {
                        int counter = count_neighbours(i, j, k, w);
                        if(get_conway(i, j, k, w) == 1 && (counter == 3 || counter == 4))
                            new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = 1;
                        else if(get_conway(i, j, k, w) == 0 && counter == 3)
                            new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = 1;
                        else new_state[i + OFFSET][j + OFFSET][k + OFFSET][w + OFFSET] = 0;
                    }
        copy_state(cycle_range);
        cycle_range++;
    }
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

    cout << "Part 1: " << (counter_part1 - 21) / 7 << '\n';
    cout << "Part 2: " << counter_part2;
}
