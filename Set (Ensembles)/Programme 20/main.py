"""
Écris une fonction filtrer(liste, interdits) qui retourne une nouvelle liste sans les mots interdits.
"""

def filtrer(liste, interdits):
    return [mot for mot in liste if mot not in interdits]



liste_exemple = ["chat", "chien", "oiseau", "poisson", "chat"]
interdits_exemple = ["chat", "poisson"]
liste_filtrée = filtrer(liste_exemple, interdits_exemple)
print(liste_filtrée) 