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