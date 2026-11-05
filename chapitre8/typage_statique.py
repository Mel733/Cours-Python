# #langue à typage dynamique
# age = "23"
# age = int(age)

# #annotation de type
# age2 : int | float = 23
# age2 = 19.5
# # age2 = "19.5"

# nom : str = "Mélo"
# notes : list[float] = [14.0, 19.2, 6.5]

# def calculer_moyenne(notes:list[float] ) -> float:
#     if not notes:
#         return 0.0
#     return sum(notes)/len(notes)
# print(calculer_moyenne(notes))

# #notes:list[float] ) décrit une liste de nombres
# #-> float, le résultat attendu
# #-> None, la fonction ne renvoie rien

# #dict[str, float] : Dictionnaire : nom et note {"Melvin", 12.0}
# #tuple [str, float] : paire: texte puis nombre("Melvin", 12.0)
# #float | None, Nombre ou abscence de valeur 14.0 ou None
# #-> None, fonction ne renvoie pas de valeur utilisé, def affiche()-> None :.....

# def premiere_notes(notes:list[float]) ->float | None : #la liste est une liste et les élément dedans sont en sorties des float ou none(pas de valeur)
#     if not notes:
#         return None
#     return notes[0]

# valeur = premiere_notes([])
# if valeur is None:
#     print("Aucune note")
# else:
#     print(f"Premiere note : {valeur:.1f}")


def total_notes(notes : list[float])-> float:
   if not notes:
       return 0.0
   return sum(notes)

def mention(moyenne : float) -> str:
    if moyenne >=10:
       return "Admis"
    return "Ajourné"

def trouver_eleve(notes:dict[str, float], nom : str) -> float|None:
   if nom in notes:
     return notes[nom]
   return None



# les assert c'est pour tester si on obtient bien les résultat voulus pour chaque scénario
assert total_notes([]) == 0.0  # test de la fonction avec liste vide, doit renvoyer 0.0
assert total_notes([12.7, 12.0]) == 24.7 #pareil mais doit renvoyer la somme exactes des notes dans la liste

assert mention(5) =="Ajourné" #test fonction méthode qui doit renvoyé "Ajourné"
assert mention(14) =="Admis" #pareil mais scénario différent
assert mention(10) == "Admis"


assert trouver_eleve({"Mélodie": 14}, "Mélodie") == 14 #teste fonction qui doit renvoyé la note paire avec le nom recherché dans le dictionnaire
assert trouver_eleve({"Mélodie": 14}, "Paul") == None #pareil mais scénario différent

print("C'est bon tout les testes passe") #s'affiche si tout les teste passe
