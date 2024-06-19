def main():
    import pathlib
    path = pathlib.Path(__file__).parent
    # Open file and convert each line to list
    with open(path / "data/P1/input.txt", "r") as file:
        lines = [line.strip() for line in file]
        convert_line = [list(map(int, string.split())) for string in lines]

    number_of_test = 0
    with open(path / 'data/P1/output.txt','w') as f:
        for sublist in convert_line:
            count_peak = 0
            for i in range(len(sublist) - 2):
                if (sublist[i + 1] > sublist[i]) and (sublist[i + 1] > sublist[i + 2]):
                    count_peak += 1
            number_of_test += 1
            f.write(f'Test {number_of_test} : {count_peak}\n')
    print('Résultats exportés dans output_p1_AM.txt')

if __name__ == "__main__":
    main()