import csv
from pathlib import Path

CHEMIN_CSV = Path(__file__).parent/"temperature.csv"
lignes = [
    ["Ville", "Température"], 
    ["Paris", 12.5],
    ["Lyon", "erreur"],
    ["Nice", 18]
]


def lire_temperatures():
    resultat = []
    with open(CHEMIN_CSV, "r", encoding="utf-8") as f:
        reader_var = csv.reader(f, delimiter=";")
        next(reader_var)
        for ligne in reader_var:
            try:
                temperature = float(ligne[1].replace(",", "."))
                resultat.append((ligne[0], temperature))
                
            except (ValueError, IndexError):
                continue
        print(resultat)
    return resultat

# def ecrire_temperature(donnee):
#     try:
#         with open(CHEMIN_CSV, "w", encoding="utf-8", newline="") as f:
#             writer_var = csv.writer(f, delimiter=";")
#             writer_var.writerow(["Ville", "Temperature"])      
#             for l in donnee:
#                 writer_var.writerow(l)  
#     except FileNotFoundError:
#         print("Le fichier n'existe pas")


# ecrire_temperature()