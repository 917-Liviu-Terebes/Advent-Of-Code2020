#include <bits/stdc++.h>
#define NUM 150
char seats[NUM][NUM];
char seats_pre[NUM][NUM];
int lenx, leny;
int dx[] = {-1,-1,-1,0,1,1,1,0};
int dy[] = {-1,0,1,1,1,0,-1,-1};
using namespace std;

int equal_states()
{
    for(int i = 1; i <= lenx; ++i)
        for(int j = 1; j <= leny; ++j)
            if(seats[i][j] != seats_pre[i][j])
                return 0;
    return 1;
}

void copy_to_pre()
{
    for(int i = 1; i <= lenx; ++i)
        for(int j = 1; j <= leny; ++j)
            seats_pre[i][j] = seats[i][j];
}

void print_seats()
{
    for(int i = 1; i <= lenx; ++i)
    {
        for(int j = 1; j <= leny; ++j)
            cout << seats_pre[i][j];
        cout << '\n';
    }
    cout << '\n';
}

int check_seat_in_dir(int x, int y, int dir)
{
    int nx = x + dx[dir];
    int ny = y + dy[dir];
    while((1 <= nx && nx <= lenx) && (1 <= ny && ny <= leny))
    {
        if(seats_pre[nx][ny] == '#')
            return 1;
        if(seats_pre[nx][ny] == 'L')
            return 0;
        nx += dx[dir];
        ny += dy[dir];
    }
    return 0;
}

int main()
{
    ifstream f("input.txt");
    char line[NUM];
    while(f.getline(line, NUM))
    {
        leny = strlen(line);
        lenx++;
        for(int i = 1; i <= strlen(line); ++i)
            seats[lenx][i] = line[i - 1];
    }

    // Part 1
    /*
    while(!equal_states())
    {
        copy_to_pre();
        //print_seats();
        for(int i = 1; i <= lenx; ++i)
            for(int j = 1; j <= leny; ++j)
            {
                if(seats_pre[i][j] == 'L')
                {
                    int counter = 0;
                    for(int k = 0; k < 8; ++k)
                    {
                        if(seats_pre[i + dx[k]][j + dy[k]] == '#')
                            counter++;
                    }
                    if(counter == 0)
                        seats[i][j] = '#';
                    else
                        seats[i][j] = 'L';
                }
                else if(seats_pre[i][j] == '#')
                {
                    int counter = 0;
                    for(int k = 0; k < 8; ++k)
                    {
                        if(seats_pre[i + dx[k]][j + dy[k]] == '#')
                            counter++;
                    }
                    if(counter < 4)
                        seats[i][j] = '#';
                    else
                        seats[i][j] = 'L';
                }
                else
                    seats[i][j] = '.';
            }
    }
    */
    // Part 2
    while(!equal_states())
    {
        copy_to_pre();
        //print_seats();
        for(int i = 1; i <= lenx; ++i)
            for(int j = 1; j <= leny; ++j)
            {
                if(seats_pre[i][j] == 'L')
                {
                    int counter = 0;
                    for(int k = 0; k < 8; ++k)
                        counter += check_seat_in_dir(i, j, k);

                    if(counter == 0)
                        seats[i][j] = '#';
                    else
                        seats[i][j] = 'L';
                }
                else if(seats_pre[i][j] == '#')
                {
                    int counter = 0;
                    for(int k = 0; k < 8; ++k)
                        counter += check_seat_in_dir(i, j, k);
                    if(counter < 5)
                        seats[i][j] = '#';
                    else
                        seats[i][j] = 'L';
                }
                else
                    seats[i][j] = '.';
            }
    }
    int counter = 0;
    for(int i = 1; i <= lenx; ++i)
        for(int j = 1; j <= leny; ++j)
            if(seats[i][j] == '#')
                counter++;
    cout << counter;
}
