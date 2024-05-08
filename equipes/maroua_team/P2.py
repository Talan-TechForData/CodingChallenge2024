from pathlib import Path


def max_houses(N: int, B: int, prices: list[int]):
    """
    Calcule le nombre maximal de maisons que l'on peut acheter avec un budget
    donné.

    Trie les prix par ordre croissant, puis achète autant de maisons que
    possible en commençant par les moins chères jusqu'à ce que le budget
    soit dépassé.

    Args:
        N (int): Nombre de maisons disponibles.
        B (int): Budget total disponible.
        prices (list[int]): Liste des prix des maisons.

    Returns:
        int: Nombre maximal de maisons que l'on peut acheter avec le budget
        donné.
    """
    prices.sort()  # Triez les prix par ordre croissant
    houses_to_buy = 0
    total_price = 0

    for price in prices:
        if total_price + price <= B:
            houses_to_buy += 1
            total_price += price
        else:
            break

    return houses_to_buy


def main():
    """
    Fonction principale pour exécuter le programme.

    Lecture des données d'entrée à partir du fichier input.txt,
    exécution de la fonction max_houses pour chaque jeu de données,
    puis enregistrement des résultats dans le fichier output.txt.
    """
    with open(
        Path(__file__).resolve().parent.parent.parent / "P2/input.txt", "r"
    ) as file:
        tests = file.readlines()
    root = Path(__file__).resolve().parent.parent.parent
    output_file = root / "P2/output.txt"
    with open(output_file, "w") as output:
        for i in range(1, len(tests), 2):  # Parcourez les tests par pas de 2
            N, B = map(int, tests[i].strip().split())
            prices = list(map(int, tests[i + 1].strip().split()))
            result = max_houses(N, B, prices)
            output.write(f"Test {i//2 + 1}: {result}\n")

    print("Résultats enregistrés dans le fichier output.txt.")


if __name__ == "__main__":
    main()
