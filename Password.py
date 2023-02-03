import hashlib #On importe le module de cryptage
import re      #On importe le module re qui permet de spécifier un ensemble souhaité de chaînes de caractères, dans une chaine de caractères

speciaux = ["!", "@", "#", "$", "%", "^", "&", "*"] #On définis la variable de caractères spéciaux

print("Bonjour, pour un mdp valide, il te faut au moins:")
print("● 8 caractères.")
print("● une lettre majuscule.")
print("● une lettre minuscule.")
print("● un chiffre.")
print("● un caractère spécial (!, @, #, $, %, ^, &, *)")
print()

while True: 
    c = input("MOT DE PASSE : ")
    if len(c) <=8:
        print("INVALIDE : 8 caractères au minimum svp")
    elif c == c.upper():                                    #Si le mdp est seulement en majuscule ...
        print("INVALIDE : Une lettre miniscule au minimun svp") #... le mdp ne sera pas valide.
    elif c== c.lower():                                     #De même, si le mdp est seulement en miniscule ...
        print("INVALIDE : Une lettre majuscule au minimun svp") #... le mdp ne sera pas valide
    elif not re.search("[0-9]", c):                         #On recherche si dans le mdp il y un chiffre entre 0-9.
        print("INVALIDE : Un chiffre au minimum svp")           #Si il n'y a pas, le mdp ne sera pas valide
    elif not any(char in speciaux for char in c):           #On recherche si un élément de la liste spéciaux se trouve dans le mdp.
        print("INVALIDE : Un caractère special au minimum svp") #Si il n'y en a aucun, le mdp ne sera pas valide
    else : 
        print("Mot de passe valide") #Sinon le mot de passe est valide
        break                        #Fin de la boucle


#Encryptage du mot de passe grâce au module hashlib
y=hashlib.sha256(c.encode('utf-8')).hexdigest()
print("Voici votre mot de passe crypté : ", y)