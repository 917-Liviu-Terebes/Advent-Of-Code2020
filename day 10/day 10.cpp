/*
--- Day 10: Adapter Array ---
Strategy:
- Dynamic Programming approach
*/

#include <bits/stdc++.h>
#define MAXLEN 150

int inp[MAXLEN];
int n, count1, count3;
typedef long long lint;
lint dp[MAXLEN];

using namespace std;

lint count_ways(int i)
{
    // DP memoization solution
    // dp[i] = number of ways to use adapters if I start from the i-th adapter

    // dp[n] is 1 because we can only use the last adapter
    if(i == n)
        return 1;
    // Use memorized value, if it exists
    if(dp[i])
        return dp[i];
    // If not, we compute id
    for(int j = i + 1; j <= n && (inp[j] - inp[i] <= 3); ++j)
    {
        // If we find an adapter with a difference less than 3 in the following set
        // of adapters, we just add the number of ways to use the adapters, starting
        // from that one
        if(inp[j] - inp[i] <= 3)
            dp[i] += count_ways(j);
    }

    return dp[i];
}


int main()
{
    ifstream f("input.txt");

    // Read the input and sort it
    while(f >> inp[++n]);
    sort(inp + 1, inp + n + 1);

    // Part 1
    for(int i = 1; i <= n; ++i)
    {
        // Count every 1/3 difference between numbers
        if((inp[i + 1] - inp[i]) == 1)
            count1++;
        else if((inp[i + 1] - inp[i]) == 3)
            count3++;
    }
    count3++;   // Special case

    cout << "Part 1: " << count1 * count3 << '\n';

    // Part 2
    cout << "Part 2: " << count_ways(1);

    f.close();
    return 0;
}
