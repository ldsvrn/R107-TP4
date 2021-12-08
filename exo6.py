tab = [5, 2, 4, 8, 1, 3]
print(tab)

# absolument pas opti mais 'fonctionne'
for i in range(len(tab)):
    temp = tab[i]

    index=0
    for j in range(i, len(tab)):
        if tab[j] < temp:
            temp = tab[j]
            index = j
            #print(f"DEBUG: j = {j}, tab[j] = {tab[j]}, temp = {temp}, index = {index}, i = {i}")

    if index != 0:
        tab[index] = tab[i]
        tab[i] = temp
    print(f"Phase {i}: {tab}")
