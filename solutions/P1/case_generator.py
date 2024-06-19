import random
import argparse
import pathlib

def generate_line(n):
    """Generates a random case of n peaks"""
    final_list = []
    for i in range(n):
        random_zeros = [0] * (random.randint(1, max(1, n // 3)) + 1)
        peak_i = random.randint(n, 2 * n)
        final_list.extend(random_zeros)
        final_list.append(peak_i)
        final_list.extend(random_zeros)
    lenght = len(final_list)
    final_list.insert(0, lenght)
    final_list = list(map(str, final_list))
    list_str = " ".join(final_list) + "\n"
    return list_str


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Creates a File with peaks")

    parser.add_argument("cases", type=int)

    args = parser.parse_args()

    path = pathlib.Path(__file__).parent.resolve()

    with open("input.txt", "w") as fin, open("output.txt", "wb") as fout:
        for i in range(args.cases):
            pk = random.randint(0, args.cases)
            fout.write(f"Case #{i}: {pk}\n".encode("utf-8"))
            test_case = generate_line(pk)
            fin.write(test_case)
