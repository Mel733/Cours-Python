with open("journal.txt", "w", encoding="utf-8") as journal:   #ouvre (ou crée) journal.txt en écriture ("w" écrase l'ancien contenu)
    journal.write("Ligne 1 : Démarrage du journal\n")   #écrit la première ligne du journal, "\n" = retour à la ligne

nombre = int(input())   #demande combien d'événements on va saisir (conversion str -> int)
with open("journal.txt", "a", encoding ="utf-8")as journal:   #rouvre le fichier en mode ajout ("a") : on écrit à la suite sans effacer
  for i in range(2, nombre + 2):   #i va de 2 à nombre+1 (la ligne 1 existe déjà, donc on numérote à partir de 2)
      evenement = input()   #demande le texte de l'événement
      journal.write(f"Ligne {i} : {evenement}\n")   #écrit la ligne numérotée dans le fichier avec l'événement

print(f"Lignes dans le journal : {nombre+1}")   #affiche le total : les événements + la ligne de démarrage
mot_cle = input().lower()   #demande le mot-clé et le met en minuscules (pour ignorer la casse)

trouve = False   #indicateur : passera à True si au moins une ligne correspond
with open("journal.txt", "r", encoding = "utf-8")as journal:   #ouvre le journal en lecture ("r")
    for ligne in journal.read().splitlines():   #read() lit tout, splitlines() découpe en liste de lignes (sans les "\n")
        if mot_cle in ligne.lower() :   #si le mot-clé est contenu dans la ligne (également mise en minuscules)
            print(ligne)   #on affiche la ligne trouvée (version originale, avec ses majuscules)
            trouve =True   #on note qu'au moins une ligne a été trouvée
if not trouve:   #si aucune ligne ne contenait le mot-clé
    print("Aucune ligne trouvée")   #on affiche un message