"""
Écris une fonction mots_uniques(texte) qui retourne un ensemble des mots distincts.
Bonus : retourne aussi le nombre de mots différents.
"""

def mots_uniques(texte):
    # Séparer le texte en mots
    mots = texte.split()
    
    # Utiliser un ensemble pour stocker les mots uniques
    mots_distincts = set(mots)
    
    # Retourner l'ensemble des mots distincts et le nombre de mots différents
    return mots_distincts, len(mots_distincts)




texte = "le chat et le chien jouent dans le jardin le chat est heureux"
mots_distincts, nombre_mots = mots_uniques(texte)

print("Mots distincts : ", mots_distincts)
print("Nombre de mots différents : ", nombre_mots)


