# Demande d'informations à l'utilisateur 

prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre age : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# Approximation des jours vecus 

jours_vecus = age*365

# Affichage formaté 
print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vecus} jours vecus environ)")
print(f"ville : {ville}")
print(f"Métier : {metier}")