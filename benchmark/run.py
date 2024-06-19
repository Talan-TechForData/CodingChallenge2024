import os
import subprocess
import time
import pandas as pd
from pathlib import Path
import argparse
import shutil

# Define base directory and file extensions
base_directory = Path(__file__).parent / "../equipes"
python_ext = '.py'
r_ext = '.R'

def generate_cases(problem, cases):
    case_generator_script = Path(__file__).parent / f"../solutions/{problem}/case_generator.py"
    try:
        subprocess.run(["python", str(case_generator_script), str(cases)], check=True)
        print(f"Generated {cases} cases for problem {problem}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate cases for problem {problem}: {e}")

def copy_input_files():
    # Iterate over each problem directory in solutions/data
    solutions_dir = Path(__file__).parent / "../solutions"
    for problem_dir in solutions_dir.iterdir():
        problem_name = problem_dir.name
        if problem_name.startswith("P"):
            cases = 250  # Adjust the number of cases as needed
            generate_cases(problem_name, cases)
            for team_dir in base_directory.glob(f"*/data/{problem_name}"):
                if team_dir.is_dir():
                    input_file_path = problem_dir / "input.txt"
                    if input_file_path.exists():
                        destination_file = team_dir / "input.txt"
                        shutil.copy(input_file_path, destination_file)
                        print(f"Copied input.txt for problem {problem_name} to {destination_file}")
                    else:
                        print(f"Warning: input.txt not found for problem {problem_name}")

def main(execute_clean_script):
    results = []

    # Copy input.txt files to team directories
    copy_input_files()

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
                print(f"Execution of {file_path} successful.")
            except subprocess.CalledProcessError:
                status = 'Failed'
                print(f"Execution of {file_path} failed.")
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
