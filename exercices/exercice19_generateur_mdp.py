import random #import le module random
import string #importe le module string

caractere ="!@#$%&*" + string.ascii_lowercase + string.ascii_uppercase + string.digits 
#la variable caractere contient tout les chiffre, caractere spéciaux, lettre en maj et min


while True: #bouble infinie jusqu'a le user choisise n
    mot_de_passe ="" #variable mdp qui stockera tout les caractere
    try: # tente d'exécuter ce bloc ; si une exception survient, on passe au except
     longueur = int(input("Quelle longueur votre mot de passe ?")) #demande la longeur en int a l'user
     if longueur <5 or longueur>20:
       print("Votre mot est passe est soit trop long ou top court\n Il doit faire minimum 5 caractere jusqu'a 20 max")
       print()
     else:
        for _ in range(longueur): #pour la longueur demander
          un_caractere = random.choice(caractere) #on affecte a la variable un caractere, un choix aléatoire de la variable caractere
          mot_de_passe += un_caractere #on l'ajoute au mdp

        print(f"Votre mot de passe généré en {longueur} caractères : {mot_de_passe}") #on affiche le mdp
        print()
        refaire = input("Veut tu en régénerer un autre ? o/n ") #le résultat de le'input s'affecte dans la variable refaire
        if refaire != "o" : #si c'est tout sauf o
         break #on stoppe le programme
    except ValueError: #si on met des lettres dans le input
      print("Merci de rentrer un chiffre")





