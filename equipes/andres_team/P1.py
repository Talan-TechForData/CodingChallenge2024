from pathlib import Path

p = Path(__file__) / "../../../P1/input.txt"
p = p.resolve()
print(p)

with open(p,"r") as f:
    text = f.readlines()

print(text)