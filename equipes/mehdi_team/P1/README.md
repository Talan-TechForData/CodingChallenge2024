# Le problème des pics

## Contexte

Monica participe à une course de vélo avec $N$ checkpoints​

Un *checkpoint* est un *pic* si et seulement si:​

1. Son niveau d'altitude est plus élevé que l'altitude du pic précédant ainsi que le pic suivant​

2. Si ce n'est pas le premier ou le dernier pic​ dans la séquence de pics

L'objectif de ce problème est de trouver le nombre de pics.

## Séquence d'entrée/sortie

Vous allez tester votre programme avec un fichier texte contenant $T$ tests différents chaque test contient la quantité $N$ de checkpoints et le niveau d'altitude de chacun.​

- **Exemple fichier en entrée**

    ```
    3   ​
    4 20 90 50 40 ​
    2 3 100​
    5 60 80 10 20 4
    ```

- **Exemple fichier en sortie**

    ```
    Test 1: 1
    Test 2: 0
    Test 3: 2
    ```
