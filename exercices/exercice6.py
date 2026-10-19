montant_depot = 2
total = 0
nb_semaines = 10
numero_semaine = 0
cap = False

while total < 200 :
 
 for semaines in range (1, nb_semaines + 1):

 
  numero_semaine += 1
  total += montant_depot
  
 
 
  if semaines % 3 == 0:
    total += 5
    print(f"Semaine {numero_semaine} : dépot de {montant_depot}, total = {total}(+5 euro Bonus de mamie)")
    print()
        
        
  else :
    print(f"Semaine {numero_semaine} : dépot de {montant_depot}, total = {total}")

  if total >= 50 and cap == False :
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

   