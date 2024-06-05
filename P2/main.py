from pathlib import Path
def solve(input_filename, output_filename):
    with open(input_filename, 'r') as f, open(output_filename, 'w') as outfile:
        count = 0
        t = int(f.readline())
        for i in range(t):
            n, b = f.readline().split()
            n, b = int(n), int(b) 
            a = sorted([int(x) for x in f.readline().split()])
            money_spent=0
            ans = 0
            
            for i in range(n):
                if money_spent + a[i] > b:
                    break
                else :
                    money_spent += a[i]
                    ans += 1
            outfile.write("Test "+str(count+1)+": "+str(ans) + "\n")
            count+=1
                
if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    input_filename = root / "input.txt"
    output_filename = root / "output2.txt"
    solve(input_filename, output_filename)