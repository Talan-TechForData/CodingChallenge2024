import time

def lire_fichier(chemin_fichier):
    """
    Lis le fichier en entrée et retourne une liste avec chaque séquence de chiffre
    à tester
    """
    sequences = []
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            sequence = [int(chiffre) for chiffre in ligne.strip().split()]
            sequences.append(sequence)
    return sequences

def compter_pics(sequence):
    """
    Retourne le nombre de pics dans une séquence
    """
    nombre_pics = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1]:
            nombre_pics += 1
    return nombre_pics

def ecrire_resultats(chemin_fichier_sortie, resultats):
    """
    Écrit les résultats dans un fichier de sortie.
    """
    with open(chemin_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        for resultat in resultats:
            fichier_sortie.write(resultat + '\n')

def main():
    """
    Fonction principal qui lis le fichier en entrée, compte le nombre de pic
    et écrit les résultats dans un fichier output.txt
    """
    import pathlib
    p = pathlib.Path(__file__).parent.resolve()
    chemin_fichier = p / '../data/P1/input.txt'
    chemin_fichier_sortie = p / '../data/P1/output.txt'

    sequences = lire_fichier(chemin_fichier)
    resultats = []

    for i, sequence in enumerate(sequences):
        debut = time.time()
        nombre_pics = compter_pics(sequence)
        fin = time.time()
        temps_calcul = fin - debut

        resultat = f"Test {i+1} : Nombre pic = {nombre_pics} (Temps: {temps_calcul:.6f} sec)"
        resultats.append(resultat)

    ecrire_resultats(chemin_fichier_sortie, resultats)

# Exécuter la fonction principale
if __name__ == "__main__":
    main()





