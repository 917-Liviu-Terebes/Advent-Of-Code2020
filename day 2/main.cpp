/*
--- Day 2: Password Philosophy ---
Strategy:
- Split each line into components and check the password
*/

#include <bits/stdc++.h>
#define NUM 100
using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");

int main()
{
    // Counters for the problem
    int passcounter_1 = 0;
    int passcounter_2 = 0;
    char input_line[NUM];

    // Read each line from the file
    while(f.getline(input_line, NUM))
    {
        // Split the line into tokens
        char *delim = ": -";
        char *tokens = strtok(input_line, delim);
        // Data which is extracted from the tokens
        int start_val, end_val;
        char letter;
        char password[NUM];

        // Extract the data from the tokens
        for(int i = 0; i < 4; ++i)
        {
            // I guess it's easier to use switch cases here (and pretty explicit)
            switch(i)
            {
                case 0: start_val = atoi(tokens); break;
                case 1: end_val = atoi(tokens); break;
                case 2: letter = tokens[0]; break;
                case 3: strcpy(password, tokens); break;
            }
            // Get the next token
            tokens = strtok(NULL, delim);
        }

        // Part 1
        // Count the frequency of the letter
        int counter = 0;
        for(int i = 0; i < strlen(password); ++i)
            if(password[i] == letter)
                counter++;
        if(counter >= start_val && counter <= end_val)
            passcounter_1++;

        // Part 2
        // Check if the letters are in the specified places
        counter = 0;
        counter += (start_val - 1 < strlen(password) ? password[start_val-1] == letter : 0);
        counter += (end_val - 1 < strlen(password) ? password[end_val-1] == letter : 0);
        if(counter == 1)
            passcounter_2++;
    }

    g << "Part 1: " << passcounter_1 << "\nPart 2: " << passcounter_2;

    f.close();
    g.close();

    return 0;
}
