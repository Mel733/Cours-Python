import random
nombre = random.randint(1,20)
nb_tentative = 0


  #Avec while pour effacer une tentative avec un chiffre invalide et une incrementation pour nb_tentatives
try :
 while nb_tentative != 5:
        nombre_choisi = int(input("Devine le nombre entre 1 et 20 : "))
        if 0>= nombre_choisi or nombre_choisi > 20:
            print("Veuillez entrer un nombre entre 1 et 20")
            print()
        elif nombre_choisi > nombre:
            print("C'est plus petit ")
        elif nombre_choisi<nombre :
            print("C'est plus grand")
            nb_tentative += 1
            print()
            print(f"tentative {nb_tentative}/5 : {nombre_choisi}") 

        if nombre == nombre_choisi:
            print()
            print(f"Bravo vous avez trouvé le chiffre : {nombre_choisi} en {nb_tentative} tentatives")
            break
 else: 
    print()
    print(f"Vous avez perdu, le chiffre secret était : {nombre}")
except ValueError:
  print("Veuillez rentrer un chiffre valide et non des lettres ou chiffres décimaux")
    

    #Avec for pour compter le chiffre invalide comme tentatives
# try :
#  for nb_tentative in range(1, 6):
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