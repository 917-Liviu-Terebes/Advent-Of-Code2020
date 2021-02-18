/*
--- Day 23: Crab Cups ---
Strategy:
- I used an array which represents the value of the following cup and simulated the moves
(linked list using an array)
*/

#include <stdio.h>
#include <stdlib.h>

int totalCups;          // hold the total number of cups
int cups[1000001];      // holds the value of the cup right of it
int cursor;             // where the crab is

int input_cups[9] = {5, 8, 3, 9, 7, 6, 2, 4, 1};

void initialize_cups(int total)
{
    // Place the first 9 cups in order
    totalCups = total;
    for (int i = 0; i < 8; ++i)
        cups[input_cups[i]] = input_cups[i + 1];

    // Also place the other million cups and set the last one
    if (totalCups > 9)
    {
        cups[input_cups[8]] = 10;
        for (int i = 10; i < totalCups; ++i)
            cups[i] = i + 1;
        cups[totalCups] = input_cups[0];
    }
    else
        cups[input_cups[8]] = input_cups[0];
    // Set the cursor
    cursor = input_cups[0];
}

void step()
{
    // Get the cups which will be moved
    int p1 = cups[cursor];
    int p2 = cups[p1];
    int p3 = cups[p2];

    // Compute the destination
    int dest = cursor;
    while (dest == cursor || dest == p1 || dest == p2 || dest == p3)
        dest = dest - 1 == 0 ? totalCups : dest - 1;

    // Place the cups at the destination and update the links
    int destNext = cups[dest];
    cups[cursor] = cups[p3];
    cups[dest] = p1;
    cups[p3] = destNext;

    cursor = cups[cursor];
}

void print_part1()
{
    // Print the result for part 1 of the problem
    printf("Part 1: ");
    int current = 1;
    for (int i = 0; i < 8; ++i)
    {
        printf("%lu", cups[current]);
        current = cups[current];
    }
    printf("\n");
}

int main()
{
    // Part 1
    // Set up 9 cups and simulate 100 moves
    initialize_cups(9);
    for (int i = 0; i < 100; ++i)
        step();
    print_part1();

    // Part 2
    // Set up 1 million cups and simulate 10 million moves
    initialize_cups(1000000);
    for (int i = 0; i < 10000000; ++i)
        step();
    printf("Part 2: %llu\n", 1LL * cups[1] * cups[cups[1]]);

    return 0;
}
