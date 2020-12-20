/*
Part 1 code
#include <bits/stdc++.h>
#define N 10
using namespace std;
typedef long long lint;

struct tile
{
    int id;
    vector<string> mat;
    void flip()
    {
        for(int i = 0; i < N; ++i)
            for(int l = 0, r = N - 1; l < r; ++l, --r)
                swap(mat[i][l], mat[i][r]);
    }
    void rotate()
    {
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

vector<tile*> tiles;
vector<pair<int, int>> index;
lint result = 1;
int used[15][15];

int matching_edges(int i, int j)
{
    if(i > 0)
    {
        for(int k = 0; k < N; ++k)
        {
            if(!(tiles[used[i][j]]->mat[0][k] == tiles[used[i - 1][j]]->mat[N - 1][k]))
                return 0;
        }
    }
    if(j > 0)
    {
        for(int k = 0; k < N; ++k)
        {
            if(!(tiles[used[i][j]]->mat[k][0] == tiles[used[i][j - 1]]->mat[k][N - 1]))
                return 0;
        }
    }
    return 1;
}

lint bkt(int i, int j)
{
    if (i >= 12)
    {
        lint res = 1;
        res *= tiles[used[0][11]]->id;
        res *= tiles[used[11][11]]->id;
        res *= tiles[used[11][0]]->id;
        res *= tiles[used[0][0]]->id;
        return res;
    }
    if (j >= 12)
        return bkt(i + 1, 0);
    for (int ii = 0; ii < 144; ++ii)
    {
        if(index[ii].first >= 0)
            continue;
        index[ii] = make_pair(i, j);
        used[i][j] = ii;
        for (int x = 0; x < 2; ++x, tiles[ii]->flip())
            for (int y = 0; y < 4; ++y, tiles[ii]->rotate())
            {
                if(!matching_edges(i, j))
                    continue;
                lint res = bkt(i, j + 1);
                if(res < 0)
                    continue;
                return res;
            }
        index[ii] = make_pair(-1, -1);
    }
    return -1;
}


int main()
{
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
    cout << bkt(0, 0);
}
*/


// Part 2
#include <bits/stdc++.h>
#define N 10
using namespace std;
typedef long long lint;

struct tile
{
    int id;
    vector<string> mat;
    void flip()
    {
        for(int i = 0; i < N; ++i)
            for(int l = 0, r = N - 1; l < r; ++l, --r)
                swap(mat[i][l], mat[i][r]);
    }
    void rotate()
    {
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

vector<tile*> tiles;
vector<pair<int, int>> index;
vector<string> seaMonster;
vector<string> img;
lint result = 1;
int used[15][15];

void make_img()
{
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
    if(i > 0)
    {
        for(int k = 0; k < N; ++k)
        {
            if(!(tiles[used[i][j]]->mat[0][k] == tiles[used[i - 1][j]]->mat[N - 1][k]))
                return 0;
        }
    }
    if(j > 0)
    {
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
    int cnt = 0;
    for(int i = 0; i < (int)img.size(); ++i)
        for(int j = 0; j < (int)img.size(); ++j)
            cnt += check_sea_monster(i, j);
    return cnt;
}

lint bkt(int i, int j)
{
    if (i >= 12)
    {
        make_img();
        int re = sea_monsters_counter();
        if(!re)
            return -1;
        int cnt = 0;
        for(auto s: img)
            for(auto c: s)
                cnt += (c == '#');
        return 0LL + cnt - re * 15LL;
    }
    if (j >= 12)
        return bkt(i + 1, 0);
    for (int ii = 0; ii < 144; ++ii)
    {
        if(index[ii].first >= 0)
            continue;
        index[ii] = make_pair(i, j);
        used[i][j] = ii;
        for (int x = 0; x < 2; ++x, tiles[ii]->flip())
            for (int y = 0; y < 4; ++y, tiles[ii]->rotate())
            {
                if(!matching_edges(i, j))
                    continue;
                lint res = bkt(i, j + 1);
                if(res < 0)
                    continue;
                return res;
            }
        index[ii] = make_pair(-1, -1);
    }
    return -1;
}


int main()
{
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
    cout << bkt(0, 0);
}
