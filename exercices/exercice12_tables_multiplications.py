while True: #lance le programme a l'infinie
 try : #gestion de l'exeption avec ValueErreur
  nombre_choisi = int(input("Quelle nombre voulez vous choisir ? ")) #demande un nombre a l'user
  multiplicateur = int(input("Jusqu'a quel chiffre ? ")) #demande jusqu'a quelle nombre multiplier le nombre choisie

  print(f"========TABLE DE {nombre_choisi}========") #affichage
  for multiplicateur in range(1,multiplicateur + 1 ): #affiche la ligne si dessous selon le nombre de fois il faut multiplier le chiffre choisie
    print(f"{nombre_choisi} X {multiplicateur} = ", nombre_choisi * multiplicateur ) #affiche et fait le calcule a chaque tour de la boucle for
    
 except ValueError : #affiche le message d'erreur si c'est des lettres ou un mixte
  print("Merci de rentrer un chiffre entier")