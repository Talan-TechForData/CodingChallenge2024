#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

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

    string line;
    int c = 1;

    while (getline(infile, line))
    { // Read each line from the file
        istringstream iss(line);
        int N;

        iss >> N; // Read the number of samples from the line
        vector<int> samples(N);
        for (int i = 0; i < N; i++)
        {
            iss >> samples[i]; // Read the samples from the line
        }

        int peaks = 0;
        for (int i = 1; i < N - 1; i++)
        {
            if (samples[i] > samples[i - 1] && samples[i] > samples[i + 1])
            {
                peaks++;
            }
        }

        cout << "Case #" << c << ": " << peaks << endl; // Print the result for the current line
        c++;                                            // Increment the case number
    }

    infile.close(); // Close the file
    return 0;
}
