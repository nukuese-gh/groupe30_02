note1 = float(input("Premiere note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisieme note : "))


moyenne = (note1+note2+note3) / 3

print(f"Moyenne : {moyenne}:.2f")

if moyenne >= 10 :
    print("L'étudiant est reçu. ")

else:
    print("L'étudiant n'est pas reçu")