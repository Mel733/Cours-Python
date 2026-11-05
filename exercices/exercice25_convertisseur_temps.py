while True: #boucle infinie jusqu'a break
  try: #essaye le bout de code et si erreur, on passe au except
   temps_minutes = int(input("Combien de temps en minutes ? ")) #demande le temps minute en int a l'user
   if temps_minutes<0: #si le temps est négatif
      print("La durée ne peut pas etre négatives") #message
   else :
      temps_heures= temps_minutes //60 #sinon on calcule les heures
      reste_minutes = temps_minutes %60 #et le reste des minutes
      
      print(f"{temps_minutes} min vaut {temps_heures}h et {reste_minutes} min") #on affiche le resultat
      exit() #fin programme ou break
  except ValueError: #affiche message si input est une chaine par exemple
    print("Erreur sur la valeur")





