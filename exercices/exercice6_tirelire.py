
total = 0
nb_semaines = 10
numero_semaine = 0
cap = False

while total < 200 :
 
 for semaines in range (1, nb_semaines + 1):
 
  numero_semaine += 1
  montant_depot = numero_semaine * 2 #calucle le depot en multipliant le numero de la semaine fois 2
  total += montant_depot
  
 
 
  if semaines % 3 == 0:
    total += 5
    print(f"Semaine {numero_semaine} : dépot de {montant_depot}, total = {total}(+5 euro Bonus de mamie)")
    print()
        
        
  else :
    print(f"Semaine {numero_semaine} : dépot de {montant_depot}, total = {total}")

  if total >= 50 and not cap:
    print("Cap des 50 euros franchis")
    print()
    cap = True

  montant_depot+= 2
  if total >= 200 :
    break
  

print (f"Il faut {numero_semaine} semaines pour acheter le vélo (total : {total} euro)")
print ("-"*30)

if total>= 100:
   print("Objectif atteint")
else :
   print ("Continue tes efforts")
print()

   


#Alternative a la partie 3
# total = 0
# semaine = 0

#while total < 200:
  #semaine += 1
  #depot = semaine * 2
  #if semaine %3==0:
    #depot += 5
    #total += depot
#print(f"Il faut {semaine} semaines pour atteindre {total} euro et achter le vélo")



    #Partie 4:
solde = 0
choix =""
while choix !="3":
      print(f"-----Tirelire de Mélodie (solde : {solde})")
      print ("1.Déposer\n2.Retirer \n3. Quitter")
      choix = input("Votre choix: ")

      if choix == "1":
        montant = int(input("Quelle est la somme a déposer ?: "))
        if(montant>0):
          solde += montant
          print (f"Vous avez déposer {montant}")
        else :
          print("Montant invalide, veuillez entrer un nombre positif")


      elif choix == "2":
        montant = int(input("Montant a retirer :"))
        if montant <= 0:
          print("Le montant a retirer doit etre positif")
        elif montant > solde:
          print("Retrait refusé! Solde insuffisant")
        else :
          solde -= montant
          print(f"Vous avez retiré {montant}")

      elif choix =="3":
        print ("Au revoir")

      else :
       print("Choix invalide, veuillez reesayer")
    


