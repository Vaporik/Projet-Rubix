## fonctions pour l'interface utilisateur en console ##


from constantes import *
from fonctions_logique import *

# affiche un rubik en console
# le rubik est affiché en mode "déplié"
# exemple :
    # ~ WWW
    # ~ WWW
    # ~ YYY
     # ~ U

# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
 # ~ L   F   R     B

    # ~ WWW
    # ~ YYY
    # ~ YYY
     # ~ D
def afficher_rubik(rubik):

	# TODO
	return
	

# retourne True si le saisie est un mouvement valide
# les mouvements valides sont une chaine de caractères sous la forme (F|L|R|U|D|B['|2])
def saisie_valide(saisie):
		
	# TODO
	return True
	
# permet la saisie d'un mouvement à effectuer
# sous la forme (F|L|R|U|D|B['|2])
# lettre = face
# ' = anti-horaire
# 2 = 180°				
# renvoie toujours un tuple valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvement():
	
	# TODO
	return

# permet la saisie d'une suite de mouvements à effectuer		
# renvoie toujours une liste de tuples valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvements():
	
	# TODO
	return
	
	
