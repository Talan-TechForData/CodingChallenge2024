import os
from rich import print
from rich.table import Table

solutions_dir = 'solutions/data'
teams_dir = 'equipes'

def compare_output_with_solution(team_name, problem):
    solution_file = os.path.join(solutions_dir, problem, 'output.txt')
    team_file = os.path.join(teams_dir, team_name, 'data', problem, 'output.txt')

    if not os.path.exists(solution_file):
        print(f"[red]Solution file {solution_file} does not exist.[/red]")
        return -1

    if not os.path.exists(team_file):
        print(f"[red]Team file {team_file} does not exist.[/red]")
        return -1

    # Read contents of the files
    with open(solution_file, 'r') as sol_file, open(team_file, 'r') as team_file:
        solution_lines = sol_file.readlines()
        team_lines = team_file.readlines()

    # Compare line by line
    diff_count = 0
    for line_num, (sol_line, team_line) in enumerate(zip(solution_lines, team_lines), start=1):
        if sol_line != team_line:
            print(f"[yellow]Difference found in {team_name} for problem {problem} at line {line_num}[/yellow]:")
            print(f"[yellow]Expected:[/yellow] {sol_line.strip()}")
            print(f"[yellow]Got     :[/yellow] {team_line.strip()}")
            diff_count += 1

    return diff_count

def main():
    problems = ['P1', 'P2', 'P3']
    teams = ['amila_team', 'maroua_team', 'mehdi_team']

    total_diff_count = 0
    summary_table = Table(title="Comparison Summary")

    summary_table.add_column("Team")
    for problem in problems:
        summary_table.add_column(problem, justify="center")

    for team in teams:
        team_diff_count = 0
        row = [team]
        for problem in problems:
            diff_count = compare_output_with_solution(team, problem)
            team_diff_count += diff_count
            row.append(str(diff_count))
        summary_table.add_row(*row)
        total_diff_count += team_diff_count

    print(summary_table)
    print(f"\nTotal differences across all teams: {total_diff_count}")

if __name__ == "__main__":
    main()
