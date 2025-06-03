"""
Ecrire un programme en Python qui compte le nombre de
chiffres dans un nombre saisi par l’utilisateur.
"""

nombre = input("Entrez un nombre (entier ou décimal) : ")

# Supprimer le signe negatif et le séparateur decimal
nombre_sans_signes = nombre.replace("-", "").replace(".", "").replace(",", "")

nb_chiffres = len(nombre_sans_signes)
print(f"Le nombre contient {nb_chiffres} chiffre(s).")