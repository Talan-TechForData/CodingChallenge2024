import subprocess
import os
from rich.table import Table
from rich.console import Console

def run_flake8(directory):
    result = subprocess.run(['flake8', directory], capture_output=True, text=True)
    return result.stdout

def parse_flake8_output(output):
    non_conformities = {}
    for line in output.splitlines():
        parts = line.split(":")
        if len(parts) >= 2:
            file_path = parts[0].strip()
            non_conformities[file_path] = non_conformities.get(file_path, 0) + 1
    return non_conformities

def main():
    base_dir = "equipes"
    console = Console()

    # Initialize a table with rich
    table = Table(title="PEP 8 Non-conformities Summary")
    table.add_column("Team", style="bold")
    table.add_column("File", style="bold")
    table.add_column("Non-conformities", justify="right", style="bold red")

    # Iterate over all subdirectories in the base directory
    for root, dirs, files in os.walk(base_dir):
        for dirname in dirs:
            if dirname.endswith("_team"):
                team_dir = os.path.join(root, dirname)
                output = run_flake8(team_dir)
                non_conformities = parse_flake8_output(output)

                team_total = 0
                for file_path, count in non_conformities.items():
                    table.add_row(dirname, file_path, str(count))
                    team_total += count

                # Add a subtotal row for the team with yellow highlight
                table.add_row(f"[bold blue]{dirname}[/bold blue]", "[bold blue]Total[/bold blue]", f"[bold blue]{team_total}[/bold blue]")

    console.print(table)

if __name__ == "__main__":
    main()
