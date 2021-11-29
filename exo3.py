while True:
    try:
        vecteurSize = int(input("Entrez la taille de vos vecteurs [Entre 1 et 10]: "))
        if 1 <= vecteurSize <= 10: break
    except ValueError:
        continue

vecteur = []

for numvecteur in range(2):
    vecteur.append([])
    for values in range(vecteurSize):
        vecteur[numvecteur].append(float(input(f"Entrez v{numvecteur + 1}[{values}]: ")))
    print("")

print(vecteur)
scalaire = 0
for v1, v2 in zip(vecteur[0], vecteur[1]):  # ???
    scalaire += v1 * v2

print(f"\t- Le produit scalaire est égal à {scalaire}")
