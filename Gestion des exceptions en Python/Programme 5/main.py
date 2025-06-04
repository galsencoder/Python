"""
Écrire un programme Python qui ouvre un fichier et gère une exception PermissionError en cas de problème de permission.
"""

def ouvrir_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        return "Erreur : Fichier non trouvé."
    except PermissionError:
        return "Erreur : Permission refusée."

if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier à ouvrir : ")
    print(ouvrir_fichier(nom_fichier))