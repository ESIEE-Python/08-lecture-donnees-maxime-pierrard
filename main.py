#### Imports et définition des variables globales
"""
    Importation des bibliothèques nécessaires pour travailler avec des fichiers CSV.
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Lit et retourne le contenu du fichier <filename>.

    Args:
        filename (str): Chemin du fichier à lire.

    Returns:
        list: Une liste contenant les lignes du fichier, chaque ligne étant une liste d'entiers.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Utiliser un lecteur CSV pour parcourir le fichier ligne par ligne
        lecteur = csv.reader(file, delimiter=';')
        # Transformer chaque ligne en une liste d'entiers
        data = [[int(valeur) for valeur in ligne] for ligne in lecteur]
    return data

def get_list_k(data, k):
    """
        Retourne la liste correspondant à l'indice k.

        Args:
            data (list): Liste de listes.
            k (int): Indice de la liste à retourner.
    """
    if not 0 <= k < len(data):
        print("Indice hors des limites autorisées.")
        return None
    return data[k]

def get_first(l):
    """
        Récupère le premier élément d'une liste.

        Args:
            l (list): Liste d'éléments.

        Returns:
            Le premier élément ou None si la liste est vide.
    """
    return l[0] if l else None

def get_last(l):
    """
        Récupère le dernier élément d'une liste.

        Args:
            l (list): Liste d'éléments.

        Returns:
            Le dernier élément ou None si la liste est vide.
    """
    return l[-1] if l else None

def get_max(l):
    """
        Renvoie la valeur maximale de la liste donnée.

        Args:
            l (list): Liste d'entiers.

        Returns:
            int: La valeur maximale ou None si la liste est vide.
    """
    return max(l) if l else None

def get_min(l):
    """
        Renvoie la valeur minimale de la liste donnée.

        Args:
            l (list): Liste d'entiers.

        Returns:
            int: La valeur minimale ou None si la liste est vide.
    """
    return min(l) if l else None

def get_sum(l):
    """
        Calcule et retourne la somme des éléments d'une liste.

        Args:
            l (list): Liste d'entiers.

        Returns:
            int: La somme des éléments ou None si la liste est vide.
    """
    return sum(l) if l else None

#### Fonction principale

def main():
    """Point d'entrée principal pour tester les fonctionnalités implémentées."""
    # Définir le nom du fichier contenant les données
    nom_fichier = FILENAME

    try:
        # Lecture des données depuis le fichier spécifié
        donnees = read_data(nom_fichier)
        print("Contenu du fichier lu avec succès :")
        print(donnees)

        # Vérifier le fonctionnement de la fonction get_list_k
        indice_k = 1  # Exemple d'indice à tester
        liste_k = get_list_k(donnees, indice_k)
        print(f"Liste à l'indice {indice_k} : {liste_k}")

        # Tester les autres fonctions secondaires avec une liste d'exemple
        exemple_liste = liste_k
        print(f"Premier élément de la liste : {get_first(exemple_liste)}")
        print(f"Dernier élément de la liste : {get_last(exemple_liste)}")
        print(f"Valeur maximale : {get_max(exemple_liste)}")
        print(f"Valeur minimale : {get_min(exemple_liste)}")
        print(f"Somme des valeurs : {get_sum(exemple_liste)}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except ValueError as erreur_conversion:
        print(f"Erreur lors de la conversion en entier : {erreur_conversion}")
    except csv.Error as erreur_csv:
        print(f"Erreur de traitement du fichier CSV : {erreur_csv}")
    except IndexError:
        print("Erreur : Indice hors limites pour accéder à une liste.")

if __name__ == "__main__":
    main()
