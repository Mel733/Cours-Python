#écrire, compléter et lire un fichier avec gestion des execptions
#les lettres: w (write), a(append), r(read)

#w: write, crée un fichier ou écrase le contenu existant
with open("journal.txt", "w", encoding="utf-8")as fichier:
#encodage : séance => Sa@ance
    try:
        fichier.write("Séance numéro 1\n")
        fichier.write("Séance numéro 2\n")
    except Exception as error:
            print(f"Une erreur est survenue : {error}")


#a : append, ajoute du contenue a la fin du fichier
#Si le fichier n'existe pas il le crée
with open("journal.docx", "a", encoding="utf-8") as fichier:
    try:
       fichier.write("Seance 4\n")
    except Exception as error:
          print(f"Une erreur est survenue : {error} ")


#r : read, lit le contenue d'un fichier
try:
    with open("journal.php", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(contenu)
except Exception as error:
    print(f"Une erreur est survenue : {error}")
    with open("journal.log", "a", encoding="utf-8") as journal:
        journal.write(f"Une erreur est survenue : {error}\n")
    print("Une erreur est survenue, veuillez consulter le journal.log")
     




