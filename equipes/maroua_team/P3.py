from collections import deque
from pathlib import Path


def rotate(state: list[int], first: int, last: int, direct: int, d: int):
    """
    Effectue une rotation sur une partie spécifique de l'état donné.

    Args:
        state (list[int]): Liste représentant l'état actuel.
        first (int): Indice du premier élément à inclure dans la rotation.
        last (int): Indice du dernier élément à inclure dans la rotation.
        direct (int): Direction de la rotation, 1 pour horaire, -1 pour
        anti-horaire.
        d (int): Nombre de chiffres distincts possibles.

    Returns:
        list[int]: État résultant après la rotation.
    """
    first -= 1  # Ajuste les indices pour commencer à partir de 0
    last -= 1  # Ajuste les indices pour commencer à partir de 0
    if direct == 1:  # Rotation horaire
        for i in range(first, last + 1):
            state[i] = (state[i] + 1) % d
    elif direct == -1:  # Rotation anti-horaire
        for i in range(first, last + 1):
            state[i] = (state[i] - 1) % d
    return state


def all_zeros(state):
    """
    Vérifie si l'état donné est résolu, c'est-à-dire s'il contient que des
    zéros.

    Args:
        state (list[int]): Liste représentant l'état actuel.

    Returns:
        bool: True si l'état est résolu, False sinon.
    """
    # Vérifie si tous les éléments de l'état sont égaux à zéro
    return all(x == 0 for x in state)


def min_operations(init_state, d):
    """
    Calcule le nombre minimal d'opérations nécessaires pour résoudre le
    problème.

    Utilise une approche de parcours en largeur (BFS) pour trouver la
    solution optimale.

    Args:
        init_state (list[int]): État initial.
        d (int): Nombre de chiffres distincts possibles.

    Returns:
        int: Nombre minimal d'opérations nécessaires pour résoudre le problème.
    """
    # Garde une trace de tous les nœuds visités pour
    # éviter les boucles
    visited = set()
    # (state, operations) où state représente l'état actuel et
    # operations garde le nombre d'opérations appliquées
    queue = deque([(init_state, 0)])

    while queue:
        curr_state, operations = queue.popleft()

        if all_zeros(curr_state):
            # Si l'état est résolu (tous les zéros), retourne le
            # nombre d'opérations
            return operations

        if tuple(curr_state) in visited:
            # Si l'état est déjà visité, passe à l'état suivant
            continue

        visited.add(tuple(curr_state))

        n = len(init_state)
        for first in range(1, n + 1):
            for last in range(first, n + 1):
                for direct in [1, -1]:
                    # Explore les rotations possibles et les met en file
                    # d'attente pour une exploration ultérieure
                    new_state = rotate(curr_state[:], first, last, direct, d)
                    queue.append((new_state, operations + 1))


def read_tests_from_file(file_path):
    """
    Lit les tests à partir du fichier d'entrée et renvoie une liste de tuples
    (N, D, init_state).

    Args:
        file_path (str): Chemin du fichier d'entrée.

    Returns:
        list: Liste de tuples (N, D, init_state) représentant les tests.
    """
    tests = []
    with open(file_path, "r") as file:
        num_tests = int(file.readline().strip())
        for _ in range(num_tests):
            N, D = map(int, file.readline().split())
            init_state = list(map(int, file.readline().split()))
            tests.append((N, D, init_state))
    return tests


def write_results_to_file(results, file_path):
    """
    Écrit les résultats dans le fichier de sortie.

    Args:
        results (list[int]): Liste des résultats.
        file_path (str): Chemin du fichier de sortie.
    """
    with open(file_path, "w") as file:
        for i, result in enumerate(results, 1):
            file.write(f"Test {i}: {result}\n")


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent.parent
    input_file = root / "P3/input.txt"
    output_file = root / "P3/output.txt"

    tests = read_tests_from_file(input_file)
    results = []
    for N, D, init_state in tests:
        min_ops = min_operations(init_state, D)
        results.append(min_ops)

    write_results_to_file(results, output_file)
