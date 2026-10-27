#if/elif/else
#structure conditionnel
#indentation = 4 espaces(recomammdation PEP 8 => style officiel python)
#if = si
#else = autre
#elif = sinon si
# if .... = predicat apres le if : Ce que la condition va verifier
# if  : chaque if est vérifié INDÉPENDAMMENT. Si plusieurs conditions sont vraies,
#       plusieurs messages s'affichent.
# elif : n'est vérifié QUE si les conditions précédentes sont fausses. Dès qu'une
#        condition est vraie, Python s'arrête et ignore les elif/else suivants,
#        donc un seul message s'affiche.
note = float(input("Quelle est ta note ?").replace(",","."))
if note >= 10 :
    print("Bravo vous avez la moyenne")
    print("Continue comme ca")
elif note >= 8:
    print("vous etes proche de la moyenne")
    print("Il faut faire un petit effort supplementaire")
else:
    print ("Vous n'avez pas la moyenne")
    print("Il faut traviller d'avantage")


print("fin du programme ")

#condition imbriquées
#v1 :
if note>= 14:
    print("Imbrication :bon résultat")
else :
    if note >= 10:
       print("imbrication: résultat correct")
    else:
       print("Imbrication : résultat isuffisant")

#v2 : meme logique avec elif
if note >=14 :
    print ("Avec elif : bon résultat")
elif note >= 10:
    print ("Avec elif : resultat correct")
else:
    print("Avec elif : résuktat insuffisant")
