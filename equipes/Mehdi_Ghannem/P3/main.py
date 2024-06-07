from collections import deque
from pathlib import Path

def neighbors(node, n, d, max_a, min_b):
    for a in range(max_a):
        for b in range(min_b, n):
            if ( a > b):
                continue
            up = [c for c in node]
            down = [c for c in node]
            for i in range(a, b + 1):
                up[i] = str((int(node[i]) + 1) % d)
                down[i] = str((int(node[i]) - 1) % d)

            yield (''.join(up), a, b)
            if (d > 2):
                yield (''.join(down), a, b)


def solve(input_filename, output_filename):
    with open(input_filename, 'r') as f, open(output_filename, 'w') as outfile:
        t = int(f.readline())
        count = 0
        for _ in range(t):

            n, d = f.readline().split()
            n, d = int(n), int(d)
            initial = ''.join(f.readline().split())

            queue = deque([(initial, 0, n, 0)])
            visited = set()
            target = '0' * n

            while queue: 
                node, depth, max_a, min_b = queue.popleft()
                if node == target:
                    outfile.write("Test "+str(count+1)+": "+str(depth) + "\n")
                    count+= 1
                    break
                if node in visited:
                    continue
                visited.add(node)
                for neighbor, a, b in neighbors(node, n, d, max_a, min_b):
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1, a, b))
                    
                
if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    input_filename = root / "input.txt"
    output_filename = root / "output3.txt"
    solve(input_filename, output_filename)