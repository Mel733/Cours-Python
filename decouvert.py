# #manipulation chaine de caracteres
# mot="python"
# print(mot[0])#affiche le premier caractere qui est (p)
# print(mot[-1])#affiche lma dernirer lettre qui est le (n)
# print(mot[-2])#affiche l'avant dernirere lettre qui est le (o)
# print(mot[1:4])#affiche les caractere 1 à 3 qui spnt (yth)
# print(mot[:3])#affiche les 3 premier caractere qui sont pyt
# print(mot[3:])#affiche les 3 dernier caractere qui sont hon

# print(len(mot))#affiche la longeur du mot (6)

# #print(mot[9]) => erreur car l'index 9 n'existe pas dans la chaine python
# mot[::-1]#"nohtyp"

# #strip() supprime les espaces au début et a la fin d'une chaine
# texte ="   Bonjour   "
# print(texte.strip())#"Bonjour"

# #lower()convertit tous les caractères d'une chaine en miniscules
# print(texte.lower())#"   bonjour   "

# #upper() : convertit tous les caracteres d'une chaine en majuscules
# print(texte.upper())#"   BONJOUR   "

# #title() : convertit la premiere de chaque mot en majuscules
# prenom = "mélodie robert"
# print(prenom.title())#Mélodie Robert"

# #replace() : remplace une sous-chaine par une autre
# texte_modifie = texte.replace("Bonjour", "Bonsoir").strip()
# print(texte_modifie) #Bonsoir

# #find(): retourne l'index de la premiere occurence d'une sous-chaine, ou -1 si elle existe pas
# phrase ="Bonjour tout le monde"
# print(phrase.find("le")) #12
# print(phrase.find("la")) #-1

# #in : retourne True si une sous-chaine est présente dans la chaine, False sinon
# print("Bonjour" in phrase) #True
# print("Python" in phrase) #False

# #isdigit() : retourne True si tous les caractères de la chaine sont des chiffres, False sinon
# print("1234".isdigit()) #True
# print("1234a".isdigit()) #False

# #isalpha(): retourne True si tous les caractères de la chaine sont des lettres, False sinon
# print("abcde".isalpha()) #True
# print("abcde1".isalpha()) #False

# #liste : collections ordonnée et modifiable
# listePrenom = ["Mark", "Alicia", "Thomas", "Sélomey"]
# #accéder a un element de la liste en se réferant a son index

# print(listePrenom[1])#affiche alicia
# print(listePrenom[-1])#affiche sélomey
# # : slicing : liste [debut : fin]
# print(listePrenom[:2])#affiche les deux premiers élément de la liste
# print(listePrenom[1:2])#affiche mark et sélomey

vide = []
print (vide)#affiche []

plusieursTypes =["Melvin", 25, True, ["jaune", ["orange", "citron"], "rouge"]]

print(plusieursTypes[3][0], plusieursTypes[3][1][1])

nouvelExemple = [
                 ["Melvin", 25, True,["Jaune",["orange", "citron"], "rouge"]],
                 ["Alicia", 30, False, ["Bleu",["vert", "violet"], "noir"]]
                 ]
print(f"{nouvelExemple[0][0]} a {nouvelExemple[0][1]} ans et il aime l'{nouvelExemple[0][3][1][0]}et sa couleur est le {nouvelExemple[0][3][2]}" )
print(f"{nouvelExemple[1][0]} a {nouvelExemple[1][1]} ans et elle aime les couleurs : {nouvelExemple[1][3][1][0]}, {nouvelExemple[1][3][1][1]}, {nouvelExemple[1][3][2]}")

#les methodes de liste
#ajouter/ insère, retire, remplce des éléments
notes = [12.0, 15.5, 18.25]
print("Depart : ", notes)

#ajouter un élément a la fin de la liste : append()
notes.append(16.0)
print("Après append :", notes)

#retirer retire et renvoie le dernier élément : pop ()
derniere = notes.pop()
print(f"pop() renvoye {derniere}, reste : {notes}")

premiere = notes.pop(0)# parametre qui retire la premiere note = 12
print(f"pop() a retiré {premiere}, reste : {notes}")

notes.remove(15.5)
print(f"après remove(), reste : {notes}")

#nouvel insertion : insert(index.val)
notes.insert(1, 16)
print(f"Apres insert(1, 16), reste : {notes}")

#remplacer un élément :
notes[1] = 14.25
print(f"Après remplacement de l'élément, reste : {notes}")

#parcourir une liste :
prenoms = ["Mélodie", "Tim", "Mark-Erwann", "Sélomey", "Alicia", "Thomas", "Melvin"]
#tim : prenoms [1]
for prenom in prenoms : 
 print(prenom)

print(len(prenoms))#nombre de valeurs dans une liste



#boucler sur les index (ou indices ou cleé "key")
for index in range(0, len(prenoms)):
 print({index})# 0 1 2 3 4 5
 print(f"{prenom[index]}")#affiche les prénoms correspondant auw index 0 1 2 3 4 5