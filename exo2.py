nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []

for i in range(nombreEtudiants):
    while True:
        try:
            note = float(input(f"Note étudiant {i + 1}: "))
            if 0 <= note <= 20:
                notes.append(note)
                moyenne += note
                break
            else:
                continue
        except ValueError:
            continue

moyenne /= nombreEtudiants
print(f"\n\t- La moyenne est de {round(moyenne, 3)}!")

print("Numéro de l'étudiant, note, différence avec la moyenne")
for i in range(len(notes)):
    print(f"Étudiant {i + 1}, {notes[i]}, {round(notes[i] - moyenne, 2)}")
