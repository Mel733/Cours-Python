#module pathib pour manipuler les chemins de fichiers de maniére portbale

#Path(__file__) pour obtenir le chemin du fichier courant
from pathlib import Path
chemin_courant = Path(__file__)
print(chemin_courant)