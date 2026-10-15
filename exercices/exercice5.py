
nom_produit =input("Quel est le nom du produit ? ")
prix_produit_unitaire = float(input("Quel est le prix à l'unité de cet objet ? ").replace(",", "."))
quantite_article = int(input("Combien en voulez-vous ? "))
remise = float (input("Quelle est le taux de pourcentage de remise ? ").replace(".",","))
total_brut = prix_produit_unitaire * quantite_article
montant_remise = (total_brut * remise) / 100
total = total_brut - montant_remise

print("======Caisse======")
print(f"Produit. {nom_produit}")
print (f"Prix unitaire (en euros): {prix_produit_unitaire:.2f}")
print(f"Quantité : {quantite_article}")
print(f"Remise (en %):{remise:.2f}")
print("")

print(f"{"=" * 10}TICKET{"=" * 10}")
print(f"{"Produit}":<18}: {nom_produit:<16}")
print (f"{"Prix unitaire":<18}: {prix_produit_unitaire:<2.2f} €")
print(f"{"Quantité":<18}:  {quantite_article:<16}")
print(f" {"Total brut":<18} : {total_brut:<2.2f} €")
print(f"{"Remise":<18} : {remise:<2.2f} %")
print("-" * 26)
print (f"{"Prix unitaire":<18}: {prix_produit_unitaire:<2.2f} ")
print(f"A PAYER   {total:<2.2f} €")
print("=" * 26)
print("Merci de votre visite !\n\tA bientôt.")
