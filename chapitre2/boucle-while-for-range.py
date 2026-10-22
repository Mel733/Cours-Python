 #while : execute tant que la condition est vrai
       
#compteur simple
compteur = 1
while compteur <= 5:
      print ("Tour numéro :", compteur)
      compteur += 1 #sans cette ligne , la boucle ne s'arrete pas
      print ("Fin de la boucle. Valeur de colpteur :", compteur)
print("Fin de la boucle. Valeur du compteur : ", compteur)
print("-"*40)

#somme
somme = 0
nombre = 1
while nombre <= 4:
   somme += nombre
   print (f"on ajoute: {nombre}, la Somme vaut maintenant : {somme}")
   nombre += 1
print ("Fin de la boule. Valeur de nombre :", nombre)
print ("Fin de la boucle. Valeur de somme :", somme)
print("-"*40)


#Vérification saisi
note = float(input("Saisissez votre note /20 ").replace(",","."))
while note <0 or note> 20:
   print ("note invalide")
   note = float(input("Saisissez votre note /20 ").replace(",","."))
print (f"note valide:  {note: .2f}")
print("-"*40)

#boucle infini = 1
#compteur = 1
#somme = 0
#while compteur <=3:
 #somme += compteur
#print("Somme :", somme)

#boucles for et range
   #for : répete son bloc pour chaque élément d'une séquence
   #range () : génère une séquence de nombre, ex: range(5) -> 0, 1, 2, 3, 4
   #range (fin): range (0) => -1
   #range(début, fin) : range (3, 9) -> 3,4,5,6,7,8
   #range (Début, fin, pas): range ( 2, 10, 2) -> 2,4,6,8

for i in range (5):
    print ("Tour numéro :", i, end =" ")
print("-"*40)

for note in range (0, 21, 5):
      print("Note :", note, end=" ")
print("-----------------------------------------")

for i in range(3, -10, -1):
    print (i, end=" ")
print()
print("-"*40)

#Break et continue
   #break : permet de sortir immédiatement d'une boucle
   #continue : permet de poser immédiatement a l'itéraction suivante de la boucle

print ("Nombres impaires de 1 à 9")
for iteration in range(1, 10):
   if iteration % 2 ==0:
      continue  #nombre pair, on passe a l'itéraction suivante
   print(iteration, end =" ") #nombre impaire
   print()

print("Recherche du premier multiple de 7 a partir de 50 :")
for nombre in range (50, 100):
      if nombre % 7 ==0:
            print ("trouvé:", nombre)
            break
print ("Fin de la recherche")
print("-"*40)

#Boucle infinies
while True:
   reponseUser = input ("Tapez la touche h pour quitter:")
   if reponseUser.lower() == "h": #attend que le user tape h
      break
print ("Fin de la boucle infinie")
print("-"*40)  

#boucles imbriqué
#ent-tête
print ("      ", end ="")
for colonne in range (1, 6):
   print(f"{colonne:>4}", end =" ")#permet de retourner a la ligne
print ()#retour a la ligne
print("-" *30)

#corp de la table
for ligne in range(1, 6):
      print (f"{ligne:>2}| ", end =" ")
      for colonne in range (1, 6):
         print (f"{ligne * colonne:>4}", end=" ")
      print ()