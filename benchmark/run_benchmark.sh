poetry run python $(pwd)/benchmark/run_sol.py
poetry run python $(pwd)/benchmark/run.py
poetry run python $(pwd)/benchmark/benchmark.py
sleep 10
poetry run python $(pwd)/benchmark/generate_copy.py --generate --cases 5 5 5
poetry run python $(pwd)/benchmark/run_sol.py
poetry run python $(pwd)/benchmark/run.py 
poetry run python $(pwd)/benchmark/benchmark.py
sleep 10
