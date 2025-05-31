"""
Écrire un programme en Python qui calcule les nombres de Fibonacci jusqu'à 50.
"""

a, b = 0, 1

print("Nombres de Fibonacci jusqu'à 50 : ")

while a <= 50:
    print(a)
    a, b = b, a + b