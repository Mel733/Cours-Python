import csv
from pathlib import Path

CHEMIN_CSV = Path(__file__).parent/ "sorties" / "data.csv" #Chemin non modifiable
#CSV : Comma Seperated Values
#Chaque ligne est une liste de valeurs sépraer par des virgules (ou; selon le format)
lignes = [
    ["Nom", "Prénom", "Moyenne"], #ligne d'en-têtes
    ["Dupont", "Jean", 15],
    ["Martin", "Claire", 13],
    ["Durand", "Paul", 8]
]

# --- Écriture avec le module csv ---
CHEMIN_CSV.parent.mkdir(parents=True, exist_ok=True)  # crée le dossier s'il n'existe pas
with open(CHEMIN_CSV, "w", encoding="utf-8", newline="") as f:  # ouvre le fichier en écriture
    writer_var = csv.writer(f, delimiter="|")       # crée l'outil qui écrit du CSV
    for l in lignes:             # pour chaque sous-liste dans la liste
        writer_var.writerow(l)       # l'écrit comme une ligne

# --- Lecture avec csv ---
with open(CHEMIN_CSV, "r", encoding="utf-8") as f:
    reader_var = csv.reader(f, delimiter="|")       # crée l'outil qui lit du CSV
    for ligne in reader_var:         #Pour chaque ligne dans le reader
        print(ligne)              #on affiche la ligne(une des liste)

# --- Écriture version brute (sans csv) ---
CHEMIN_CSV.parent.mkdir(parents=True, exist_ok=True)
with open(CHEMIN_CSV, "w", encoding="utf-8", newline="") as f:
    for l in lignes:
        # convertit chaque élément en texte, les colle avec des virgules, ajoute un retour à la ligne
        f.write("|".join(str(infos) for infos in l) + "\n")

# --- Lecture brute : affiche le texte tel quel ---
with open(CHEMIN_CSV, "r", encoding="utf-8") as f:  # ouvre en lecture
    contenu = f.read()           # lit tout le fichier dans une seule chaîne
    print(contenu)

