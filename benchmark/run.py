import os
import subprocess
import time
import pandas as pd
from pathlib import Path
import argparse
import threading

# Define base directory and file extensions
base_directory = Path(__file__).parent / "../equipes"
python_ext = '.py'
r_ext = '.R'

def run_with_timeout(command, timeout):
    """Run a command with a timeout."""
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    timer = threading.Timer(timeout, proc.kill)
    try:
        timer.start()
        stdout, stderr = proc.communicate()
    finally:
        timer.cancel()
    return stdout, stderr

def main():
    results = []

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
                stdout, stderr = run_with_timeout([interpreter, file_path], timeout=60)
                status = 'Success'
                print(f"Execution of {file_path} successful.")
            except subprocess.TimeoutExpired:
                status = '>30s'
                print(f"Execution of {file_path} exceeded 30 seconds.")
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

if __name__ == "__main__":
    main()
