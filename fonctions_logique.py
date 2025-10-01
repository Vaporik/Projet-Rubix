## fonctions implémentant la logique du projet : ##
## génération du cube, mélange, application des mouvements, vérifications de victoire, etc. ##

from constantes import *

import random
import copy


# génère et retourne un rubik's cube résolu
# voir constantes.py pour la réprésentation
def generer_rubik_termine():

    # TODO

    cube = [[["NNN" for i in range(3)] for i in range(3)] for i in range(3)]
    for x in range(len(cube)):
        for y in range(len(cube[0])):
            for z in range(len(cube[0][0])):
                #                lettres = ["O", "G", "Y", "R", "B", "W"]
                #                chiffres_if = [0, 0, 0, 2, 2, 2]
                #                chiifres_liste = [2, 1, 0, 2, 1, 0]
                #                for i in range(6):
                #                    texte = list(cube[x][y][z])
                #                    texte[2] = "O"
                #                    cube[x][y][z] = "".join(texte)

                if x == 0:
                    texte = list(cube[x][y][z])
                    texte[2] = "O"
                    cube[x][y][z] = "".join(texte)
                if y == 0:
                    texte = list(cube[x][y][z])
                    texte[1] = "G"
                    cube[x][y][z] = "".join(texte)
                if z == 0:
                    texte = list(cube[x][y][z])
                    texte[0] = "Y"
                    cube[x][y][z] = "".join(texte)
                if x == 2:
                    texte = list(cube[x][y][z])
                    texte[2] = "R"
                    cube[x][y][z] = "".join(texte)
                if y == 2:
                    texte = list(cube[x][y][z])
                    texte[1] = "B"
                    cube[x][y][z] = "".join(texte)
                if z == 2:
                    texte = list(cube[x][y][z])
                    texte[0] = "W"
                    cube[x][y][z] = "".join(texte)

    return cube

# genere un rubik aleatoire
# nb_mouvs : nombre de mouvements aléatoires à apLeliquer
# retourne un tuple (rubik, scramble) (rubik : le cube généré, scramble : liste de tuples des mouvements effectués)


def generer_rubik(nb_mouvs):

    # TODO
    return

# genere un rubik mélangé grâce au scramble en paramètre
# scramble : une cdc des mouvements à effectuer (par exemple "B2 F2 F' L2 B")


def generer_rubik_scramble(scramble):

    # TODO
    return

# applique au rubik en paramètre nb_mouvs mouvements aléatoires
# retourne le scramble (liste de tuples des mouvements effectués)


def melanger(rubik, nb_mouvs):

    # TODO
    return


# retourne la couleur du cubelet correspondante à la face demandée
# exemple : ("YGO", "U") renvoie "Y"
def c(cubelet, f):

    # TODO
    return

# les fonctions suivantes permettent d'extraire une face du rubik en paramètre
# la face retournée, une matrice à deux dimensions, est ordonnée comme si le rubik avait été déplié
# f : lettre de la face à extraire, f = caractère (U,L,F,R,B,D)
# note : ces fonctions ne modifient PAS l'orientation (couleur) des cubelets


def extraire(rubik, f):

    # TODO
    return


# applique une rotation à la face passée en paramètre
# cette fonction ne modifie PAS l'orientation (couleur) des cubelets
# face : matrice 2D de cubelets
# sens : True pour horaire
# double : True pour 180°
def appliquer_rotation(face, sens, double):

    # TODO
    return

# reimplante (remplace) la face f de rubik avec les cubelets du paramètre face
# note : cette fonction n'applique PAS de rotation ou de réorientation des cubelets
# f : lettre de la face à remplacer, f = caractère (U,L,F,R,B,D)
# face : matrice 2D de cubelets


def reimplanter(rubik, f, face):

    # TODO
    return

# effectue un mouvement du rubik
# extrait, applique la rotation, réoriente les couleurs et réimplante la face
# mouv est un tuple (f, sens, double)
# f = caractère (U,L,F,R,B,D)
# sens = booleen (True = horaire)
# double = boolean (True = 180°)


def appliquer_mouvement(rubik, mouv):

    # TODO
    return

# renvoie True si la face est terminée
# face : matrice 2D de cubelets
# f : caractère (U,L,F,R,B,D)


def face_terminee(face, f):

    # TODO
    return False

# renvoie True si le cube est terminé


def victoire(rubik):

    # TODO
    return False

# renvoie un tuple (face, sens, double) correspondant au mouvement m
# m : chaîne de caractères représentant un mouvement
# exemples: "F" renvoie ('F',True,False), "R'" renvoie ('R',False,False), "L2" renvoie ('L',False,True)
# m DOIT être valide


def mouv(m):

    # TODO
    return

# renvoie une liste de tuples correspondants aux mouvements ms
# ms : chaîne de caractères représentant des mouvements (scramble)
# exemple: "F R' L2" renvoie [('F',True,False),('R',False,False),('L',False,True)]
# ms DOIT être valide


def mouvements(ms):

    # TODO
    return

# applique les mouvements ms au cube rubik
# ms : chaîne de caractères représentant des mouvements (scramble)


def m(rubik, ms):

    # TODO
    return

# renvoie une chaîne de caractères correspondant aux mouvements mouvs
# exemple: [('F',True,False),('R',False,False),('L',False,True)] renvoie "F R' L2"


def scramble(mouvs):

    # TODO
    return
