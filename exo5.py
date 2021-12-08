while True:
    date = input("Entrez la date: ")
    if len(date) != 8 or not date.isdigit(): continue
    break

day = int(date[0] + date[1])
month = int(date[2] + date[3])
year = int(date[4] + date[5] + date[6] + date[7])

print(f"La date entrée est: {day}/{month}/{year}")

bissextile = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f"L'année {year} est bissextile!" if bissextile else f"L'année {year} est commune!")

if bissextile:
    monthLimit = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
else:
    monthLimit = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

monthOk = 1 <= month <= 12

if monthOk:
    dayOk = 1 <= day <= monthLimit[month - 1]
    if dayOk:
        print("La date est valide!")
    else:
        print("Le jour spécifié n'existe pas dans le mois!")
else:
    print("Le mois n'est pas compris entre 1 et 12!")
