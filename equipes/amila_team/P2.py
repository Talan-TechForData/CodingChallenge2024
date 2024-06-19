import itertools
def main():
    import pathlib
    path = pathlib.Path(__file__).parent
    with open(path / "data/P2/input.txt", "r") as file:
        lines = [line.strip() for line in file]
        convert_line = [list(map(int, string.split())) for string in lines]

    # Start list after the number of test
    start_list = convert_line[1:]

    number_of_test = 0
    with open('output_p2_AM.txt', 'w') as f:
        for i in range(0, len(start_list),2):
            #Number of house
            N = start_list[i][0]
            #Budget
            B = start_list[i][1]
            #Number max of house
            max_house = 0
            number_of_test += 1
            for r in range(1, len(start_list[i+1]) + 1):
                # try combinations to find the max number of house
                for comb in itertools.combinations(start_list[i+1], r):
                    if sum(comb) <= B:
                        max_house = max(max_house, len(comb))
            f.write(f'Test {number_of_test} : {max_house}\n')
    print('Résultats exportés dans output_p2_AM.txt')


if __name__ == "__main__":
    main()
