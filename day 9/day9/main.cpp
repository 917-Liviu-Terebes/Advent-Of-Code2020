#include <bits/stdc++.h>
#define PRE 25
#define MAXLENGTH 1100
using namespace std;
typedef long long lint;
lint input_num[MAXLENGTH];
lint partsum[MAXLENGTH];

int main()
{
    ifstream f("input.txt");
    for(int i = 1; i <= 1000; ++i)
        f >> input_num[i];
    /*
    // Part 1
    for(int i = 26; i <= 1000; ++i)
    {
        int ok = 0;
        for(int j = i - 25; j <= i && !ok; ++j)
            for(int k = i - 25; k <= i && !ok; ++k)
        {
            if(input_num[j] != input_num[k] && (input_num[j] + input_num[k] == input_num[i]))
                ok = 1;
        }
        if(!ok)
        {
            cout << input_num[i];
            return 0;
        }
    }*/
    /*
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
                cout << minim + maxim;
                return 0;
            }*/
    // efficient O(N) algorithm for part 2
    // thinking with 2-pointer method
    lint current_sum = input_num[1];
    int start = 1;
    for(int i = 2; i <= 1000; ++i)
    {
        // subtract first elements from the sum if it is bigger than the searched value
        while(current_sum > 552655238 && start < i - 1)
            current_sum -= input_num[start++];

        // we found the sum, yey
        if(current_sum == 552655238)
        {
            // now find the min and max
            lint minim = 552655238;
            lint maxim = 0;
            for(int k = start; k < i; ++k)
            {
                if(input_num[k] > maxim)
                    maxim = input_num[k];
                else if(input_num[k] < minim)
                    minim = input_num[k];
            }
            cout << minim + maxim;
            return 0;
        }

        current_sum += input_num[i];
    }
}
