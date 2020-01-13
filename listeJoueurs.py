# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. [(nom,tresors,num),(nom,tresors,num)]
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    res=[]
    i=1
    jc=0
    for nom in nomsJoueurs:
        res.append((nom,[],i,jc))
        i+=1
    return res

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append(Joueur(joueur))

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    jc=randint(0,len(joueurs))
    j1=(joueurs[0][0],joueurs[0][1],joueurs[0][2],jc)
    if len(joueurs)>=2:
        j2=(joueurs[1][0],joueurs[1][1],joueurs[1][2],jc)
    if len(joueurs)>=3:
        j3=(joueurs[2][0],joueurs[2][1],joueurs[2][2],jc)
    if len(joueurs)>=4:
        j4=(joueurs[3][0],joueurs[3][1],joueurs[3][2],jc)
    joueurs=[]
    joueurs.append(j1)
    if len(joueurs)>=2:
        joueurs.append(j2)
    if len(joueurs)>=3:
        joueurs.append(j3)
    if len(joueurs)>=4:
        joueurs.append(j4)        
    
    

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresor=[]
    for i in range(1,nbTresors+1):
        tresor.append(i)
    if nbTresorMax==0:
        x=nbTresors//len(joueurs)
        for nb in range(len(joueurs)):
            for i in range(x):
                random.shuffle(tresor)
                joueurs[nb][1].append(tresor[0])
                tresor.pop(0)
    else:
        for nb in range(len(joueurs)):
            for i in range(nbTresorMax):
                random.shuffle(tresor)
                joueurs[nb][1].append(tresor[0])
                if len(tresor)!=0:
                    tresor.pop(0)
            
def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    print(joueurs)
    jc=joueurs[0][3]
    jc+=1
    if jc ==4:
        jc=0
    j1=(joueurs[0][0],joueurs[0][1],joueurs[0][2],jc)
    if len(joueurs)>=2:
        j2=(joueurs[1][0],joueurs[1][1],joueurs[1][2],jc)
    if len(joueurs)>=3:
        j3=(joueurs[2][0],joueurs[2][1],joueurs[2][2],jc)
    if len(joueurs)>=4:
        j4=(joueurs[3][0],joueurs[3][1],joueurs[3][2],jc)
    joueurs=[]
    joueurs.append(j1)
    if len(joueurs)>=2:
        joueurs.append(j2)
    if len(joueurs)>=3:
        joueurs.append(j3)
    if len(joueurs)>=4:
        joueurs.append(j4)      
    print(joueurs)

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs[0]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if len(joueurs[0][1])!=0:
        joueurs[0][1].pop(0)
    

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    res=None
    i=0
    while i<len(joueurs) and res==None:
        if joueurs[i][2]==numJoueur:
            res=len(joueurs[i][1])
        i+=1
    return res

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[0][2]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return joueurs[0][0]

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    res=None
    i=0
    while i<len(joueurs) and res==None:
        if joueurs[i][2]==numJoueur:
            res=joueur[i][0]
        i+=1
    return res    

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    res=None
    i=0
    while i<len(joueurs) and res==None:
        if joueurs[i][2]==numJoueur:
            res=joueur[i][1][0]
        i+=1
    return res

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return joueurs[0][1][0]

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    return len(joueurs[0][1])==0
