from pathlib import Path

def solve(input_filename, output_filename):
    with open(input_filename, 'r') as f, open(output_filename, 'w') as outfile:
        count = 0
        for line in f.readlines():
            data = [int(x) for x in line.split()]
            # test case
            ans = 0
            
            for i in range(len(data)  - 3):
                v0 , v1, v2 = data[i + 1], data[i + 2], data[i + 3]
                if v0 < v1 and v1 > v2:
                    ans+=1
            outfile.write("Test "+str(count+1)+": "+str(ans) + "\n")
            count+=1

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    input_filename = root / "input.txt"
    output_filename = root / "output1.txt"
    solve(input_filename, output_filename)