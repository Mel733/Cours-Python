import string #importe le module string
frequences = {} #dictionnaire fréquence : mot : nombre d'apparitions
total_mots = 0 #initialisé à 0
somme_longueur = 0 #initialisé à 0
try: #fait le bloc de code et si une erreur on saute au except
     fichier_choix = input("Quel fichier.txt voulez choix choisir ? ") #demande à l'user de choisir le fichier

     with open(fichier_choix, "r", encoding="utf-8") as fichier_analyser: #on l'ouvre et on le lit
       for ligne in fichier_analyser: #pour chaque ligne dans le fichier
           for mot in ligne.split(): #on regarde chaque mot dans la phrase découpée
             mot_clean = mot.strip(string.punctuation) #on nettoie les mots et on ignore les ponctuations autour du mot
             if mot_clean : #si le mot n'est pas vide après le nettoyage
                   total_mots += 1 #incrémente de 1
                   somme_longueur += len(mot_clean) #on ajoute la longueur du mot dans somme longueur
                   frequences[mot_clean] = frequences.get(mot_clean, 0) + 1 #ajoute 1 à la fréquence du mot (0 si c'est la première fois)
except FileNotFoundError: #erreur si le fichier existe pas
    print("Ce fichier n'existe pas")
    exit() #on arrete le programme

if total_mots == 0: #si le total est de 0
    print("Impossible de faire une division par 0 pour la moyenne") #message d'avertissement
    exit() #on arrête le programme

print("ANALYSEUR DE FICHIER TEXTE") #affichage
print(f"Fichier à analyser : {fichier_choix}\n") #affiche le fichier choisi
print("====STATISTIQUES====") #titre de la partie statistiques
print(f"Nombre total de mots : {total_mots}") #affiche le nombre total de mots
print(f"Mots uniques : {len(frequences)}") #affiche le nombre de mots uniques
print(f"Longueur moyenne : {(somme_longueur/total_mots):.2f}") #calcule la longueur moyenne des mots (2 décimales)
print(f"Mot le plus long : {max(frequences, key=len)} ") #affiche le mot le plus long
print(f"Mot le plus court : {min(frequences, key =len)}\n") #affiche le mot le plus court

print("===TOP 10 MOTS FREQUENTS===") #titre de la partie top 10
top10 = sorted( frequences.items() , key=lambda paire : paire[1], reverse=True)[:10] #trie les paires (mot, nombre) du plus fréquent au moins fréquent, garde les 10 premières
for numero, (mot, nombre)in enumerate(top10, start=1): #boucle for pour afficher les 10 mots les plus fréquents, avec un enumerate qui commence à 1
    longueur_barre =int(nombre*30/top10[0][1]) #pour calculer la longueur de la barre (30 caractères max pour le mot le plus fréquent)
    print(f"{numero}. {mot} : {nombre} ({nombre/ total_mots* 100:.1f}%) {"█"*longueur_barre} ") #message affichage : rang, mot, nombre, pourcentage, barre