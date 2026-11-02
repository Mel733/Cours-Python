#Ouvrir et lire un fichier:
with open("texte.txt", "r", encoding="utf-8") as f:
    # open(nom, mode, encoding) ouvre le fichier.
    #   "r" = read (lecture), c'est le mode par défaut.
    #   encoding="utf-8" évite les problèmes avec les accents (é, è...).
    # "with" ferme automatiquement le fichier à la fin du bloc.
    # "as f" : f est l'objet fichier qu'on utilise ensuite.
    contenu = f.read()
    # read() lit TOUT le fichier dans une seule chaîne :
    # contenu = "Alice 12\nBob 8\nChloé 15\n"
    # \n est le retour à la ligne (invisible quand on affiche).

print(contenu)
# Après le with, le fichier est fermé, mais contenu reste utilisable.
#-----------------------------------------------------------------------------
#Les trois facons de lire:
with open("texte.txt", encoding="utf-8") as f:
    ligne = f.readline()
    # Lit UNE seule ligne : "Alice 12\n"
    # Si on rappelle f.readline(), on obtient la suivante : "Bob 8\n"

with open("texte.txt", encoding="utf-8") as f:
    lignes = f.readlines()
    # Liste de toutes les lignes :
    # ["Alice 12\n", "Bob 8\n", "Chloé 15\n"]

with open("texte.txt", encoding="utf-8") as f:
    for ligne in f:
        # La méthode la plus courante : on parcourt le fichier ligne par ligne.
        # 1er tour : ligne = "Alice 12\n"
        print(ligne.strip())
        # strip() enlève les espaces et le \n aux extrémités : "Alice 12"
#------------------------------------------------------------------------------------
#Exemples concret : traiter les données
        notes = {}   # dictionnaire vide, qui contiendra {"Alice": 12, ...}

with open("texte.txt", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        # "Alice 12\n" -> "Alice 12"
        if ligne == "":
            continue
        # On saute les lignes vides (sinon split() donnerait une liste vide
        # et la ligne suivante planterait).
        nom, note = ligne.split()
        # "Alice 12".split() -> ["Alice", "12"]
        # nom = "Alice", note = "12" (encore du texte !)
        notes[nom] = int(note)
        # int("12") -> 12 ; notes = {"Alice": 12}

print(notes)
# {'Alice': 12, 'Bob': 8, 'Chloé': 15}
print(sum(notes.values()) / len(notes))
# (12 + 8 + 15) / 3 = 11.666...
#------------------------------------------------------------------------------------
#Avec une compréhension
with open("texte.txt", encoding="utf-8") as f:
    notes = [int(ligne.split()[1]) for ligne in f if ligne.strip()]
    # [12, 8, 15]
    # "if ligne.strip()" ne garde que les lignes non vides.
#------------------------------------------------------------------------------------------
#Ecrire dans un fichier    
    with open("resultat.txt", "w", encoding="utf-8") as f:
    # "w" = write : crée le fichier, ou ÉCRASE son contenu s'il existe déjà !
     f.write("Résultats\n")
    # write() n'ajoute PAS de retour à la ligne tout seul : il faut écrire \n.
    f.write(f"Moyenne : {11.67}\n")
    # Le fichier contient maintenant :
    # Résultats
    # Moyenne : 11.67

with open("resultat.txt", "a", encoding="utf-8") as f:
    # "a" = append : AJOUTE à la fin sans effacer ce qui existe.
    f.write("Fin\n")