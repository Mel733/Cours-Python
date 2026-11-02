with open("journal.txt", "w", encoding="utf-8") as journal:
    journal.write("Ligne 1 : Démarrage du journal\n")

nombre = int(input())
with open("journal.txt", "a", encoding ="utf-8")as journal:
  for i in range(2, nombre + 2):
      evenement = input()
      journal.write(f"Ligne {i} : {evenement}\n")  

print(f"Lignes dans le journal : {nombre+1}")
mot_cle = input().lower()

trouve = False
with open("journal.txt", "r", encoding = "utf-8")as journal:
    for ligne in journal.read().splitlines():
        if mot_cle in ligne.lower() :
            print(ligne)
            trouve =True
if not trouve:
    print("Aucune ligne trouvée")
