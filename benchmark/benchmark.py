import os

solutions_dir = 'solutions/data'
teams_dir = 'equipes'

def compare_output_with_solution(team_name, problem):
    solution_file = os.path.join(solutions_dir, problem, 'output.txt')
    team_file = os.path.join(teams_dir, team_name, 'data', problem, 'output.txt')

    if not os.path.exists(solution_file):
        print(f"Solution file {solution_file} does not exist.")
        return -1

    if not os.path.exists(team_file):
        print(f"Team file {team_file} does not exist.")
        return -1

    # Read contents of the files
    with open(solution_file, 'r') as sol_file, open(team_file, 'r') as team_file:
        solution_lines = sol_file.readlines()
        team_lines = team_file.readlines()

    # Compare line by line
    diff_count = 0
    for line_num, (sol_line, team_line) in enumerate(zip(solution_lines, team_lines), start=1):
        if sol_line != team_line:
            print(f"Difference found in {team_name} for problem {problem} at line {line_num}:")
            print(f"Expected: {sol_line.strip()}")
            print(f"Got     : {team_line.strip()}")
            diff_count += 1

    return diff_count

def main():
    problems = ['P1', 'P2', 'P3']
    teams = ['amila_team', 'maroua_team', 'mehdi_team']

    total_diff_count = 0

    for team in teams:
        print(f"Checking team: {team}")
        team_diff_count = 0
        for problem in problems:
            diff_count = compare_output_with_solution(team, problem)
            team_diff_count += diff_count
        print(f"Total differences for {team}: {team_diff_count}\n")
        total_diff_count += team_diff_count

    print(f"Total differences across all teams: {total_diff_count}")

if __name__ == "__main__":
    main()
