import random
import argparse
import pathlib

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Creates a File with Locks")

    parser.add_argument("cases", type=int)

    args = parser.parse_args()

    path = pathlib.Path(__file__).parent.resolve()

    with open(path / "input.txt", "w") as fin:
        fin.write(f"{args.cases}\n")
        for i in range(args.cases):
            D = random.randint(0, 9)
            N = random.randint(3, 9)
            l_i = []
            for i in range(N):
                l_i.append(random.randint(0, D))
            l_i = list(map(str, l_i))
            list_str = " ".join(l_i) + "\n"
            fin.write(f"{N} {D}\n")
            fin.write(list_str)
