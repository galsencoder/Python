"""
Écrire un programme Python pour trouver les nombres maximum et minimum à partir des nombres décimaux spécifiés.
"""

def trouver_max_min(nombres):
    maximum = max(nombres)
    minimum = min(nombres)
    return maximum, minimum

# Exemple d'utilisation
if __name__ == "__main__":
    nombres = [1.5, 2.3, 3.7, 0.8, 4.1]
    max_val, min_val = trouver_max_min(nombres)
    print(f"Maximum: {max_val}, Minimum: {min_val}")