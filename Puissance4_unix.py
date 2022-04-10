###########################
# DEFINITON DES FONCTIONS #
###########################

#définition de la fonction win
def win(joueur):
    """cette fonction permet de savoir si le joueur venant de mettre un jeton a gagné ou s'il vient de remplir entierement la grille"""
    """l=ligne (verticale) et c=colonne (horizontale)"""
    #test sur horizontale
    jetons_alignés=0
    for l in range (6):
        jetons_alignés=0
        for c in range (7):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0

    #test sur verticale
    for c in range (7):
        jetons_alignés=0
        for l in range (6):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0

    #test sur diagonale↘ partie gauche
    for l in range (6):
        jetons_alignés=0
        c=0
        while (l<=5) and (c<=6):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0
            l=l+1
            c=c+1

    #test sur diagonale↘ partie droite
    for c in range (7):
        jetons_alignés=0
        l=0
        while (l<=5) and (c<=6):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0
            l=l+1
            c=c+1

    #test sur diagonale↙ partie gauche
    for l in range (6):
        jetons_alignés=0
        c=0
        while (l>=0) and (c<=6):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0
            l=l-1
            c=c+1


    #test sur diagonale↙ partie droite
    for c in range (7):
        jetons_alignés=0
        l=5
        while (c<=6) and (l>=0):
            if état_grille[l][c] == joueur:
                jetons_alignés=jetons_alignés+1
                if jetons_alignés == 1:
                    P1=(c,l)
                elif jetons_alignés == 4:
                    P2=(c,l)
                    return 1,P1,P2
            else:
                jetons_alignés=0
            c=c+1
            l=l-1


    #test pour savoir s'il y a égalité (toute la grille est remplie)
    égalité=1
    for c in range (6):
        for l in range (7):             #on afiche les trous vides ou remplis
            if état_grille[c][l]==0:
                égalité=0

    #savoir si il y a égalité iu rien
    if égalité==1:
        return 2
    else:
        return 0

#définir waitclic()
def waitclic():
    """ attend que l'utilisateur clique , et renvoie les coordonnées du point cliqué. ferme le programme si clic sur croix"""
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type== MOUSEBUTTONDOWN :
                return event.pos

#définition de la fonction soon qui permet d'arreter ou de remetrre le son et de changer le bouton en conséquence
def soon():
    global musique
    if musique==1:
        pygame.mixer.pause()
        rectangle_plein((581,24),50,38,couleur2)
        window.blit(no_son,(556,10))
        pygame.display.flip()
        musique=0
    else:
        pygame.mixer.unpause()
        rectangle_plein((581,24),50,38,couleur2)
        window.blit(son,(556,10))
        pygame.display.flip()
        musique=1

#définition de la fonction qui affiche le bouton son ou no_son par rapport à l'ancien
def bouton():
    if musique==1:
        window.blit(son,(556,10))
    else:
        window.blit(no_son,(556,10))

#definition de la fonction rond plein
def rond_plein(centre,rayon,couleur):
    while rayon!=0:
        pygame.draw.circle(screen,couleur,centre,rayon,2)
        rayon=rayon-1


#définition de la fonction rectangle plein
def rectangle_plein(centre,horizontale,verticale,couleur):
    """rectangle plein(centre du rectangle,longueur segment horizontaux,longueur segments verticaux,couleur, )"""
    while (horizontale!=-1) and (verticale!=-1):
        x1,y1=centre[0]-horizontale//2,centre[1]-verticale//2
        x2,y2=centre[0]+horizontale//2,centre[1]-verticale//2
        x3,y3=centre[0]+horizontale//2,centre[1]+verticale//2
        x4,y4=centre[0]-horizontale//2,centre[1]+verticale//2
        pygame.draw.line(screen,couleur,(x1,y1),(x2,y2),1)
        pygame.draw.line(screen,couleur,(x2,y2),(x3,y3),1)
        pygame.draw.line(screen,couleur,(x3,y3),(x4,y4),1)
        pygame.draw.line(screen,couleur,(x4,y4),(x1,y1),1)
        if horizontale!=-1:
            horizontale=horizontale-1
        if verticale!=-1:
            verticale=verticale-1

#définition de la fonction grille
def grille():
    débutX,débutY=distance//2+rayon,espace+distance//2+rayon
    débutX_ = débutX
    rectangle_plein(centre_rectangle,horizontale,verticale,couleur)#fond de la grille
    for l in range (6):
        for c in range (7):             #on afiche les trous vides ou remplis
            if état_grille[l][c]==1:
                rond_plein((débutX,débutY),rayon,j1)
            elif état_grille[l][c]==-1:
                rond_plein((débutX,débutY),rayon,j2)
            else:
                rond_plein((débutX,débutY),rayon,couleur2)
            débutX=débutX+rayon*2+distance
        débutX=débutX_
        débutY=débutY+rayon*2+distance

#définition de la fonction affichage_joueur
def affichage_joueur(j):
    rond_plein((320,40),30,j)
    window.blit(joue,(0,0))
    pygame.display.flip()

#définition de la fonction choix de la colonne
def choix_colonne(rayon,distance,Xwaitclic):
    colonne=Xwaitclic//(rayon*2+distance)
    return colonne

#définition de la fonction choix de la ligne
def choix_ligne(joueur,colonne):
    ligne=0
    if état_grille[ligne][colonne] == 0:
        ligne=5
        while état_grille[ligne][colonne] != 0:
            ligne=ligne-1
        return ligne
    else:
        return 606

#définition de la fonction ajout d'un jeton dans la grille(a la fois dans le tableau et dans la fenetre graphique
def ajout_jeton(colonne,ligne,joueur):
    #ajout dans la fenetre graphique
    colonne_=int((colonne)*(rayon*2+distance)+rayon+distance//2)
    ligne_=int((ligne)*(rayon*2+distance)+espace+rayon+distance//2)
    ligne_provisoire=-rayon
    if joueur==1:
        jeton=j1
    else:
        jeton=j2
    while ligne_provisoire < ligne_:
        screen.fill(couleur2)
        grille()
        rond_plein((colonne_,ligne_provisoire),rayon,jeton)
        pygame.display.flip()
        ligne_provisoire=ligne_provisoire+15
    grille()
    bouton()
    rond_plein((colonne_,ligne_),rayon,jeton)
    pygame.display.flip()
    #ajout dans le tableau
    état_grille[ligne][colonne]=joueur

#définition de la fonction trace_puissance4 qui met en évidence le puissance 4
def Trace_puissance4(colonne,ligne,P1,P2):
    vert=(0,170,15)
    #conversion des données en coordonnéees
    colonne_1,ligne_1=P1
    colonne_1=int((colonne_1)*(rayon*2+distance)+rayon+distance//2)
    ligne_1=int((ligne_1)*(rayon*2+distance)+espace+rayon+distance//2)
    colonne_2,ligne_2=P2
    colonne_2=int((colonne_2)*(rayon*2+distance)+rayon+distance//2)
    ligne_2=int((ligne_2)*(rayon*2+distance)+espace+rayon+distance//2)
    #trace le puissance 4
    pygame.draw.line(screen,vert,(colonne_1,ligne_1),(colonne_2,ligne_2),9)
    pygame.display.flip()

#informations utilisés durant toute la partie(création de la grille,création de la fenetre,affichage jeton...)

espace=80
rayon=40
distance=8
horizontale=7*distance+14*rayon
verticale=7*distance+12*rayon
taille_fenetre=(horizontale,verticale+espace)
centre_rectangle=(taille_fenetre[0]//2,taille_fenetre[1]-verticale//2)
couleur=(16,40,100) #bleu
couleur2=(0,0,0)    #noir
j1=(255,0,0)        #rouge
j2=(255,255,0)      #jaune

#définition de la fonction jeu
def partie():
    screen.fill(couleur2)
    grille()
    bouton()
    pygame.display.flip()
    joueur=-1
    gagné=0
    while gagné==0:
        joueur=joueur*-1
        if joueur == 1:
            affichage_joueur(j1)
        else:
            affichage_joueur(j2)
        Xwaitclic,Ywaitclic=waitclic()
        if (556<Xwaitclic<606) and (10<Ywaitclic<48):
            soon()
        colonne=choix_colonne(rayon,distance,Xwaitclic)
        ligne=choix_ligne(joueur,colonne)
        while (espace>Ywaitclic) or (ligne == 606):
            Xwaitclic,Ywaitclic=waitclic()
            if (556<Xwaitclic<606) and (10<Ywaitclic<48):
                soon()
                continue
            colonne=choix_colonne(rayon,distance,Xwaitclic)
            ligne=choix_ligne(joueur,colonne)
        ajout_jeton(colonne,ligne,joueur)
        gagné=win(joueur)
    if gagné!=2:
        Trace_puissance4(colonne,ligne,gagné[1],gagné[2])
        window.blit(gagne,(0,0))
    else:
        window.blit(egalite,(0,0))
    pygame.display.flip()

#INITIALISATION
import pygame
from pygame.locals import *
pygame.init() # initialisation de pygame
#construit la fenetre
window= pygame.display.set_mode(taille_fenetre)
screen = pygame.display.get_surface()

#chargement de la musique
minuit = pygame.mixer.Sound("midnight.wav")
musique=1

#chargement des images
menu = pygame.image.load("pictures\menu.png").convert()
regle = pygame.image.load("pictures\regle.png").convert()
credits = pygame.image.load("pictures\credits.png").convert()
joue = pygame.image.load("pictures\joue.png").convert_alpha()
gagne = pygame.image.load("pictures\gagne.png").convert_alpha()
egalite = pygame.image.load("pictures\egalite.png").convert_alpha()
son = pygame.image.load("pictures\son.png").convert_alpha()
no_son = pygame.image.load("pictures\no_son.png").convert_alpha()
#lancement de la musique
minuit.play(loops=-1, maxtime=0, fade_ms=0)

bon=0
while bon<1:
    window.blit(menu,(0,0))
    bouton()
    pygame.display.flip()
    jeu=0
    règle=0
    crédits=0
    quitter=0
    action=0
    while action!=1:
        Xclick,Yclick=waitclic()
        if (45<Xclick<571) and (150<Yclick<230):
            jeu=1
            action=1
        elif (45<Xclick<571) and (265<Yclick<345):
            règle=1
            action=1
        elif (45<Xclick<571) and (390<Yclick<470):
            crédits=1
            action=1
        if (45<Xclick<571) and (505<Yclick<585):
            quitter=1
            action=1
        elif (556<Xclick<606) and (10<Yclick<48):
            soon()
    if jeu==1:
        #définition des jetons dans la grille
        état_grille=[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        partie()
    elif règle==1:
        window.blit(regle,(0,0))
        bouton()
        pygame.display.flip()
    elif crédits==1:
        window.blit(credits,(0,0))
        bouton()
        pygame.display.flip()
    else:
        pygame.quit()
        break
    retour_menu=0
    while retour_menu!=1:
        Xclick,Yclick=waitclic()
        if (330<Xclick<600) and (550<Yclick<610):
            retour_menu=1
        elif (556<Xclick<606) and (10<Yclick<48):
            soon()
