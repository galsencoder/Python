"""
Écrire un programme Python pour trouver le nombre max à partir de trois nombres.
"""

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxieme nombre : "))
c = float(input("Entrez le troisieme nombre : "))


maximun = max(a,b,c)
print(f"Le maximun est {maximun}")

# Autre methode
"""
maximun = a
if b >= maximun :
    maximun = b
if c >= maximun :
    maximun = c

print(f"Le maximun est {maximun}")

"""