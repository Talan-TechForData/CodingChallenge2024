import random
import argparse
import pathlib

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Creates a File with Locks")

    parser.add_argument("cases", type=int)

    args = parser.parse_args()

    path = pathlib.Path(__file__).parent.resolve()


    with open(path / "input.txt", "w") as fin, open(path / "output.txt", "w") as fout:
        fin.write(f"{args.cases}\n")
        for i in range(args.cases):
            N = random.randint(1, 30)
            B = random.randint(10, 30)
            fin.write(f"{N} {B}\n")

            a_i = []
            for i in range(N):
                a_i.append(random.randint(1, N))

            a_ic = a_i.copy()
            aist = list(map(str, a_ic))
            list_str = " ".join(aist) + "\n"
            fin.write(list_str)

            a_i.sort()
            tmp = 0
            for i, a in enumerate(a_i):
                if tmp + a > B:
                    Bs = i + 1
                    break
                tmp += a
            fout.write(f"Case #{i}: {Bs}\n")
