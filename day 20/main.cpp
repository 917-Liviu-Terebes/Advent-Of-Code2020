/*
--- Day 20: Jurassic Jigsaw ---
Strategy:
- Use backtracking to put the pieces together, then scan for the monster.
*/

#include <bits/stdc++.h>
#define N 10
using namespace std;
typedef long long lint;
struct tile
{
    // Tile structure/class which holds a tile (it can flip or rotate it)
    int id;
    vector<string> mat;

    void flip()
    {
        // Flip the matrix
        for(int i = 0; i < N; ++i)
            for(int left = 0, right = N - 1; left < right; ++left, --right)
                swap(mat[i][left], mat[i][right]);
    }

    void rotate()
    {
        // Rotate the matrix
        vector<string> mat2 = mat;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
            {
                int ni = N - 1 - j, nj = i;
                mat2[ni][nj] = mat[i][j];
            }
        mat.swap(mat2);
    }
};

// Global variables to store the data
// I couldn't think of making them local, sorry refactoring
vector<tile*> tiles;                // Vector to store pointers to tiles
vector<pair<int, int>> index;       // Vector to store indexes of each tile
vector<string> seaMonster;          // Vector to store the sea monster image
vector<string> img;                 // Vector to store the image
lint result = 1;
int used[15][15];
int part1 = 1;

void make_img()
{
    /*
        Create the image using the current tiles placement
    */
    img.clear();
    for(int line = 0; line < 12; ++line)
        for(int i = 1; i < 9; ++i)
        {
            string s;
            for(int col = 0; col < 12; ++col)
                for(int j = 1; j < 9; ++j)
                    s += tiles[used[line][col]] -> mat[i][j];
            img.push_back(s);
        }
}

int matching_edges(int i, int j)
{
    /*
        Check if the tile on position (i, j) matches the neighbor tiles
    */
    if(i > 0)
    {
        // Check the tile above it
        for(int k = 0; k < N; ++k)
        {
            if(!(tiles[used[i][j]]->mat[0][k] == tiles[used[i - 1][j]]->mat[N - 1][k]))
                return 0;
        }
    }
    if(j > 0)
    {
        // Check the tile left of it
        for(int k = 0; k < N; ++k)
        {
            if(!(tiles[used[i][j]]->mat[k][0] == tiles[used[i][j - 1]]->mat[k][N - 1]))
                return 0;
        }
    }
    return 1;
}

int check_sea_monster(int x, int y)
{
    /*
        Check if there is a sea monster at position (x, y) in the image
    */
    for(int i = 0; i < 3; ++i)
        for(int j = 0; j < (int)seaMonster[i].size(); ++j)
        {
            if(seaMonster[i][j] == ' ')
                continue;
            if(x + i >= (int)img.size())
                return 0;
            if(y + j >= (int)img.size())
                return 0;
            if(img[x + i][y + j] != seaMonster[i][j])
                return 0;
        }
    return 1;
}

int sea_monsters_counter()
{
    /*
        Count the number of sea monsters in the image
    */
    int cnt = 0;
    for(int i = 0; i < (int)img.size(); ++i)
        for(int j = 0; j < (int)img.size(); ++j)
            cnt += check_sea_monster(i, j);
    return cnt;
}

lint bkt(int i, int j)
{
    /*
        Backtracking procedure to place the tiles
    */
    if (i >= 12)
    {
        if(part1)
        {
            // Compute the product and return it
            lint res = 1;
            res *= tiles[used[0][11]]->id;
            res *= tiles[used[11][11]]->id;
            res *= tiles[used[11][0]]->id;
            res *= tiles[used[0][0]]->id;
            return res;
        }
        else
        {
            // Create the image and count the sea monsters
            make_img();
            int re = sea_monsters_counter();
            if(!re)
                return -1;
            int cnt = 0;
            for(auto s: img)
                for(auto c: s)
                    cnt += (c == '#');
            // Return the result
            return 0LL + cnt - re * 15LL;
        }
    }
    if (j >= 12)
        return bkt(i + 1, 0);

    for (int ii = 0; ii < 144; ++ii)
    {
        // Try every tile available, that was not placed before
        if(index[ii].first >= 0)
            continue;

        // Place the tile
        index[ii] = make_pair(i, j);
        used[i][j] = ii;

        // Rotate and flip in every way the tile and go to the next
        // backtracking stage, if possible
        for (int x = 0; x < 2; ++x, tiles[ii]->flip())
            for (int y = 0; y < 4; ++y, tiles[ii]->rotate())
            {
                // If the tile doesn't match the neighbors, skip
                if(!matching_edges(i, j))
                    continue;

                lint res = bkt(i, j + 1);

                if(res < 0)
                    continue;

                // Maybe we have a result
                return res;
            }

        // De-place (?) the tile
        index[ii] = make_pair(-1, -1);
    }

    return -1;
}

int main()
{
    // Save the monster
    seaMonster.push_back("                  # ");
    seaMonster.push_back("#    ##    ##    ###");
    seaMonster.push_back(" #  #  #  #  #  #   ");

    ifstream f("input.txt");

    // Reading all the tiles
    for(int i = 0; i < 144; ++i)
    {
        int id;
        vector<string> inp_mat;
        string inp_line;

        // Read id
        f >> inp_line >> id;
        f >> inp_line;

        // Reading the tile
        for(int j = 0; j < 10; ++j)
        {
            f >> inp_line;
            inp_mat.push_back(inp_line);
        }

        // Save the id and tile
        tiles.push_back(new tile());
        tiles[i]->id = id;
        tiles[i]->mat = inp_mat;
    }

    index.resize(tiles.size(), make_pair(-1, -1));

    cout << "Part 1: " << bkt(0, 0) << "\n";
    // Clear for part 2
    part1 = 0;
    index.clear();
    index.resize(tiles.size(), make_pair(-1, -1));
    cout << "Part 2: " << bkt(0, 0) << "\n";

    f.close();
    return 0;
}
