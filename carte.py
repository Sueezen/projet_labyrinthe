# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """

    # On va utiliser la structure de donnée du dictionnaire, cela nous permettra de retrouver les informations
    # des directions plus facilement
    carte={}
    carte["Nord"]=nord
    carte["Est"]=est
    carte["Sud"]=sud
    carte["Ouest"]=ouest
    carte["Tresor"]=tresor
    carte["Pions"]=pions
    return carte

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    res=False
    cpt=0 # Compteur permettant de calculer le nombre de mur présent sur la carte
    for (direction, valeur) in c.items():
        if direction == "Nord" or direction == "Est" or direction == "Sud" or direction == "Ouest":
            if valeur == True:
                cpt+=1
    if cpt==2 or cpt==0 or cpt==1: # On cherche à savoir si le compteur est à 0, 1 ou 2 murs.
        res=True
    return res

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    res=False
    if c["Nord"]==True:
        res=True
    return res

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    res=False
    if c["Sud"]==True:
        res=True
    return res

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    res=False
    if c["Est"]==True:
        res=True
    return res

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    res=False
    if c["Ouest"]==True:
        res=True
    return res

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["Pions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["Pions"]=listePions
    return c

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    res=0
    for (cle, valeur) in c.items():
        if cle == "Pions":
            res= len(valeur) # On vient simplement chercher la longueur de notre liste de pions
    return res

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    res=False
    for (cle, valeur) in c.items():
        if cle=="Pions" and pion in valeur:
            res=True
    return res


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["Tresor"]

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["Tresor"]
    c["Tresor"]=0
    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c["Tresor"]
    c["Tresor"]=tresor
    return res


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for (cle, valeur) in c.items():
        if cle == "Pions" and pion in valeur:
            valeur.remove(pion) # On vient simplement retirer l'élément Pion dans la liste des pions

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for (cle, valeur) in c.items():
        if cle == "Pions" and pion not in valeur:
            valeur.append(pion)

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    valeur_direction=[c["Nord"], c["Est"], c["Sud"], c["Ouest"]]
    if valeur_direction == [True, False, False, False]: # Compare la carte: ╦
        # Donne le symbole suivant : ╣
        c["Nord"]= False
        c["Est"]= True
    elif valeur_direction == [False, True, False, False]: # Compare la carte: ╣   
        # Donne le symbole suivant : ╩
        c["Est"]= False
        c["Sud"]= True
    elif valeur_direction == [False, False, True, False]: # Compare la carte: ╩
        # Donne le symbole suivant : ╠
        c["Sud"]= False
        c["Ouest"]= True
    elif valeur_direction == [False, False, False, True]: # Compare la carte: ╠
        # Donne le symbole suivant : ╦
        c["Nord"]= True
        c["Ouest"]= False
    elif valeur_direction == [True, True, False, False]: # Compare la carte: ╗
        # Donne le symbole suivant : ╝
        c["Nord"]= False
        c["Est"]= True
        c["Sud"]= True
    elif valeur_direction == [False, False, True, True]: # Compare la carte: ╚
        # Donne le symbole suivant : ╔
        c["Nord"]= True
        c["Sud"]= False
        c["Ouest"]= True
    elif valeur_direction == [True, False, False, True]: # Compare la carte: ╔
        # Donne le symbole suivant : ╗
        c["Nord"]= True
        c["Est"]= True
        c["Ouest"]= False
    elif valeur_direction == [False, True, True, False]: # Compare la carte: ╝
        # Donne le symbole suivant : ╚
        c["Est"]= False
        c["Sud"]= True
        c["Ouest"]= True
    elif valeur_direction == [True, False, True, False]: # Compare la carte: ═
        # Donne le symbole suivant : ║
        c["Nord"]= False
        c["Est"]= True
        c["Sud"]= False
        c["Ouest"]= True
    elif valeur_direction == [False, True, False, True]: # Compare la carte: ═
        # Donne le symbole suivant : ║
        c["Nord"]= True
        c["Est"]= False
        c["Sud"]= True
        c["Ouest"]= False
    elif valeur_direction == [False, False, False, False]: # Compare la carte: ╬
        # Donne le symbole suivant : ╬
        c["Nord"]= False
        c["Est"]= False
        c["Sud"]= False
        c["Ouest"]= False

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    valeur_direction=[c["Nord"], c["Est"], c["Sud"], c["Ouest"]]
    if valeur_direction == [True, False, False, False]: # Compare la carte: ╦
        # Donne le symbole suivant : ╠
        c["Nord"]= False
        c["Ouest"]= True
    elif valeur_direction == [False, True, False, False]: # Compare la carte: ╣   
        # Donne le symbole suivant : ╦
        c["Nord"]= True
        c["Est"]= False
    elif valeur_direction == [False, False, True, False]: # Compare la carte: ╩
        # Donne le symbole suivant : ╣
        c["Est"]= True
        c["Sud"]= False
    elif valeur_direction == [False, False, False, True]: # Compare la carte: ╠
        # Donne le symbole suivant : ╩
        c["Sud"]= True
        c["Ouest"]= False
    elif valeur_direction == [True, True, False, False]: # Compare la carte: ╗
        # Donne le symbole suivant : ╔
        c["Est"]= False
        c["Ouest"]= True
    elif valeur_direction == [False, False, True, True]: # Compare la carte: ╚
        # Donne le symbole suivant : ╝
        c["Est"]= True
        c["Ouest"]= False
    elif valeur_direction == [True, False, False, True]: # Compare la carte: ╔
        # Donne le symbole suivant : ╚
        c["Nord"]= False
        c["Sud"]= True
    elif valeur_direction == [False, True, True, False]: # Compare la carte: ╝
        # Donne le symbole suivant : ╗
        c["Nord"]= True
        c["Sud"]= False
    elif valeur_direction == [True, False, True, False]: # Compare la carte: ═
        # Donne le symbole suivant : ║
        c["Nord"]= False
        c["Est"]= True
        c["Sud"]= False
        c["Ouest"]= True
    elif valeur_direction == [False, True, False, True]: # Compare la carte: ═
        # Donne le symbole suivant : ║
        c["Nord"]= True
        c["Est"]= False
        c["Sud"]= True
        c["Ouest"]= False
    elif valeur_direction == [False, False, False, False]: # Compare la carte: ╬
        # Donne le symbole suivant : ╬
        c["Nord"]= False
        c["Est"]= False
        c["Sud"]= False
        c["Ouest"]= False

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    for i in range(0, randint(0, 4)): # On remarque qu'on fait tourner au maximum 4 fois, car il y a 4 directions
        tournerHoraire(c)

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """

    # Nord = 1, Est = 2, Sud = 4 , Ouest = 8
    res=0
    if murOuest(c):
        res+=8
    if murSud(c):
        res+=4
    if murEst(c):
        res+=2
    if murNord(c):
        res+=1
    return res
    
    

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """

    liste=[]
    if code-8>=0:
        code-=8
        liste.append(True)
    else:
        liste.append(False)
    if code-4>=0:
        code-=4
        liste.append(True)
    else:
        liste.append(False)
    if code-2>=0:
        code-=2
        liste.append(True)
    else:
        liste.append(False)
    if code-1>=0:
        code-=1
        liste.append(True)
    else:
        liste.append(False)

    c["Nord"]=liste[3]
    c["Est"]=liste[2]
    c["Sud"]=liste[1]
    c["Ouest"]=liste[0]

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    liste_compare=[]
    res=""
    for (cle, valeur) in c.items():
        if cle == "Nord" or cle == "Sud" or cle == "Ouest" or cle == "Est":
            liste_compare.append(valeur)
    if liste_compare == [False, False, False, False]:
        res="╬"
    elif liste_compare == [True, False, False, False]:
        res="╦"
    elif liste_compare == [False, True, False, False]:
        res="╣"
    elif liste_compare == [True, True, False, False]:
        res="╗"
    elif liste_compare == [False, False, True, False]:
        res="╩"
    elif liste_compare == [True, False, True, False]:
        res="═"
    elif liste_compare == [False, True, True, False]:
        res="╝"
    elif liste_compare == [False, False, False, True]:
        res="╠"
    elif liste_compare == [True, False, False, True]:
        res="╔"
    elif liste_compare == [False, True, False, True]:
        res="║"
    elif liste_compare == [False, False, True, True]:
        res="╚"
    elif liste_compare == [True, True, False, True]:
        res="Ø"
    elif liste_compare == [True, True, True, False]:
        res="Ø"
    elif liste_compare == [True, False, True, True]:
        res="Ø"
    elif liste_compare == [False, True, True, True]:
        res="Ø"
    elif liste_compare == [True, True, True, True]:
        res="Ø"
    return res

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte1["Nord"]==False and carte2["Sud"]==False: # On cherche à savoir si il y a pas de mur
    # au nord de la carte 1 et qu'il n'y a pas de mur au Sud de la carte 2.
        res=True
    return res

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte2["Nord"]==False and carte1["Sud"]==False: # On cherche à savoir si il y a pas de mur
    # au nord de la carte 2 et qu'il n'y a pas de mur au Sud de la carte 1.
        res=True
    return res

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte2["Est"]==False and carte1["Ouest"]==False: # On cherche à savoir si il y a pas de mur
    # à l'Est de la carte 2 et qu'il n'y a pas de mur à l'Ouest de la carte 1.
        res=True
    return res

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    res=False
    if carte2["Ouest"]==False and carte1["Est"]==False: # On cherche à savoir si il y a pas de mur
    # à l'Est de la carte 1 et qu'il n'y a pas de mur à l'Ouest de la carte 2.
        res=True
    return res
