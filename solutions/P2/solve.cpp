#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream infile("input.txt");

    if (!infile)
    {
        cerr << "Error opening file" << endl;
        return 1;
    }

    int T;
    infile >> T;
    for (int c = 1; c <= T; c++)
    {
        int ret = 0;
        int N, B;
        infile >> N >> B;
        vector<int> A(N);
        for (int i = 0; i < N; i++)
        {
            infile >> A[i]; // Read the prices of the houses from the file
        }
        sort(A.begin(), A.end()); // Sort the house prices in ascending order
        for (int i = 0; i < N; i++)
        {
            if (A[i] <= B)
            {              // If the current house price is within the budget
                B -= A[i]; // Deduct the house price from the budget
                ret++;     // Increment the count of houses bought
            }
            else
            {
                break; // If the current house price exceeds the budget, break the loop
            }
        }
        cout << "Case #" << c << ": " << ret << endl; // Print the result for the current test case
    }

    infile.close(); // Close the file
    return 0;
}
