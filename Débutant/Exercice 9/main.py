"""
Écrire un programme Python qui prend un nombre entière et calcule sa valeur absolue.
"""

nombre = float(input("Entrez un nombe : "))

if nombre < 0 :
    print(f"la valeur absolue de {nombre} est {-nombre}")
else :
    print(f"la valeur absolue de {nombre} est {nombre}")
