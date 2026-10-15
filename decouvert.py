#opérateur arithmétique
print("7+2 =", 7 + 2)
print("7-2 =", 7 - 2)
print("7*2 =", 7 * 2)
print("7/2 =", 7 / 2)

print("7%2 =", 7 % 2)

#priorité des opérateurs
print("7+2*3 =", 7 + 2 * 3)
print("(7+2)*3 =", (7 + 2) * 3)

#comparaison : résultat boolean
print("7 > 2 =", 7 > 2)
print("7 < 2 =", 7 < 2)
print("7 == 2 =", 7 == 2)
print("7 != 2 =", 7 != 2)


#arrondis ete concversion de type :
print("Arondis de 34.234567890: " , round(34.234567890, 2)) #combien de chiffre apres la virgule
print ("Conversion de type :", int(34.12345678))
print("Conversion de type:", float(34))

#abération de code: flottant
print ("0.1 + 0.2 =", 0.1 + 0.2)
print ("0.1 + 0.2 =",round( 0.1 + 0.2, 1))

print ("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

#saisi avec input()
age_saisi =input("Quel age as tu ? ")
print("Dans deux ans, tu auras", int(age_saisi) + 2)

prix=round(float(input("Quel est le prix de cet article ? ")), 2)
prix_formate = str(prix).replace(".", ",")


print("Prix TTC :", prix_formate, "€")

#formater avec f-string
print(f"Prix TTC : {prix_formate} €")

nom ="Mélodie"
moyenne = 15.5
nombre_de_notes = 3
print(f"Nom : {nom}, Moyenne : {moyenne}, Nombre de notes : {nombre_de_notes}")

#.2f pour arrondir à 2 chiffres après la virgule
print(f"Nom : {nom}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

#:> 10 pour aligner à droite sur 10 caractères
print(f"Nom : {nom :>10}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")
#:< 10 pour aligner à gauche sur 10 caractères
print(f"Nom : {nom :<10}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")
#:^ 10 pour centrer sur 10 caractères
print(f"Nom : {nom:^10}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

#les caractères d'échappement
#saut de ligne :\n
print("Ceci est une ligne\nCeci est une autre ligne")

#tabulation : \t
print("Nom\t/Moyenne\tNombre de notes")

#guillemets : \" ou \'
print("Il a dit : \"Bonjour\"")


