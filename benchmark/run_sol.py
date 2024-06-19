import os
import subprocess
import time
import pandas as pd
from pathlib import Path
import argparse

# Define the base directory where compiled C++ files are located
base_directory = Path(__file__).parent / "../solutions"
cpp_ext = '.cpp'

# Define mappings for input and output paths based on problem directories
MAP = {
    "P1": "data/P1/input.txt",
    "P2": "data/P2/input.txt",
    "P3": "data/P3/input.txt"
}

MAP_OUTPUTS = {
    "P1": "data/P1/",
    "P2": "data/P2/",
    "P3": "data/P3/"
}

def main(execute_clean_script):
    results = []

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(cpp_ext):
                interpreter = 'bash'
                file_call = file.split(".")[0] + ".o"

                # Determine the input file and output directory based on the directory
                if "P1" in str(file_path):
                    input_file = MAP.get("P1")
                    output_dir = MAP_OUTPUTS.get("P1")
                elif "P2" in str(file_path):
                    input_file = MAP.get("P2")
                    output_dir = MAP_OUTPUTS.get("P2")
                elif "P3" in str(file_path):
                    input_file = MAP.get("P3")
                    output_dir = MAP_OUTPUTS.get("P3")
                else:
                    continue  # Skip files that do not match any problem directory

                # Create output directory if it does not exist
                os.makedirs(output_dir, exist_ok=True)

                # Output file path for storing captured output
                output_file = os.path.join(output_dir, "output.txt")

                # Measure the execution time
                start_time = time.time()
                try:
                    # Run the compiled C++ file with the specified input file and capture output
                    with open(output_file, 'w') as f_out:
                        subprocess.run(["bash", file_call, input_file], stdout=f_out, stderr=subprocess.PIPE, check=True)
                    status = 'Success'
                except subprocess.CalledProcessError as e:
                    status = 'Failed'
                    with open(output_file, 'w') as f_out:
                        f_out.write(f"Execution failed with error:\n{e.stderr.decode('utf-8')}")
                end_time = time.time()

                execution_time = end_time - start_time

                # Append the results
                results.append({
                    'File': file_path,
                    'Interpreter': interpreter,
                    'Status': status,
                    'Execution Time (s)': execution_time,
                    'Output File': output_file
                })

    # Convert results to a DataFrame
    df = pd.DataFrame(results)

    # Print the results in a table format
    print(df.to_string(index=False))

    # Optionally execute the clean_outputs.sh script
    if execute_clean_script:
        bash_file = Path(__file__).parent.resolve() / "clean_outputs.sh"
        try:
            subprocess.run(["bash", str(bash_file)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute clean_outputs.sh: {e}")
    else:
        print("Skipping execution of clean_outputs.sh")

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='Execute compiled C++ files and optionally clean outputs.')
    parser.add_argument('--clean', action='store_true', help='Execute clean_outputs.sh after execution (default: False)')
    args = parser.parse_args()

    # Call main function with optional clean argument
    main(args.clean)
