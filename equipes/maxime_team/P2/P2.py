import time

def lire_fichier_entree(fichier_entree):
    with open(fichier_entree, 'r') as fichier:
        lignes = fichier.readlines()
    
    lignes= lignes[1:]
    donnees = []
    i = 0
    while i < len(lignes):
        N, B = map(int, lignes[i].split())
        prix_maisons = list(map(int, lignes[i+1].split()))
        donnees.append((N, B, prix_maisons))
        i += 2
    
    return donnees

def maisons_max(N, B, prix_maisons):
    prix_maisons.sort()
    cout_total = 0
    nombre_maisons = 0
    for prix in prix_maisons:
        if cout_total + prix <= B:
            cout_total += prix
            nombre_maisons += 1
        else:
            break
    return nombre_maisons

def ecrire_fichier_sortie(fichier_sortie, resultats):
    with open(fichier_sortie, 'w') as fichier:
        for i, resultat in enumerate(resultats):
            fichier.write(f"Test {i+1} : {resultat[0]} temps {resultat[1]:.6f} sec\n")

def main():

    fichier_entree = '../../../P2/input.txt'
    fichier_sortie = 'ResultatsP2/output.txt'
    donnees = lire_fichier_entree(fichier_entree)
    resultats = []
    for N, B, prix_maisons in donnees:
        debut = time.time()
        resultat = maisons_max(N, B, prix_maisons)
        fin = time.time()
        temps = fin - debut
        resultats.append((resultat, temps))
    ecrire_fichier_sortie(fichier_sortie, resultats)

# Exécuter la fonction principale
if __name__ == "__main__":
    main()