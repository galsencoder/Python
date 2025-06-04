"""
Écrire un programme Python qui exécute une opération sur une
liste et gère une exception IndexError si l’index est en dehors de la plage.
"""


def acceder_element_liste(liste, index):
    try:
        return liste[index]
    except IndexError:
        return "Erreur : Index en dehors de la plage de la liste."
    

# Exemple d'utilisation
if __name__ == "__main__":
    ma_liste = [10, 20, 30, 40, 50]
    index = int(input("Entrez l'index de l'élément à accéder : "))
    print(acceder_element_liste(ma_liste, index))