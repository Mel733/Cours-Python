nom_etudiant = "Mélodie"
note_1 = 11.5
note_2 = 8.0
note_3 = 13.0
print("Étudiant:", nom_etudiant)
print("Notes:", note_1, note_2, note_3)
print("Moyenne:", (note_1 + note_2 + note_3) / 3)

#calculs :
nombre_de_notes = 3
somme_des_notes = note_1 + note_2 + note_3
moyenne = somme_des_notes / nombre_de_notes

#comparaison : le resultat sera un booelan
est_admis = moyenne >= 10

#affcihage des résultats
print("Nombre de notes :", nombre_de_notes)
print("Somme des notes :", somme_des_notes)
print("Moyenne :", moyenne)
print("Résultat de l'admission :", est_admis)

#verfication du typage
print("Type du 'nom_etudiant' :", type(nom_etudiant))
print("Type du 'nombre de notes' :", type(nombre_de_notes))
print("Type de la 'somme_des_notes' :", type(somme_des_notes))
print("Type de la 'moyenne' :", type(moyenne))
print("Type de 'est_admis' :", type(est_admis))

print("======Carnet de notes :========")
nom_etudiant =input("Quel est ton nom ?")
note1 = float(input("Note 1 (Sur 20) : ").replace(",", "."))
note2 = float(input("Note 1 (Sur 20) : ").replace(",", "."))
note3 = float(input("Note 1 (Sur 20) : ").replace(",", "."))

nombre_de_notes = 3
moyenne =(note1+note2+note3)/nombre_de_notes

print(f"Etudiant : {nom_etudiant}")
print(f"Notes : {note1:.2f},{note2:.2f}, {note3:.2f}")
print(f"Moyenne : {moyenne:.2f}")

#validiter des notes : une note est valide si elle est comprise entre 0 et 2O
notes_valide = (0<= note1 <= 20)and (0 <= note2 <= 20) and (0 <= note3 <= 20)

if not notes_valide:
    print("Erreur : une ou plusieur notes ne sont pas valide(doivent etre comprise entre 0 et 20)")
else:
 moyenne = (note1 + note2+ note3)/3
 if moyenne >= 16:
    mention = "Tres bien"
 elif moyenne >= 14:
    mention = "Bien"
 elif moyenne >= 12:
        mention = "Assez bien"
 elif moyenne >= 10:
        mention = "Passable"
 else:
    mention = "Insuffisante"
   

    est_admis = moyenne >= 10
    print(f"Etudiant : {nom_etudiant}")
    print (f"Notes : {note1:.2f},{note2:.2f}, {note3:.2f}")
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Mention : {mention}")

if est_admis :
    print("Décision: admis")
else :
    print("Décision : Refusé")

print("-----BOUCLES-----")
nom_etudiant = input("Nom de l'étudiant : ")

#Accumulateur :
somme_des_notes = 0.0
nombre_de_notes = 0
note_maximal = 0.0
note_minimal = 20.0

choix = ""
while choix != "0":
    print()
    print("1 : Ajouter une note")
    print("2 : Ajouter plusieur notes au menu")
    print("3 : Afficher le bulletin ")
    print("0: quitter")
    choix = input("Votre choix :")

    if choix == "1":
        note = float(input("Saisir une note /20 :").replace(",", "."))
        while note < 0 or note > 20:
             print ("Veuillez entrer une note valide")
             note = float(input("Saisir une note /20 :").replace(",", "."))

        somme_des_notes += note
        nombre_de_notes += 1

        if note < note_minimal :
                note_minimal = note
        if note > note_maximal :
                note_minimal = note
        
    elif choix =="2":
        quantite_notes = int(input("Combien de notes voulez vous ajouter ?"))
        for numero_note in range(1, quantite_notes +1):
            print(f"\n note {numero_note}sur{quantite_notes}:")
            note = float(input("Saisir une note /20 : ").replace(",", "."))
            while note < 0 or note > 20:
                  print ("Veuillez entrer une note valide")
                  note = float(input("Saisir une note /20 :").replace(",", "."))

    

            somme_des_notes += note
            nombre_de_notes += 1

            if note < note_minimal :
               note_minimal = note
            if note > note_maximal :
               note_maximal = note
        print(f"{quantite_notes}, notes ajouté")

    elif choix == "3":
        if nombre_de_notes == 0:
           print("Aucune note enregistrer")
        else:
            moyenne = somme_des_notes / nombre_de_notes
            # Ces 3 lignes doivent être alignées sous moyenne :
            print(f"Bulletin de {nom_etudiant} ")
            print(f"Nombre de notes : {nombre_de_notes} ")
            print(f"Moyenne : {moyenne:.2f}/20 :")
    elif choix == "0":
         print("Au revoir")
         break

    else:
        print("Choic invalide : tapez 1,2, 3 ou 0")