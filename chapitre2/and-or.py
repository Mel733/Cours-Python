#and or
          #a and b : si a est faux le resultat est faux sans evalier b
          # a or b : si a est vrai le résultat est vrai sans évaluer b
          
nombre_de_notes = 0
somme_notes = 0.0
if nombre_de_notes > 0 and somme_notes / nombre_de_notes >= 10:
 print("Moyenne suffisante")
else:
 print("Moyenne insuffisante")

est_deleguer = True
if est_deleguer or somme_notes/nombre_de_notes >=16 :
 print("invité au conseil de classe")

#if somme_notes/nombre_de_notes >= 10 and nombre_de_notes > 0 :
#print("Moyenne suffisante et des notes présente")
#ne marche pas car 0 diviser par 0