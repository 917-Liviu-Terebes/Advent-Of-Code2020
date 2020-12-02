#include <bits/stdc++.h>
#define NUM 100
using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");

int main()
{
    int passcounter = 0;
    char input_line[NUM];
    while(f.getline(input_line, NUM))
    {
        // read each line and convert it to needed data
        char *delim = ": -";
        char *tokens = strtok(input_line, delim);
        // data
        int start_val, end_val;
        char letter;
        char password[NUM];

        for(int i = 0; i < 4; ++i)
        {
            switch(i)
            {
                case 0: start_val = atoi(tokens); break;
                case 1: end_val = atoi(tokens); break;
                case 2: letter = tokens[0]; break;
                case 3: strcpy(password, tokens); break;
            }

            tokens = strtok(NULL, delim);
        }

        // checking if the password is correct part 1
        /*
        int counter = 0;
        for(int i = 0; i < strlen(password); ++i)
            if(password[i] == letter)
                counter++;
        if(counter >= start_val && counter <= end_val)
            passcounter++;
        */
        // part 2
        int counter = 0;
        counter += (start_val - 1 < strlen(password) ? password[start_val-1] == letter : 0);
        counter += (end_val - 1 < strlen(password) ? password[end_val-1] == letter : 0);
        if(counter == 1)
            passcounter++;
    }
    g << passcounter;
}
