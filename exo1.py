while True:
    try:
        nb = float(input("Quelle table de multiplication: "))
        break
    except ValueError:
        continue

result = []
for i in range(10):
    result.append(nb*i)

for i in result:
    print(f"{nb} x {int(i/nb)} = {round(i, 2)}")
