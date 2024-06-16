#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int min_moves_to_unlock(int N, int D, vector<int> &wheels)
{
    int moves = 0;
    int i = 0;
    while (i < N)
    {
        if (wheels[i] != 0)
        {
            // Determine the length of the current sequence of non-zero wheels
            int j = i;
            while (j < N && wheels[j] != 0)
            {
                j++;
            }

            // Move all wheels in the interval [i, j-1] to 0
            moves++;
            i = j;
        }
        else
        {
            i++;
        }
    }
    return moves;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    { // Check if the number of arguments is correct
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    ifstream infile(argv[1]); // Open the input file

    if (!infile)
    { // Check if the file was successfully opened
        cerr << "Error opening file " << argv[1] << endl;
        return 1;
    }

    int T;
    infile >> T;
    for (int t = 1; t <= T; t++)
    {
        int N, D;
        infile >> N >> D;
        vector<int> wheels(N);
        for (int i = 0; i < N; i++)
        {
            infile >> wheels[i];
        }
        int result = min_moves_to_unlock(N, D, wheels);
        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}
