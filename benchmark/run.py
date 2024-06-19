import os
import subprocess
import time
import pandas as pd
from pathlib import Path

base_directory = Path(__file__).parent / "../equipes"
python_ext = '.py'
r_ext = '.R'

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

df = pd.DataFrame(results)
print(df.to_string(index=False))
bash_file = Path(__file__).parent.resolve() / "clean_outputs.sh"
subprocess.run(["bash", str(bash_file)], check=True)