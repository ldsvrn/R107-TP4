L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

counter = 0
num = 0

for i in L1:
    j = L1.count(i)
    if j > counter:
        counter = j
        num = i

print(f"Le nombre le plus frequent dans la liste est le: {num} ({counter}x)")