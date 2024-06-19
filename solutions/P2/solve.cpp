#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc != 2)
    { // Check if the number of arguments is correct
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    ifstream infile(argv[1]); // Open the file named "input.txt"

    if (!infile)
    { // Check if the file was successfully opened
        cerr << "Error opening file" << argv[1] << endl;
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
        cout << "Test " << c << ": " << ret << endl; // Print the result for the current test case
    }

    infile.close(); // Close the file
    return 0;
}
