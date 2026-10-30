# ------------------------------------------------------------
# PARTIE 1 : LECTURE DES DONNEES
# ------------------------------------------------------------

# On lit combien de lignes on va recevoir (ex : 5)
nombre = int(input())

# Dictionnaire vide : groupe -> liste des élèves
# Exemple final : {"A": ["Tom", "Hugo", "Nora"], "B": ["Lina", "Sami"]}
groupes = {}

# Cette boucle se répète "nombre" fois, une fois par ligne lue.
# Tout ce qui est indenté en dessous est répété à chaque tour.
for _ in range(nombre):

    # On lit une ligne comme "Tom A" et on la coupe en deux :
    # eleve = "Tom", groupe = "A"
    eleve, groupe = input().split()

    # Si le groupe n'existe pas encore, on le crée avec une liste vide.
    # S'il existe déjà, setdefault ne fait rien.
    groupes.setdefault(groupe, [])

    # On ajoute l'élève à la liste de son groupe
    groupes[groupe].append(eleve)


# ------------------------------------------------------------
# PARTIE 2 : AFFICHAGE DE CHAQUE GROUPE
# (au niveau du for = après avoir tout lu)
# ------------------------------------------------------------

# On parcourt les groupes dans l'ordre alphabétique (A, puis B, ...)
for groupe in sorted(groupes):

    # On trie les noms des membres de ce groupe par ordre alphabétique.
    # (la variable s'appelle "eleve" mais elle contient une LISTE d'élèves)
    eleve = sorted(groupes[groupe])

    # On affiche : Groupe A (3) : Hugo, Nora, Tom
    #   {groupe}            -> le nom du groupe
    #   {len(...)}          -> le nombre de membres
    #   ', '.join(eleve)    -> colle les noms avec ", " entre chacun
    print(f"Groupe {groupe} ({len(groupes[groupe])}) : {', '.join(eleve)}")


# ------------------------------------------------------------
# PARTIE 3 : LE GROUPE LE PLUS NOMBREUX
# (une seule fois, donc en dehors de la boucle)
# ------------------------------------------------------------

# max(...) cherche le meilleur groupe parmi sorted(groupes).
# key=lambda groupe: len(groupes[groupe]) veut dire :
# "pour comparer deux groupes, regarde leur nombre de membres".
# En cas d'égalité, max garde le PREMIER rencontré, donc le premier
# par ordre alphabétique (car on parcourt sorted(groupes)).
print(f"Groupe le plus nombreux : {max(sorted(groupes), key=lambda groupe: len(groupes[groupe]))}")