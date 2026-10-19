 #truthy & falsy
#falsy : false, none, 0, 0.0, ''
#truthy : tout ce qui n'est pas falsy (ex : true, 1, -1, 'texte', [1,2,3], "O")
print("boll(0);", bool(0)) #false
print("boll(0.0);", bool(0.0)) #false
print("boll('');", bool('')) #false
print("boll(\"\");", bool(" ")) #true
print("boll(\"0\");", bool("0")) #true
print("boll(1);", bool(1)) #true
#ne s'affiche pas

nom = input("Quel est votre nom ?")
if nom :
 print ("Bonjour ", nom)
else:
 print ("Vous n'avez pas saisi de nom")
