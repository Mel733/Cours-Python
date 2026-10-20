
while True : #prédicat
    try:
        annee= int(input("Quelle est votre année de naissance ?"))
        if 1900<= annee <= 2026:
            break
        else:
            print("Erreur, veuillez renter une année valide entre 1900 et 2026")

    except ValueError: #affiche une erreur au lieu de l'erreur du terminal
        print ("Erreur : veullez saisir un nombre entier pour l'année")

age = 2026 - annee
print(f"Vous avez {age} ans ")





