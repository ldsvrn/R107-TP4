L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

counter = 0
num = 0

def listcount(liste, num):
    count = 0
    for i in liste:
        if i == num:
            count += 1
    return count

for i in L1:
    j = listcount(L1, i)
    if j > counter:
        counter = j
        num = i

print(f"Le nombre le plus frequent dans la liste est le: {num} ({counter}x)")
