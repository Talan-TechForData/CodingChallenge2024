from pathlib import Path
import argparse

p = Path(__file__) / "../../../P1/input.txt"
p = p.resolve()
print(p)

with open(p,"r") as f:
    for line in f.readlines():
        print(line)
        break