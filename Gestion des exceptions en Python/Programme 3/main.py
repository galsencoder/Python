"""
Écrivez un programme Python qui ouvre un fichier et gère 
une exception FileNotFoundError si le fichier n’existe pas.
"""

def ouvrir_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        return "Erreur : Fichier non trouvé."

if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier à ouvrir : ")
    print(ouvrir_fichier(nom_fichier))