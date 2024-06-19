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
    "P1": base_directory / "data/P1/input.txt",
    "P2": base_directory / "data/P2/input.txt",
    "P3": base_directory / "data/P3/input.txt"
}

MAP_OUTPUTS = {
    "P1": "solutions/data/P1/",
    "P2": "solutions/data/P2/",
    "P3": "solutions/data/P3/"
}

def compile_cpp_file(file_path):
    try:
        compile_command = ["g++", str(file_path), "-o", str(file_path.with_suffix('.o'))]
        print(f"Compiling with command: {' '.join(compile_command)}")
        result = subprocess.run(compile_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        print(result.stderr.decode('utf-8'))
        print(f"Successfully compiled {file_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile {file_path}: {e}")
        return False


def main(execute_clean_script):
    results = []

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix == cpp_ext:
                interpreter = 'bash'
                # Check if the corresponding .o file exists or compile it
                if not (file_path.with_suffix('.o')).exists():
                    if not compile_cpp_file(file_path):
                        continue  # Skip to the next file if compilation fails

                file_call = file_path.with_suffix('.o')

                # Determine the input file and output directory based on the directory
                input_file = None
                input_file_dir = None
                for problem, path in MAP.items():
                    if problem in str(file_path):
                        input_file = path
                        input_file_dir = Path(path).parent
                        output_dir = MAP_OUTPUTS[problem]
                        break
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
                        subprocess.run([str(file_call), input_file], stdout=f_out, stderr=subprocess.PIPE, check=True)
                    status = 'Success'
                except subprocess.CalledProcessError as e:
                    status = 'Failed'
                    with open(output_file, 'w') as f_out:
                        call_str = " ".join([str(file_call), str(input_file)])
                        f_out.write(f"Executed call: {call_str}\n")
                        f_out.write(f"Execution failed with error:\n{e.stderr.decode('utf-8')}")
                end_time = time.time()

                execution_time = end_time - start_time

                # Append the results
                results.append({
                    'File': str(file_path),
                    'Interpreter': interpreter,
                    'Status': status,
                    'Execution Time (s)': execution_time,
                    'Output File': output_file,
                    'Input File Directory': str(input_file_dir)  # Add input file directory to results
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
