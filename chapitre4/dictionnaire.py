# DICTIONNAIRES : collection de paires clé -> valeur
# Clés : "prenom", "promo", "age"  |  Valeurs : "Sélomey", "B1DEV", 17

etudiant = {
    "prenom": "Sélomey",
    "promo": "B1DEV",
    "age": 17
}
print(etudiant) # {'prenom': 'Sélomey', 'promo': 'B1DEV', 'age': 17}

# --- Lire une valeur : dictionnaire[clé] ---
print(etudiant["prenom"])   # Sélomey
print(etudiant["age"])      # 17
print(etudiant["promo"])    # B1DEV
print(f"Dans la promo des {etudiant['promo']} il y a {etudiant['prenom']} et elle a {etudiant['age']} ans")

# --- Tester si une clé existe (renvoie True ou False) ---
print("prenom" in etudiant)   # True
print("nom" in etudiant)      # False

# --- get() : lire sans risque d'erreur ---
# etudiant["nom"] -> KeyError si la clé n'existe pas
# get() renvoie None, ou une valeur par défaut qu'on choisit
print(etudiant.get("prenom"))          # Sélomey
print(etudiant.get("nom", "Inconnu"))  # Inconnu (la clé "nom" n'existe pas)

# --- Ajouter une paire (clé qui n'existe pas encore) ---
etudiant["nom"] = "Dupont"
print(f"{etudiant['prenom']} {etudiant['nom']}")   # Sélomey Dupont

# --- Modifier une valeur (clé qui existe déjà) ---
etudiant["age"] = 18
print(f"Après modif, l'âge est de : {etudiant['age']}")  # 18

# --- Supprimer une paire ---
del etudiant["age"]
print(f"Après suppression, l'étudiant est : {etudiant}")
# {'prenom': 'Sélomey', 'promo': 'B1DEV', 'nom': 'Dupont'}

# --- Une valeur peut être une liste ---
etudiant["nom"] = ["Dupont", "Martin"]
print(etudiant["nom"][1])   # Martin (clé "nom", puis index 1 de la liste)

# --- Une valeur peut être un autre dictionnaire (imbriqué) ---
etudiant["prenom"] = {"prenom1": "Sélomey", "prenom2": "Timothé"}

# On descend niveau par niveau : d'abord la clé principale, puis la clé enfant
print(f"{etudiant['prenom']['prenom1']}, {etudiant['prenom']['prenom2']}")
# Sélomey, Timothé


#Exemple
# On demande à l'utilisateur de saisir une phrase,
# puis on la met en minuscules pour que "Chat" et "chat" soient comptés comme le même mot
phrase = input().lower()

# On crée un dictionnaire vide qui stockera : mot -> nombre d'apparitions
compteur = {}

# split() découpe la phrase en une liste de mots (séparés par les espaces)
# Ex : "le chat le chien" -> ["le", "chat", "le", "chien"]
for mot in phrase.split():
    # compteur.get(mot, 0) renvoie le nombre actuel du mot,
    # ou 0 si le mot n'est pas encore dans le dictionnaire
    # On ajoute 1 et on enregistre le résultat
    compteur[mot] = compteur.get(mot, 0) + 1

# On parcourt chaque paire (mot, nombre d'apparitions) du dictionnaire
for mot, nb in compteur.items():
    # Affiche par exemple : le : 2
    print(mot, ":", nb)

# len(compteur) donne le nombre de clés, donc le nombre de mots différents
print(f"Mots différents : {len(compteur)}")


# ============================================================
# LE .get() SUR UN DICTIONNAIRE
# ============================================================

# PROBLEME :
# Si on cherche une clé qui n'existe pas avec dico[clé],
# Python plante avec une KeyError.
#
#   stock = {"vis": 100}
#   print(stock["clous"])   -> KeyError : 'clous'
#
# SOLUTION : .get(clé, valeur_par_défaut)
# Il signifie : "donne-moi la valeur de cette clé,
# et si elle n'existe pas, donne-moi la valeur par défaut".
# Il ne plante jamais.
#
#   print(stock.get("clous", 0))   -> 0
#   print(stock.get("vis", 0))     -> 100

# A RETENIR :
# .get(clé, 0) = "la valeur de la clé, ou 0 si elle n'existe pas encore"
#0 est la valeur de défaut, elle s'affiche quand la clé existe pas. Dans ce cas le 0 est la quantité


# ------------------------------------------------------------
# UTILISATION 1 : AJOUTER (cumuler une quantité)
# ------------------------------------------------------------
# stock[produit] = stock.get(produit, 0) + quantite
#
# Lecture de droite à gauche :
#   1. stock.get(produit, 0) : valeur actuelle du produit,
#                              ou 0 si c'est la première fois
#   2. + quantite            : on ajoute la nouvelle quantité
#   3. stock[produit] = ...  : on range le résultat dans le dictionnaire
#
# Exemple :
#   1er ajout de vis (100) : 0 + 100 = 100
#   2e ajout de vis (15)   : 100 + 15 = 115
#
# Sans .get()  -> KeyError au premier ajout
# Avec "=" seul -> on écrase l'ancienne valeur au lieu de cumuler


# ------------------------------------------------------------
# UTILISATION 2 : VERIFIER UN RETRAIT
# ------------------------------------------------------------
# elif action == "retrait" and stock.get(produit, 0) >= quantite:
#
# Si le produit n'existe pas (ex : "marteau"), .get() renvoie 0.
# Comme 0 >= 1 est faux, le retrait est refusé sans plantage.


# ------------------------------------------------------------
# EXEMPLE COMPLET
# ------------------------------------------------------------
panier = {"pomme": 2}
panier["pomme"] = panier.get("pomme", 0) + 3   # 2 + 3 = 5
panier["poire"] = panier.get("poire", 0) + 4   # 0 + 4 = 4 (clé créée)
print(panier)   # {'pomme': 5, 'poire': 4}