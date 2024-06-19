import os
from rich import print
from rich.table import Table
from rich.console import Console
from rich.color import Color

solutions_dir = 'solutions/data'
teams_dir = 'equipes'

# Initialize a rich Console
console = Console()

def compare_output_with_solution(team_name, problem):
    solution_file = os.path.join(solutions_dir, problem, 'output.txt')
    team_file = os.path.join(teams_dir, team_name, 'data', problem, 'output.txt')

    if not os.path.exists(solution_file):
        console.print(f"[red]Solution file {solution_file} does not exist.[/red]")
        return -1

    if not os.path.exists(team_file):
        console.print(f"[red]Team file {team_file} does not exist.[/red]")
        return -1

    # Read contents of the files
    with open(solution_file, 'r') as sol_file, open(team_file, 'r') as team_file:
        solution_lines = sol_file.readlines()
        team_lines = team_file.readlines()

    # Compare line by line
    diff_count = 0
    for line_num, (sol_line, team_line) in enumerate(zip(solution_lines, team_lines), start=1):
        if sol_line != team_line:
            diff_count += 1
            console.print(f"[yellow]Difference found in {team_name} for problem {problem} at line {line_num}[/yellow]:")
            console.print(f"[yellow]Expected:[/yellow] {sol_line.strip()}")
            console.print(f"[yellow]Got     :[/yellow] {team_line.strip()}")

    return diff_count

def main():
    problems = ['P1', 'P2', 'P3']
    teams = ['amila_team', 'maroua_team', 'mehdi_team']

    # Define initial values V based on the number of cases
    V = {
        'P1': 50,
        'P2': 50,
        'P3': 5
    }

    total_score = 0
    summary_table = Table(title="Comparison Summary")

    summary_table.add_column("Team")
    for problem in problems:
        summary_table.add_column(problem, justify="center")
    summary_table.add_column("Total", justify="center")  # Add Total column

    for team in teams:
        team_score = 0
        row = [team]
        for problem in problems:
            diff_count = compare_output_with_solution(team, problem)
            if diff_count == -1:
                score = -V[problem]  # Execution failure case
            else:
                score = V[problem] - diff_count
            team_score += score
            row.append(f"{score:+d}")  # Format score as signed integer

        row.append(f"{team_score:+d}")  # Append team's total score to the row
        summary_table.add_row(*row)
        total_score += team_score

    console.print(summary_table)
    console.print(f"\nTotal score across all teams: {total_score}")

if __name__ == "__main__":
    main()
