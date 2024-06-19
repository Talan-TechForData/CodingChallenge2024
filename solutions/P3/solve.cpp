#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#define FOR(k, n) for (int k = 0; k < (n); ++k)

const int d4i[4] = {-1, 0, 1, 0}, d4j[4] = {0, 1, 0, -1};
const int d8i[8] = {-1, -1, 0, 1, 1, 1, 0, -1}, d8j[8] = {0, 1, 1, 1, 0, -1, -1, -1};

long long dp[400][400][400];

long long solve_case(std::ifstream &infile)
{
    int n, d;
    infile >> n >> d;
    std::vector<int> v(n);
    for (int i = 0; i < n; ++i)
        infile >> v[i];

    for (int i = n - 1; i >= 0; --i)
    {
        FOR(k, n)
        {
            dp[i][i][k] = std::min((v[i] + d - v[k]) % d, d - (v[i] + d - v[k]) % d);
        }
        for (int j = i + 1; j < n; ++j)
        {
            FOR(k, n)
            {
                dp[i][j][k] = dp[i][j - 1][j] + std::min((v[j] + d - v[k]) % d, d - (v[j] + d - v[k]) % d);
                dp[i][j][k] = std::min(dp[i][j][k], dp[i + 1][j][i] + std::min((v[i] + d - v[k]) % d, d - (v[i] + d - v[k]) % d));
            }
        }
    }

    long long result = std::min(dp[0][n - 1][n - 1] + v[n - 1], dp[0][n - 1][n - 1] + d - v[n - 1]);
    result = std::min(result, dp[0][n - 1][0] + v[0]);
    result = std::min(result, dp[0][n - 1][0] + d - v[0]);

    return result;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    { // Check if the number of arguments is correct
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }

    std::ifstream infile(argv[1]); // Open the input file
    if (!infile)
    { // Check if the file was successfully opened
        std::cerr << "Error opening input file " << argv[1] << std::endl;
        return 1;
    }

    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    int t;
    infile >> t; // Read the number of test cases

    for (int i = 1; i <= t; ++i)
    {
        long long result = solve_case(infile);
        std::cout << "Test " << i << ": " << result << "\n";
    }

    return 0;
}
