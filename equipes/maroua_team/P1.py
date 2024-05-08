import time
from pathlib import Path


def count_peaks(altitudes: list[int]):
    """
    Compte le nombre de pics dans une liste d'altitudes.

    Args:
        altitudes (list[int]): Liste des altitudes.

    Returns:
        int: Nombre de pics dans la liste d'altitudes.
    """
    peaks = 0
    n = len(altitudes)

    if n <= 2:
        return peaks

    for i in range(1, n - 1):
        if altitudes[i] > altitudes[i - 1] and altitudes[i] > altitudes[i + 1]:
            peaks += 1

    return peaks


def main():
    """
    Fonction principale pour exécuter le programme.

    Lecture des données d'entrée à partir du fichier input.txt,
    exécution du comptage des pics pour chaque jeu de données,
    puis enregistrement des résultats dans le fichier output.txt.
    """
    root = Path(__file__).resolve().parent.parent.parent
    with open(root / "P1/input.txt", "r") as file:
        tests = file.readlines()

    output_file = root / "P1/output.txt"
    with open(output_file, "w") as output:
        for i, test in enumerate(tests):
            test_data = list(map(int, test.strip().split()[1:]))

            start_time = time.time()  # Mesurer le temps d'exécution

            peaks = count_peaks(test_data)

            end_time = time.time()
            execution_time = end_time - start_time

            output.write(f"Test {i+1}: {peaks} (Time: {execution_time:.6f})\n")

    print("Résultats enregistrés dans le fichier output.txt.")


if __name__ == "__main__":
    main()
