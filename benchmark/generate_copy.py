import os
import subprocess
import shutil
from pathlib import Path
import argparse

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
    solutions_dir = Path(__file__).parent / "../solutions"
    total_lines_copied = 0  # Track total lines copied across all files

    for problem_dir in solutions_dir.iterdir():
        problem_name = problem_dir.name
        if problem_name.startswith("P"):
            # Copy to team_dir under each team's data/{problem_name} directory
            for team_dir in base_directory.glob(f"*/data/{problem_name}"):
                if team_dir.is_dir():
                    input_file_path = problem_dir / "input.txt"
                    if input_file_path.exists():
                        destination_file = team_dir / "input.txt"
                        shutil.copy(input_file_path, destination_file)

                        # Count lines in source file
                        with open(input_file_path, 'r') as src_file:
                            num_lines = len(src_file.readlines())

                        # Log the copy operation
                        print(f"Copied {num_lines} lines from {input_file_path} to {destination_file}")
                        print(f"Source: {input_file_path}")

                        total_lines_copied += num_lines
                    else:
                        print(f"Warning: input.txt not found for problem {problem_name}")

            # Additionally copy to solutions/data/{problem_name} directory
            data_dir = solutions_dir / "data" / problem_name
            data_dir.mkdir(parents=True, exist_ok=True)  # Ensure data directory exists
            if input_file_path.exists():
                destination_file = data_dir / "input.txt"
                shutil.copy(input_file_path, destination_file)

                # Count lines in source file
                with open(input_file_path, 'r') as src_file:
                    num_lines = len(src_file.readlines())

                # Log the copy operation
                print(f"Copied {num_lines} lines from {input_file_path} to {destination_file}")
                print(f"Source: {input_file_path}")

                total_lines_copied += num_lines
            else:
                print(f"Warning: input.txt not found for problem {problem_name}")

    print(f"Total lines copied: {total_lines_copied}")

def main(generate_cases_flag, num_cases, execute_clean_script):
    if generate_cases_flag:
        for problem, cases in num_cases.items():
            generate_cases(problem, cases)
        copy_input_files()

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
    parser = argparse.ArgumentParser(description='Generate cases and copy input files.')
    parser.add_argument('--generate', action='store_true', default=True, help='Generate input.txt files (default: True)')
    parser.add_argument('--cases', type=int, nargs=3, metavar=('P1', 'P2', 'P3'), default=[50, 50, 5], help='Number of cases to generate for P1, P2, and P3 (default: 50 50 5)')
    args = parser.parse_args()

    num_cases = {'P1': args.cases[0], 'P2': args.cases[1], 'P3': args.cases[2]}

    main(args.generate, num_cases, False)  # False for execute_clean_script
