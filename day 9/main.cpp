/*
--- Day 9: Encoding Error ---
Strategy:
- For part 1, find the error number by finding two neighbors so that the sum is correct
- For part 2, Modulo thing-y or
*/

#include <bits/stdc++.h>
#define PRE 25
#define MAXLENGTH 1100
using namespace std;

typedef long long lint;
lint input_num[MAXLENGTH];
lint partsum[MAXLENGTH];

int part1()
{
    // Part 1 of the problem
    for(int i = 26; i <= 1000; ++i)
    {
        int ok = 0;
        // Search the neighbors such that the sum is the number
        for(int j = i - 25; j <= i && !ok; ++j)
            for(int k = i - 25; k <= i && !ok; ++k)
            {
                if(input_num[j] != input_num[k] && (input_num[j] + input_num[k] == input_num[i]))
                    ok = 1;
            }
        // If the sum cannot be found, return the number
        if(!ok)
            return input_num[i];
    }
}

/*
int part2_modulo()
{
    // Don't mind this O(N^2) solution for part 2
    // I was thinking with modulo
    for(int i = 1; i <= 1000; ++i)
        partsum[i] = (partsum[i - 1] + input_num[i]) % 552655238;
    for(int i = 1; i <= 1000; ++i)
        for(int j = i + 1; j <= 1000; ++j)
            if(partsum[i] == partsum[j])
            {
                lint minim = 552655238;
                lint maxim = 0;
                for(int k = i; k <= j; ++k)
                {
                    if(input_num[k] > maxim)
                        maxim = input_num[k];
                    else if(input_num[k] < minim)
                        minim = input_num[k];
                }
                return minim + maxim;
            }
}
*/

int part2(int searched_value)
{
    // Part 2 of the problem
    // Efficient O(N) algorithm for part 2 (Thinking with 2-pointer method)

    // Basically, keep the sum of the elements between the index start and i
    // If the sum is bigger than the searched value, subtract the first elements from the
    // starting positions (start, start + 1, etc) until the sum is smaller or equal to the
    // searched value. Then find the minimum and maximum

    lint current_sum = input_num[1];
    int start = 1;
    for(int i = 2; i <= 1000; ++i)
    {
        // Subtract first elements from the sum if it is bigger than the searched value
        while(current_sum > searched_value && start < i - 1)
            current_sum -= input_num[start++];

        // We found the sum, yeah
        if(current_sum == searched_value)
        {
            // Now find the min and max
            lint minimum = searched_value;
            lint maximum = 0;

            for(int k = start; k < i; ++k)
            {
                if(input_num[k] > maximum)
                    maximum = input_num[k];
                else if(input_num[k] < minimum)
                    minimum = input_num[k];
            }

            return minimum + maximum;
        }

        // Add the current number to the sum
        current_sum += input_num[i];
    }
}

int main()
{
    ifstream f("input.txt");

    // Read the numbers from the file
    for(int i = 1; i <= 1000; ++i)
        f >> input_num[i];

    cout << "Part 1: " << part1() << "\n";
    cout << "Part 2: " << part2(part1()) << "\n";

    f.close();
    return 0;
}
