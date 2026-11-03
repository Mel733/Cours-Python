nombre = int(input())    #demande combien de lignes on va saisir (conversion str -> int)
with open("brouillon.txt", "w", encoding="utf-8") as brouillon:   #ouvre (ou crée) brouillon.txt en écriture ("w" écrase l'ancien contenu), with ferme le fichier automatiquement
    for _ in range(nombre):    #pour chaque ligne à saisir (_ = variable jetable)
        brouillon.write(input() + "\n")   #écrit la saisie dans le fichier, "\n" = retour à la ligne

lignes_propres = []    #liste qui contiendra les lignes nettoyées
deja_vues = set()    #ensemble des lignes déjà rencontrées (un set ne garde pas de doublons et la recherche est rapide)
compteur_supprimer = 0    #compte les lignes supprimées (vides ou doublons)
compteur_conserver = 0    #compte les lignes conservées
with open("brouillon.txt", "r", encoding="utf-8")as brouillon:    #ouvre brouillon.txt en lecture ("r")
     for ligne in brouillon.read().splitlines():    #read() lit tout le fichier, splitlines() le découpe en liste de lignes (sans les "\n")
          ligne = " ".join(ligne.split())     #split() découpe aux espaces (et supprime les espaces en trop), join() recolle avec un seul espace

          if ligne == "":    #si la ligne est vide après nettoyage
              compteur_supprimer+=1    #on la compte comme supprimée
              continue    #on passe directement à la ligne suivante
          ligne = ligne[0].upper()+ligne [1:]    #première lettre en majuscule + le reste de la ligne inchangé (tranche à partir de l'index 1)

          if ligne in deja_vues:    #si la ligne a déjà été rencontrée (doublon)
              compteur_supprimer+=1    #on la compte comme supprimée
              continue    #on passe à la ligne suivante
          deja_vues.add(ligne)    #sinon on l'ajoute à l'ensemble des lignes vues
          compteur_conserver+= 1    #on la compte comme conservée
          lignes_propres.append(ligne)    #on l'ajoute à la liste des lignes propres

with open("propre.txt", "w", encoding ="utf-8")as fichier:    #ouvre (ou crée) propre.txt en écriture
    for ligne in lignes_propres:    #pour chaque ligne propre
        fichier.write(ligne + "\n")    #on l'écrit dans le fichier avec un retour à la ligne
        print(ligne)    #et on l'affiche aussi à l'écran

print(f"Lignes conservées : {compteur_conserver}")   #affiche le nombre de lignes conservées
print(f"Lignes supprimées : {compteur_supprimer}")   #affiche le nombre de lignes supprimées