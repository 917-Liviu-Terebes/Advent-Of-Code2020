/*
--- Day 5: Binary Boarding ---
Strategy:
- You can look at each of the seat codes like a binary number. RB are the 1 bit
Using bitwise operators, you get the position of each code.
(For part 2 you also need a hashing (frequency) table.)
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
    // Table for the seats (initialized with 0. If a seat is occupied, set the value to 1)
    int map_seats[950];
    memset(map_seats, 0, sizeof(map_seats));


    char seat_string[15];   // String to read the input
    int maximum = 0;        // Maximum seat ID for part 1

    FILE *f;
    f = fopen("input.in", "r");

    // Read each line from the file
    while (fgets(seat_string, 11, f) != NULL)
    {
        /*
        eg: FBFBBFF  (replace F with 0 and B with 1)
        ->  0101100 = 44 in decimal (the row value we need)
        */

        // Find the row of the seat
        int row = 0;
        int string_index = 0;
        for(int i = 6; i >= 0; --i)
            row += ((seat_string[string_index++] == 'B' ? 1 : 0) << i);

        // Find the column of the seat
        int column = 0;
        for(int i = 2; i >= 0; --i)
            column += ((seat_string[string_index++] == 'R' ? 1 : 0) << i);

        // Mark the seat
        map_seats[row * 8 + column] = 1;

        // Check for maximum
        maximum = (maximum > row * 8 + column ? maximum : row * 8 + column);
    }

    // Part 1 result
    printf("Part 1: %d\n", maximum);

    // Part 2 result
    // Print the seat such that the adjacent ones are occupied
    for(int i = 1; i < 940; ++i)
    {
        if(!map_seats[i] && map_seats[i - 1] && map_seats[i + 1])
            printf("Part 2: %d\n", i);
    }

    fclose(f);
    return 0;
}
