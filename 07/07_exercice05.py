entree = input("Entrez des éléments : ")
liste = entree.split()

liste_inversee = []

for i in range(len(liste)-1, -1, -1):
    liste_inversee.append(liste[i])

print(f"Liste inversibe : {liste_inversee}")