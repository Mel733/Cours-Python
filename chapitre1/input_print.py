#libéller : 

#saisi avec input()
age_saisi =input("Quel age as tu ? ")
print("Dans deux ans, tu auras", int(age_saisi) + 2)#affiche l'age avec un type int(renvoie un chiffre entier) + 2

prix=round(float(input("Quel est le prix de cet article ? ")), 2)#demande un prix float qui sera arrondi avec deux chiffre après la virgule
prix_formate = str(prix).replace(".", ",") #converti le prix en string pour remplacer le . par ,


print("Prix TTC :", prix_formate, "€")

#formater avec f-string
print(f"Prix TTC : {prix_formate} €")#affiche la même chose que au dessus

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
print("Il a dit : 'Bonjour'")

#backslash : \\
print("Dossier : C:\\Users\\Mélodie")

#=========================================================================================

