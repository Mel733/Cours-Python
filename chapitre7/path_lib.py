#module pathib pour manipuler les chemins de fichiers de maniére portable
#Path(__file__) pour obtenir le chemin du fichier courant
from pathlib import Path

chemin_courant = Path(__file__)
print(chemin_courant)

#parent de chemin courant
parent_courant = chemin_courant.parent
print(parent_courant)

dossier_script = parent_courant
dossier_sorties = parent_courant / "sorties"
print(dossier_sorties)
fichier_rapport = dossier_sorties / "rapport.txt"
print(fichier_rapport)

#crée le dossier(et ces parents =, sans erreur s'il existe déjà)
dossier_sorties.mkdir(parents=True, exist_ok=True)
print(f"Le dossier {dossier_sorties} a été crée ou existait déjà.")
print(f"Le dossier sorties existe : {dossier_sorties.exists()}")

with open(fichier_rapport, "w", encoding="utf-8") as f: #handle
    f.write("Rapport générer\n")
print(f"Le fichier rapport a été crée : {fichier_rapport.exists()}")

