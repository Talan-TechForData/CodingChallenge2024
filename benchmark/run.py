import os
import subprocess
import time
import pandas as pd
from pathlib import Path
import argparse

# Define base directory and file extensions
base_directory = Path(__file__).parent / "../equipes"
python_ext = '.py'
r_ext = '.R'

def main(execute_clean_script):
    results = []

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(python_ext):
                interpreter = 'python'
            elif file.endswith(r_ext):
                interpreter = 'Rscript'
            else:
                continue  # Skip files that are not Python or R scripts

            # Measure the execution time
            start_time = time.time()
            try:
                subprocess.run([interpreter, file_path], check=True)
                status = 'Success'
            except subprocess.CalledProcessError:
                status = 'Failed'
            end_time = time.time()

            execution_time = end_time - start_time

            # Append the results
            results.append({
                'File': file_path,
                'Interpreter': interpreter,
                'Status': status,
                'Execution Time (s)': execution_time
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
    parser = argparse.ArgumentParser(description='Execute Python and R scripts and optionally clean outputs.')
    parser.add_argument('--clean', action='store_true', help='Execute clean_outputs.sh after execution (default: False)')
    args = parser.parse_args()

    # Call main function with optional clean argument
    main(args.clean)
