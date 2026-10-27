#liste : collections ordonnée et modifiable
listePrenom = ["Mark", "Alicia", "Thomas", "Sélomey"]

#accéder a un element de la liste en se réferant a son index
print(listePrenom[1])#affiche alicia
print(listePrenom[-1])#affiche sélomey
# : slicing : liste [debut : fin]
print(listePrenom[:2])#affiche les deux premiers élément de la liste
print(listePrenom[1:2])#affiche mark et sélomey

vide = []
print (vide)#affiche []

# ---------- EXEMPLE 1 : une liste imbriquée ----------

# Niveau 1 : la grande liste
# Index :          0         1    2      3
plusieursTypes = ["Melvin", 25, True, ["jaune", ["orange", "citron"], "rouge"]]

# Niveau 2 : la sous-liste qui est à l'index 3
# plusieursTypes[3] = ["jaune", ["orange", "citron"], "rouge"]
# Index :                 0              1               2

# Niveau 3 : la sous-sous-liste qui est à l'index 1 de la sous-liste
# plusieursTypes[3][1] = ["orange", "citron"]
# Index :                    0         1


# L'élément 3 est lui-même une liste :  ["jaune", ["orange", "citron"], "rouge"]
#   - [3][0] -> "jaune"
#   - [3][1] -> ["orange", "citron"]  (encore une liste !)
#   - [3][2] -> "rouge"
#
# Et dans ["orange", "citron"] :
#   - [3][1][0] -> "orange"
#   - [3][1][1] -> "citron"

print(plusieursTypes[3][0], plusieursTypes[3][1][1])
#                    │  │                  │  │  └─ 2e élément de ["orange", "citron"] -> "citron"
#                    │  │                  │  └──── 2e élément de la liste du 3 -> ["orange", "citron"]
#                    │  │                  └─────── élément 3 de plusieursTypes -> la grande sous-liste
#                    │  └─ 1er élément de la sous-liste -> "jaune"
#                    └──── élément 3 de plusieursTypes -> la grande sous-liste
# Affiche : jaune citron


# =====================================================================
# EXEMPLE 2 : une liste de listes (3 niveaux d'imbrication)
# =====================================================================
#
# STRUCTURE (à lire de l'extérieur vers l'intérieur) :
#
#   Niveau 1 : nouvelExemple            -> contient 2 personnes
#   Niveau 2 : nouvelExemple[0]         -> une personne (Melvin ou Alicia)
#   Niveau 3 : nouvelExemple[0][3]      -> ses couleurs
#   Niveau 4 : nouvelExemple[0][3][1]   -> ses 2 fruits/couleurs groupés
#
# Contenu d'une personne (les index repartent de 0 à chaque liste) :
#   [0] -> prénom
#   [1] -> âge
#   [2] -> booléen (True / False)
#   [3] -> sous-liste de couleurs

nouvelExemple = [
    # nouvelExemple[0] = Melvin
    # Index :  
    #   0       1    2      3
    ["Melvin", 25, True, ["Jaune", ["orange", "citron"], "rouge"]],
    #                       └ sous-liste [3] :
    #                         [3][0] = "Jaune"
    #                         [3][1] = ["orange", "citron"]
    #                         [3][2] = "rouge"

    # nouvelExemple[1] = Alicia
    # Index : 
    #    0      1    2       3
    ["Alicia", 30, False, ["Bleu", ["vert", "violet"], "noir"]]
    #                        └ sous-liste [3] :
    #                          [3][0] = "Bleu"
    #                          [3][1] = ["vert", "violet"]
    #                          [3][2] = "noir"
]

# ---------------------------------------------------------------------
# MELVIN : on commence par nouvelExemple[0]
# ---------------------------------------------------------------------
#   nouvelExemple[0]          -> ["Melvin", 25, True, [...]]   (toute la liste de Melvin)
#   nouvelExemple[0][0]       -> "Melvin"                       (prénom)
#   nouvelExemple[0][1]       -> 25                             (âge)
#   nouvelExemple[0][3]       -> ["Jaune", ["orange", "citron"], "rouge"]
#   nouvelExemple[0][3][1]    -> ["orange", "citron"]
#   nouvelExemple[0][3][1][0] -> "orange"
#   nouvelExemple[0][3][2]    -> "rouge"
print(f"{nouvelExemple[0][0]} a {nouvelExemple[0][1]} ans et il aime l'{nouvelExemple[0][3][1][0]} et sa couleur est le {nouvelExemple[0][3][2]}")
# Affiche : Melvin a 25 ans et il aime l'orange et sa couleur est le rouge

# ---------------------------------------------------------------------
# ALICIA : on commence par nouvelExemple[1]
# ---------------------------------------------------------------------
#   nouvelExemple[1]          -> ["Alicia", 30, False, [...]]   (toute la liste d'Alicia)
#   nouvelExemple[1][0]       -> "Alicia"                       (prénom)
#   nouvelExemple[1][1]       -> 30                             (âge)
#   nouvelExemple[1][3]       -> ["Bleu", ["vert", "violet"], "noir"]
#   nouvelExemple[1][3][1]    -> ["vert", "violet"]
#   nouvelExemple[1][3][1][0] -> "vert"
#   nouvelExemple[1][3][1][1] -> "violet"
#   nouvelExemple[1][3][2]    -> "noir"
print(f"{nouvelExemple[1][0]} a {nouvelExemple[1][1]} ans et elle aime les couleurs : {nouvelExemple[1][3][1][0]}, {nouvelExemple[1][3][1][1]}, {nouvelExemple[1][3][2]}")
# Affiche : Alicia a 30 ans et elle aime les couleurs : vert, violet, noir



#les methodes de liste:

#ajouter/ insère, retire, remplce des éléments
notes = [12.0, 15.5, 18.25]
print("Depart : ", notes)

#ajouter un élément a la fin de la liste : append()
notes.append(16.0)
print("Après append :", notes)

# retire et renvoie le dernier élément : pop ()
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

print(len(prenoms))#nombre d'élément dans une liste



#boucler sur les index (ou indices ou cleé "key")
for index in range(0, len(prenoms)):
 print({index})# 0 1 2 3 4 5
 print(f"{prenom[index]}")#affiche les prénoms correspondant aux index 0 1 2 3 4 5

# .join(liste) colle les éléments de la liste en une seule chaîne,
# avec " " (un espace) entre chaque élément.
