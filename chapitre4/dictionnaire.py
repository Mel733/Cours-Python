#dictionnaires : collection non ordonné de paires clé-valeurs
#prenom, promo , age sont des exemples de clé
#Selomey, B1DEV et 17 sont des exemples de valeurs

etudiant = {
    "prenom": "Sélomey",
    "promo" : "B1DEV",
    "age" : 17
}
print(etudiant)

print(etudiant["prenom"])
print(etudiant["age"])
print(etudiant["promo"])
print(f"Dans la promo des {etudiant["promo"]} il y a {etudiant["prenom"]} et elle a {etudiant["age"]} ans")

#tester la présence d'une clé:

print("prenom" in etudiant) #true
print("nom" in etudiant) #false

#get : permet de récuperer la valeur aassocier a une clé, avec une valeur par défaut si la clé n'existe pas
print(etudiant.get("prenom")) #affiche "Sélomey"
print(etudiant.get("nom", "Inconnu")) # affiche "Inconnu" car la clé nom n'existe pas 

#ajouter une nouvelle paire clé-valeur
etudiant ["nom"] = "Dupont"
print(f"{etudiant['prenom']} {etudiant['nom']}")

#modification d'une valeur d'une paire clé-valeur
etudiant["age"] = 18
print(f"Apres modif, l'age est de : {etudiant["age"]}")

#supression :
del etudiant["age"]
print(f"A pres supression, l'édutiant est : {etudiant}")

#ajout d'une valeur dans la clé nom
etudiant ["nom"] = ["Dupont", "Martin"]

etudiant["prenom"] = {"prenom1": "Sélomey", "prenom2": "Timothé"} #céer deux clé dans la clé prenom

print(f"{etudiant["prenom"]["prenom1"]}, {etudiant["prenom"]["prenom2"]}") #aller d'abord dans la clé principale, ensuite la clé enfant pour afficher la valeur correspondant