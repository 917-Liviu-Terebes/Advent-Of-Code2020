#include <stdio.h>
#include <stdlib.h>

int main()
{
    int map_seats[950];
    memset(map_seats, 0, sizeof(map_seats));
    char seat_string[11];
    FILE *f;
    f = fopen("input.in", "r");
    int maximum = 0;
    while (fscanf(f, "%s", seat_string) != EOF)
    {
        // get the row
        int row = 0;
        int string_index = 0;
        for(int i = 6; i >= 0; --i)
            row += ((seat_string[string_index++] == 'B' ? 1 : 0) << i);

        // get the column
        int column = 0;
        for(int i = 2; i >= 0; --i)
            column += ((seat_string[string_index++] == 'R' ? 1 : 0) << i);
        map_seats[row * 8 + column] = 1;
        //maximum = (maximum > row * 8 + column ? maximum : row * 8 + column);
    }
    // for part 1
    //printf("%d", maximum);

    // for part 2
    for(int i = 1; i < 940; ++i)
    {
        if(!map_seats[i] && map_seats[i - 1] && map_seats[i + 1])
            printf("%d\n", i);
    }
    return 0;
}
