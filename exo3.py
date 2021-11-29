while True:
    try:
        vectorSize = int(input("Entrez la taille de vos vecteurs [Entre 1 et 10]: "))
        if 1 <= vectorSize <= 10: break
    except ValueError:
        continue

vector = []

for numvector in range(2):
    vector.append([])
    for values in range(vectorSize):
        vector[numvector].append(int(input(f"Entrez v{numvector + 1}[{values}]: ")))
    print("")

scalaire = 0
for i in range(vectorSize):
    scalaire += vector[0][i] * vector[1][i]

print(f"\t- Le produit scalaire est égal à {scalaire}")
