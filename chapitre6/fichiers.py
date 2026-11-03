
# Ouvrir et lire un fichier :
with open("texte.txt", "r", encoding="utf-8") as f:
    # "r" = lecture (mode par défaut), encoding="utf-8" évite les problèmes d'accents.
    # "with" ferme automatiquement le fichier à la fin du bloc.
    contenu = f.read()
    # read() lit TOUT le fichier dans une seule chaîne :
    # "Alice 12\nBob 8\nChloé 15\n"   (\n = retour à la ligne)

print(contenu)   # le fichier est fermé, mais contenu reste utilisable
#-------------------------------------------------------------------------
# Les trois façons de lire :
with open("texte.txt", encoding="utf-8") as f:
    ligne = f.readline()    # lit UNE ligne : "Alice 12\n" (un 2e appel donne la suivante)

with open("texte.txt", encoding="utf-8") as f:
    lignes = f.readlines()  # liste de toutes les lignes : ["Alice 12\n", "Bob 8\n", ...]

with open("texte.txt", encoding="utf-8") as f:
    for ligne in f:                # la plus courante : ligne par ligne
        print(ligne.strip())       # strip() enlève espaces et \n aux extrémités : "Alice 12"
#-------------------------------------------------------------------------
# Exemple concret : traiter les données
notes = {}   # contiendra {"Alice": 12, ...}

with open("texte.txt", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()          # "Alice 12\n" -> "Alice 12"
        if ligne == "":
            continue                   # on saute les lignes vides (sinon le split planterait)
        nom, note = ligne.split()      # ["Alice", "12"] : note est encore du texte
        notes[nom] = int(note)         # conversion en int : {"Alice": 12}

print(notes)                                # {'Alice': 12, 'Bob': 8, 'Chloé': 15}
print(sum(notes.values()) / len(notes))     # (12 + 8 + 15) / 3 = 11.666...
#-------------------------------------------------------------------------
# Avec une compréhension :
with open("texte.txt", encoding="utf-8") as f:
    notes = [int(ligne.split()[1]) for ligne in f if ligne.strip()]
    # [12, 8, 15] : "if ligne.strip()" ne garde que les lignes non vides
#-------------------------------------------------------------------------
# Écrire dans un fichier :
with open("resultat.txt", "w", encoding="utf-8") as f:
    # "w" = write : crée le fichier, ou ÉCRASE son contenu s'il existe déjà !
    f.write("Résultats\n")             # write() n'ajoute PAS de \n tout seul
    f.write(f"Moyenne : {11.67}\n")

with open("resultat.txt", "a", encoding="utf-8") as f:
    # "a" = append : AJOUTE à la fin sans effacer ce qui existe
    f.write("Fin\n")

# Le fichier contient maintenant :
# Résultats
# Moyenne : 11.67
# Fin