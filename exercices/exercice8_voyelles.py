choix=""

def compteur_voyelle (texte):
    voyelle = "aeiouyéèàùîÏ"
    nb_voyelle = 0
    for caracter in texte.lower():
        if caracter in voyelle:
            nb_voyelle += 1
    return nb_voyelle


def demander_choix():
    while True :
      print("------Compteur de voyelles------")
      print("1.Analyser une phrase \n2.Quitter")

        

      try :
   
        choix=input("Quelle est votre choix ?")

        if choix == "1" or choix == "2":
            return choix
        else:
            print("erreur : choix invalide")

      except ValueError:
          print("Merci de choisir 1 ou 2")

def lancer_programme():
    while True:
        choix = demander_choix()

        if choix == "1" :
            phrase =input("Quelle est votre phrase ?")

            if phrase.strip()=="":
                print("Erreur la phrase ne peut pas etre vide")

            else :
                nombre_voyelle = compteur_voyelle(phrase)
                print(f"La phrase contient : {nombre_voyelle} voyelles")

        elif choix == "2":
            print("Au revoir")
            break

lancer_programme()
           
          