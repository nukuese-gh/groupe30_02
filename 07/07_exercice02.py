entree = input("Entez des valeurs (séparées par des espaces ) : ")
liste = entree.split()

uniques = []

for item in liste:
    if item not in uniques:
        uniques.append(item)

print(f"Liste sans doublons : {uniques}")