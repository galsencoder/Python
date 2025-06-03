"""
Écrire un programme Python pour calculer la distance entre deux points.
"""

import math 

x1 = int(input("Entrez laa valeur de x1 : "))
y1 = int(input("Entrez la valeur de y1 : "))

x2 = int(input("Entrez la valeur de x2 : "))
y2 = int(input("Entrez la valeur de y2 : "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
print(f"La distance entre ces points est : {distance:.2f}")