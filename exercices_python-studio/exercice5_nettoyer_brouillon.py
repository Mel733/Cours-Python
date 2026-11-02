nombre = int(input())
with open("brouillon.txt", "w", encoding="utf-8") as brouillon:
    for _ in range(nombre):
        brouillon.write(input() + "\n")
        
lignes_propres = []
deja_vues = set()
compteur_supprimer = 0
compteur_conserver = 0
with open("brouillon.txt", "r", encoding="utf-8")as brouillon:
     for ligne in brouillon.read().splitlines():
          ligne = " ".join(ligne.split())
         
          if ligne == "":
              compteur_supprimer+=1
              continue
          ligne = ligne[0].upper()+ligne [1:]
         
          if ligne in deja_vues:
              compteur_supprimer+=1
              continue
          deja_vues.add(ligne)
          compteur_conserver+= 1
          lignes_propres.append(ligne)

with open("propre.txt", "w", encoding ="utf-8")as fichier:
    for ligne in lignes_propres:
        fichier.write(ligne + "\n")
        print(ligne)

print(f"Lignes conservées : {compteur_conserver}")
print(f"Lignes supprimées : {compteur_supprimer}")
