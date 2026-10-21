import random
nombre = random.randint(1,20) # indique que random dois utilsier un chiffre int entre 1 et 20, cette valeur sera stoker dans nombre
nb_tentative = 0 #initialise le nombre de tentatives a zéro


#Avec while pour effacer une tentative avec un chiffre invalide et une incrementation pour nb_tentatives :

try : #gestion exeption avec le ValueError
 while nb_tentative != 5: #lance le programme jusque se que le nombre de tentatives soit de 5
        nombre_choisi = int(input("Devine le nombre entre 1 et 20 : "))#indique qu'un int doit etre retourner

        if 0>= nombre_choisi or nombre_choisi > 20: #si le chiffre est inférieur ou égal a 0 ou superieur a 20:
            print("Veuillez entrer un nombre entre 1 et 20")#le message d'affiche
            print()
            nb_tentative -= 1 #enlever une tentative pour laisser au user 5 tentatives avec chiffre valide
        elif nombre_choisi > nombre:  #si le nombre choisi par l'user est plus grand que le nombre
            print("C'est plus petit ") #indice indiquer

        elif nombre_choisi<nombre : #si le nombre choisi est plus petit
            print("C'est plus grand") #indice indiquer
        nb_tentative += 1 #nombre de tentaives + 1
        print()
        print(f"tentative {nb_tentative}/5 : {nombre_choisi}") #affiche le nombre de tentaive et le chiffre mit par l'user

        if nombre == nombre_choisi: #si le chiffre est le chiffre secret
            print()
            print(f"Bravo vous avez trouvé le chiffre : {nombre_choisi} en {nb_tentative} tentatives") #affiche se message et le nombre de tentatives
            break #fin programme
 else: #autre si nb_tentative > 5 alors
  print()
  print(f"Vous avez perdu, le chiffre secret était : {nombre}") #affiche se message et revele le chiffre secret

except ValueError: #erreur afficher lorsque lettres sont écrit dans le input
  print("Veuillez rentrer un chiffre valide et non des lettres ou chiffres décimaux")
    

    #Avec for pour compter le chiffre invalide comme tentatives :
# try :
#  for nb_tentative in range(1, 6): #augmente 1 le nombre de tentaives a chaque tour de boucle jusqu'a 5. nb_tentaives prendra a chaque fois +1
#   nombre_choisi = int(input("Devine le nombre entre 1 et 20 : "))
#   if 0>= nombre_choisi or nombre_choisi > 20:
#      print("Veuillez entrer un nombre entre 1 et 20 :")
  
#   elif nombre_choisi > nombre:
#     print("C'est plus petit ")
#   elif nombre_choisi<nombre :
#     print("C'est plus grand")
#     print(f"Tentative {nb_tentative}/5 : {nombre_choisi}") 

#  if nombre == nombre_choisi:
#       print(f"Bravo vous avez trouvé le chiffre : {nombre_choisi} en {nb_tentative} tentatives")
  
#  else: 
#     print(f"Vous avez perdu, le chiffre secret était : {nombre}")
# except ValueError:
#   print("Veuillez rentrer un chiffre valide et non des lettres ou chiffres décimaux")