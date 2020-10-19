#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      manu
#
# Created:     23/05/2012
# Copyright:   (c) manu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import*
from tkinter import tix
from tkinter.constants import *
import sqlite3
from random import*


class ptifenetre:
    def __init__(self,parent):
        self.fen2=parent
        emplacementX=(self.fen2.winfo_screenwidth()-500)//2
        emplacementY=(self.fen2.winfo_screenheight()-400)//2
        self.fen2.geometry("%dx%d%+d%+d" % (500,400,emplacementX,emplacementY))
        self.fen2.resizable(width=False,height=False)
        self.fen2.title('Culture Quest')
        self.fen2.attributes('-topmost', 1)
        self.fond=Canvas(self.fen2,height=400,width=500,bg="black")
        self.fond.place(x=0,y=0)


        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()



class fenetre:

    """creation d'un moule pour toute mes fenetre"""

    def __init__(self,parent):
        self.fen = parent
        emplacementX=(self.fen.winfo_screenwidth()-1024)//2
        emplacementY=(self.fen.winfo_screenheight()-640)//2
        self.fen.geometry("%dx%d%+d%+d"% (1024,640,emplacementX,emplacementY))
        self.fen.resizable(width=False,height=False)
        self.fen.title('Culture Quest')
        fenetre.ouvertBD(self)
        #################creation du menu ########################
        self.menu1=Menu(self.fen)
        self.fichier=Menu(self.fen,tearoff=0)
        self.aide=Menu(self.fen,tearoff=0)
        self.statistique=Menu(self.fen,tearoff=0)
        self.menu1.add_cascade(label="Fichier",menu=self.fichier)
        self.fichier.add_command(label="Quitter",command=self.fen.destroy)
        self.fichier.add_command(label="Nouvelle Partie",command=lambda:fenetre.NEW_PARTY(self))
        self.fichier.add_command(label="Enregistrer",command=lambda:fenetre.sauvegarde(self))
        self.fichier.add_command(label="Charger",command=lambda:fenetre.Charger(self))
        self.fichier.add_command(label="Nouveau joueur", command=lambda:fenetre.insertionjoueur(self))
        self.menu1.add_cascade(label="Aide",menu=self.aide)
        self.aide.add_command(label="regle du Jeux",command=lambda:fenetre.RegleJeux(self))
        self.aide.add_command(label="credit",command=lambda:fenetre.Credit(self))
        self.menu1.add_cascade(label="statistique",menu=self.statistique)
        self.statistique.add_command(label="personnel",command= lambda:Joueur.affichescore(self))
        self.statistique.add_command(label="top 10 des joueurs",command= lambda:fenetre.TOP10(self))
        self.fen.config(menu=self.menu1)
################################fond du programme#############################

        self.Fond=PhotoImage(file='image/ecran.gif')

        self.corps=Canvas(width=1024, height=640, bg="Black")
        self.corps.create_image( 0,0, image=self.Fond, anchor=NW )
        self.corps.place(x=0,y=0)


    def NEW_PARTY(self):   # renvoye ÃƒÆ’Ã‚Â   fenetreNombreJoueur pour recommencer une partie
        self.fen.destroy()
        fen=Tk()
        fen=fenetreNombreJoueur(fen)
    def insertionjoueur(self):  # renvoye ÃƒÆ’Ã‚Â  fenetreinsertionjoueur pour crÃƒÆ’Ã‚Â©er un Nouveau Joueur
        fen2=Tk()
        fen2=fenetreinsertjoueur(fen2)
    def ouvertBD(self):  # ouvre La Base  de donnee


        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()

    def RegleJeux (self):
        fen2=Tk()
        fen2=fenRegleJeux(fen2)
    def Credit (self):
        print("")
    def TOP10 (self):
        print("")

########################### creation de la fenetre de base####################


class fenRegleJeux(ptifenetre):
    def __init__(self,parent,):
        self.fen2=parent
        ptifenetre. __init__ (self,self.fen2)
        lb1= Label(root,text="bonjour, pour commencer une partie vous devez d'abord choisir le nombre de Joueur et inscrire les nouveau joueur. Quand cela es ")
class fenetreNombreJoueur(fenetre):
    """creation de la fenetre du choix du nombre de joueur"""

    def __init__(self,parent):
        self.fen=parent
        fenetre.__init__(self,self.fen)


        self.entete=Label(text="Culture Quest",font=("French Script MT", 48),fg="white",bg='#010810', relief=FLAT)
        self.entete.place(x=380,y=50)
        self.demande=Label(text="Veuillez choisir le nombre de joueurs ",font=("French Script MT",25),fg="white",bg='#000200', relief=FLAT)
        self.demande.place(x=340, y=200)
        self.bouton1Joueur=Button(parent,width=4,state=DISABLED,height=1,bg='#125991', text='1',font=("Harlow Solid Italic", 48), relief=FLAT,command=lambda:fenetreNombreJoueur.Solo(self))
        self.bouton1Joueur.place(x=50,y=300)
        self.bouton2Joueur=Button(parent,width=4,height=1,bg='#125991',text='2', font=("Harlow Solid Italic", 48), relief=FLAT,command=lambda:fenetreNombreJoueur.DeuxJoueur(self))
        self.bouton2Joueur.place(x=300,y=300)
        self.bouton3Joueur=Button(parent,width=4,height=1,bg='#125991', text='3',font=("Harlow Solid Italic", 48), relief=FLAT, command=lambda:fenetreNombreJoueur.TroisJoueur(self))
        self.bouton3Joueur.place(x=550,y=300)
        self.bouton4Joueur=Button(parent,width=4,height=1,bg='#125991',text='4',font=("Harlow Solid Italic", 48), relief=FLAT, command=lambda:fenetreNombreJoueur.quatreJoueur(self))
        self.bouton4Joueur.place(x=800,y=300)

        self.fen.mainloop()
    def Solo(self):
        self.conn.commit()
        self.c.close()

        self.fen.destroy()
        fen=Tk()
        fen=FenetreChoixJoueur(fen)
    def DeuxJoueur(self):
        self.conn.commit()
        self.c.close()

        self.fen.destroy()
        fen=Tk()
        fen=FenetreChoixJoueur2(fen)


    def TroisJoueur(self):
        self.conn.commit()
        self.c.close()

        self.fen.destroy()
        fen=Tk()
        fen=FenetreChoixJoueur3(fen)

    def quatreJoueur(self):
        self.conn.commit()
        self.c.close()

        self.fen.destroy()
        fen=Tk()
        fen=FenetreChoixJoueur4(fen)



class fenetreinsertjoueur(ptifenetre):
    def __init__(self,parent,):
        self.fen2=parent
        ptifenetre. __init__ (self,self.fen2)
        numjoueur="0"
        nomJoueur=""
        self.c.execute('''select max(NUM_Joueur) from Joueurs''')# recherche du Numero de joueur le plus ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©
        for row in self.c:
            row[0]
        row=int(row[0])

        self.numjoueur=row+1



        labelnonJoueur=Label(self.fen2,text ="Nouveau Joueur")

        self.nomjoueur=Entry(self.fen2,textvariable=nomJoueur,width=30,text="InsÃƒÆ’Ã‚Â©rez votre pseudo ici")

        labelnonJoueur.pack()

        self.nomjoueur.pack()
        boutonsauvegarde=Button(self.fen2,text="Sauvegarde", command=lambda:fenetreinsertjoueur.sauvegarde1(self))

        boutonsauvegarde.pack()

        self.fen2.mainloop()
    def sauvegarde1(self):
        nom=self.nomjoueur.get()

        num=self.numjoueur
        #print(num,nom,)
        self.c.execute ("""INSERT INTO Joueurs values(%s,"%s")"""%(num,nom,))#insertion des joueurs dans la BD
        self.conn.commit()
        self.c.close()
        self.fen2.destroy()

class FenetreChoixJoueur(fenetre):

    def __init__(self,parent):
        def saveJoueur(evt):
            self.nom_Joueur=self.NUM_Joueur.get()
            self.numero_joueur=self.c.execute('''select NUM_Joueur from Joueurs where NOM == "%s"'''%(self.nom_Joueur))
            for row in self.c:
                #print(row[0])
                self.numero_joueur=row[0]
        self.fen=parent
        fenetre.__init__(self,self.fen)
        self.numfen=1

        self.fen.tk.eval('package require Tix')
        labelJoueur=Label(self.fen, text="Joueur 1",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)



        labelJoueur.place(x=80,y= 100)
########################################################################choix de joueurs dans une liste remplit par la BD #####################################################################
        self.NUM_Joueur = tix.StringVar()
        combo_joueur = tix.ComboBox(self.fen, editable=1, dropdown=1, variable=self.NUM_Joueur, value="Chercher votre nom dans la liste",command=saveJoueur)
        combo_joueur.entry.config(state='readonly')  ## met la zone de texte en lecture seule

        for row in self.c.execute('''select * from Joueurs where NUM_Joueur > 0''') :
            self.numero_Joueurs=row[0]
            self.nom_Joueurs=row[1]
            combo_joueur.insert(self.numero_Joueurs,self.nom_Joueurs)

        combo_joueur.place(x=200,y= 110)
        self.numero_Joueurs=self.numero_Joueurs+1
        Joueurs=""
##############################################################################################################################################################################################




        boutonsauvegarde=Button(self.fen,text="Menu Principal",font=("Times New Roman", 12),bg='#06192a',fg='white', relief=FLAT , command=lambda:FenetreChoixJoueur.MenuPrincipal(self))

        boutonsauvegarde.place(x=400,y= 500)



    def MenuPrincipal(self):
        self.c.execute("DELETE FROM Pion")
        self.c.execute("DELETE FROM Partie")
########################################################appel de la fenetre Principal + mise ÃƒÆ’Ã‚Â  jour des donnees des pions par rapport aux joueurs#############################################
        self.c.execute("""INSERT INTO Partie values (%s,"%s","%s","%s","%s",%s,%s,%s,%s,%s)"""%(1,"","","","",0,0,0,0,0))#crÃƒÆ’Ã‚Â©ation de la mÃƒÆ’Ã‚Â©moire de la partie sur la BD
        if  self.numfen==4:

            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(1,"rouge",self.numero_joueur,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(2,"bleu",self.numero_joueur2,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(3,"orange",self.numero_joueur3,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(4,"vert",self.numero_joueur4,0,0))#insertion dans la BD des donnees des pions

            self.conn.commit()
            self.c.close()

            self.fen.destroy()
            fen=Tk()
            fen=fenetrePrincipal4(fen)
        if  self.numfen==3:
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(1,"rouge",self.numero_joueur,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(2,"bleu",self.numero_joueur2,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(3,"orange",self.numero_joueur3,0,0))#insertion dans la BD des donnees des pions
            self.conn.commit()
            self.c.close()
            self.fen.destroy()
            fen=Tk()
            fen=fenetrePrincipal3(fen)
        if  self.numfen==2:
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(1,"rouge",self.numero_joueur,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(2,"bleu",self.numero_joueur2,0,0))#insertion dans la BD des donnees des pions
            self.conn.commit()
            self.c.close()
            self.fen.destroy()
            fen=Tk()
            fen=fenetrePrincipal2(fen)
        if  self.numfen==1:
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(1,"rouge",self.numero_joueur,0,0))#insertion dans la BD des donnees des pions
            self.c.execute ("""INSERT INTO Pion values(%s,"%s",%s,%s,%s)"""%(2,"bleu",0,0,0))#insertion dans la BD des donnees des pions
            self.conn.commit()
            self.c.close()
            self.fen.destroy()
            fen=Tk()
            fen=fenetrePrincipal(fen)



class FenetreChoixJoueur2(FenetreChoixJoueur):

    def __init__(self,parent):
        def saveJoueur2(evt):
            self.nom_Joueur2=self.NUM_Joueur2.get()
            self.numero_joueur2=self.c.execute('''select NUM_Joueur from Joueurs where NOM == "%s"'''%(self.nom_Joueur2))
            for row in self.c:
                #print(row[0])
                self.numero_joueur2=row[0]
        self.fen=parent
        FenetreChoixJoueur.__init__(self,self.fen)
        self.numfen=2

        labelJoueur=Label(self.fen, text="Joueur 2",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)



        labelJoueur.place(x=80,y= 210)

        self.NUM_Joueur2 = tix.StringVar()
        combo_joueur2 = tix.ComboBox(self.fen, editable=1, dropdown=1, variable=self.NUM_Joueur2, value="Chercher votre nom dans la liste",command=saveJoueur2)
        combo_joueur2.entry.config(state='readonly')  ## met la zone de texte en lecture seule

        for row in self.c.execute('''select * from Joueurs where NUM_Joueur > 0''') :
            self.numero_Joueurs2=row[0]
            self.nom_Joueurs2=row[1]
            combo_joueur2.insert(self.numero_Joueurs2,self.nom_Joueurs2)

        combo_joueur2.place(x=200,y= 220)
        self.numero_Joueurs2=self.numero_Joueurs2+1
        Joueurs2=""






class FenetreChoixJoueur3(FenetreChoixJoueur2):
    def __init__(self,parent):
        def saveJoueur3(evt):
            self.nom_Joueur3=self.NUM_Joueur3.get()
            self.numero_joueur3=self.c.execute('''select NUM_Joueur from Joueurs where NOM == "%s"'''%(self.nom_Joueur3))
            for row in self.c:
                #print(row[0])
                self.numero_joueur3=row[0]
        self.fen=parent
        FenetreChoixJoueur2.__init__(self,self.fen)
        self.numfen=3
        labelJoueur=Label(self.fen, text="Joueur 3",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)



        labelJoueur.place(x=80,y= 320)

        self.NUM_Joueur3 = tix.StringVar()
        combo_joueur3 = tix.ComboBox(self.fen, editable=1, dropdown=1, variable=self.NUM_Joueur3, value="Chercher votre nom dans la liste",command=saveJoueur3)
        combo_joueur3.entry.config(state='readonly')  ## met la zone de texte en lecture seule

        for row in self.c.execute('''select * from Joueurs where NUM_Joueur > 0''') :
            self.numero_Joueurs3=row[0]
            self.nom_Joueurs3=row[1]
            combo_joueur3.insert(self.numero_Joueurs3,self.nom_Joueurs3)

        combo_joueur3.place(x=200,y= 330)
        self.numero_Joueurs3=self.numero_Joueurs3+1
        Joueurs3=""



class FenetreChoixJoueur4(FenetreChoixJoueur3):
    def __init__(self,parent):
        def saveJoueur4(evt):
            self.nom_Joueur4=self.NUM_Joueur4.get()
            self.numero_joueur4=self.c.execute('''select NUM_Joueur from Joueurs where NOM == "%s"'''%(self.nom_Joueur4))
            for row in self.c:
                #print(row[0])
                self.numero_joueur4=row[0]
        self.fen=parent
        FenetreChoixJoueur3.__init__(self,self.fen)
        self.numfen=4
        labelJoueur=Label(self.fen, text="Joueur 4",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)



        labelJoueur.place(x=80,y= 430)

        self.NUM_Joueur4 = tix.StringVar()
        combo_joueur4 = tix.ComboBox(self.fen, editable=1, dropdown=1, variable=self.NUM_Joueur4, value="Chercher votre nom dans la liste",command=saveJoueur4)
        combo_joueur4.entry.config(state='readonly')  ## met la zone de texte en lecture seule

        for row in self.c.execute('''select * from Joueurs  where NUM_Joueur > 0''') :
            self.numero_Joueurs4=row[0]
            self.nom_Joueurs4=row[1]
            combo_joueur4.insert(self.numero_Joueurs4,self.nom_Joueurs4)

        combo_joueur4.place(x=200,y= 440)
        self.numero_Joueurs4=self.numero_Joueurs4+1
        Joueurs3=""

        self.fen.mainloop()

class fenetrePrincipal(fenetre):
    """crÃƒÆ’Ã‚Â©ation du Menu Principal"""
    def __init__(self,parent):
        self.fen=parent
        fenetre.__init__(self,self.fen)
        self.entete=Label(text="Culture Quest",font=("French Script MT", 48),fg="white",bg='#010810', relief=FLAT)
        self.entete.place(x=380,y=50)
        Mycontainer6=Frame(self.fen, height=640, width=250, bg='black', relief= FLAT)
        Mycontainer6.place(x=0,y=5)

        LabelMENU=Label(Mycontainer6,text='Menu Principal',font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelMENU.place(x=50,y=255)
        can=Canvas(Mycontainer6 ,width=240,height=200, highlightcolor="white",highlightthickness=3,bg='black')
        can.place(x=5,y=300)
        boutonNouvelleParty=Button(Mycontainer6,text='Nouvelle partie',bg='#FFD133' ,width= 25,height=2,command=lambda:fenetrePrincipal.nouvellePartie(self))
        boutonNouvelleParty.place (x=35,y=330)
        boutonaide=Button(Mycontainer6,text='aide',bg='#FFD133',width= 25,height=2)
        boutonaide.place (x=35,y=380)
        boutonQuitter=Button(Mycontainer6,text='Quitter',bg='#FFD133',width= 25,height=2,command=self.fen.destroy)
        boutonQuitter.place (x=35,y=430)
        for row in self.c.execute('''select NOM from Joueurs where NUM_Joueur in (select NUM_Joueur from Pion where NUM_pion== "%s")'''%(1)) :
            self.NOMJoueur1=row[0]
        LabelJoueur1=Label(text='Joueur 1: ' + self.NOMJoueur1,font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelJoueur1.place(x=800,y=250)
    def nouvellePartie(self):
        self.fen.destroy()
        self.conn.commit()
        self.c.close()
        fen=Tk()
        fen=fen_dif(fen)

class fenetrePrincipal2(fenetrePrincipal):
    def __init__(self,parent):
        self.fen=parent
        fenetrePrincipal.__init__(self,self.fen)
        for row in self.c.execute('''select NOM from Joueurs where NUM_Joueur in (select NUM_Joueur from Pion where NUM_pion== "%s")'''%(2)) :
            self.NOMJoueur1=row[0]
        LabelJoueur2=Label(text='Joueur 2: ' + self.NOMJoueur1,font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelJoueur2.place(x=800,y=300)
class fenetrePrincipal3(fenetrePrincipal):
    def __init__(self,parent):
        self.fen=parent
        fenetrePrincipal2.__init__(self,self.fen)
        for row in self.c.execute('''select NOM from Joueurs where NUM_Joueur in (select NUM_Joueur from Pion where NUM_pion== "%s")'''%(3)) :
            self.NOMJoueur1=row[0]
        LabelJoueur3=Label(text='Joueur 3: ' + self.NOMJoueur1,font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelJoueur3.place(x=800,y=350)
class fenetrePrincipal4(fenetrePrincipal):
    def __init__(self,parent):
        self.fen=parent
        fenetrePrincipal3.__init__(self,self.fen)
        for row in self.c.execute('''select NOM from Joueurs where NUM_Joueur in (select NUM_Joueur from Pion where NUM_pion== "%s")'''%(4)) :
            self.NOMJoueur1=row[0]
        LabelJoueur4=Label(text='Joueur 4: ' + self.NOMJoueur1,font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelJoueur4.place(x=800,y=400)
class fen_dif(fenetre):
     def __init__(self,parent):
        self.fen=parent
        fenetre.__init__(self,self.fen)
        self.demande=Label(text="Veuillez choisir le niveau de difficultee ",font=("French Script MT",25),fg="white",bg='#000200', relief=FLAT)
        self.demande.place(x=340, y=200)
        self.bouton1Dif=Button(parent,width=4,height=1,bg='#125991', text='1',font=("Harlow Solid Italic", 40), relief=FLAT,command=lambda:fen_dif.difficulte(self,1))
        self.bouton1Dif.place(x=35,y=300)
        self.bouton2Dif=Button(parent,width=4,height=1,bg='#125991',text='2', font=("Harlow Solid Italic", 40), relief=FLAT,command=lambda:fen_dif.difficulte(self,2))
        self.bouton2Dif.place(x=235,y=300)
        self.bouton3Dif=Button(parent,width=4,height=1,bg='#125991', text='3',font=("Harlow Solid Italic", 40), relief=FLAT,command=lambda:fen_dif.difficulte(self,3))
        self.bouton3Dif.place(x=435,y=300)
        self.bouton4Dif=Button(parent,width=4,height=1,bg='#125991',text='4',font=("Harlow Solid Italic", 40), relief=FLAT,command=lambda:fen_dif.difficulte(self,4))
        self.bouton4Dif.place(x=635,y=300)
        self.bouton5Dif=Button(parent,width=4,height=1,bg='#125991',text='5',font=("Harlow Solid Italic", 40), relief=FLAT,command=lambda:fen_dif.difficulte(self,5))
        self.bouton5Dif.place(x=835,y=300)
     def difficulte(self,num):
        num=num
        self.fen.destroy()
        self.conn.commit()
        self.c.close()
        fen=Tk()
        fen=fen_Plateau(fen,num)



class fen_Plateau(fenetre):
    div=0
    def __init__(self,parent,div):

        global boutonhautdroit
        global boutonbasgauche
        global boutonhautgauche
        global boutonbasdroit
        global boutondroit
        global boutongauche
        global boutonbas
        global boutonhaut
        self.dif=div
        self.numeroJoueurTour=1
        self.imageplateau=PhotoImage(file='image/plateau.gif')
        self.gauche=PhotoImage(file='image/flecheG.gif')
        self.droite=PhotoImage(file='image/flecheD.gif')
        self.haut=PhotoImage(file='image/flecheH.gif')
        self.bas=PhotoImage(file='image/flecheB.gif')
        self.basgauche=PhotoImage(file='image/flecheBG.gif')
        self.hautdroite=PhotoImage(file='image/flecheHD.gif')
        self.hautgauche=PhotoImage(file='image/flecheHG.gif')
        self.basdroit=PhotoImage(file='image/flecheBD.gif')
        self.centre=PhotoImage(file='image/stop1.gif')
        self.k=1
        self.var1=1
        self.var2=1

        self.fen=parent
        fenetre.__init__(self,self.fen)
        self.difficultee=div
        #print(div)
        self.canevas = Canvas(self.corps,width =500, height =500, bg ='white', relief=GROOVE,bd=4)
        self.finit=0
        self.canevas.place(x=25, y=25)
        pion1=Pion('rouge','',1)
        pion2=Pion('bleu','',2)
        pion3=Pion('orange','',3)
        pion4=Pion('rouge','',4)
        fen_Plateau.plateau(self)
        self.nbrPion=self.numPion
        #print(self.canevas.find_all())

        boutondroit=Button(width=32,height=32,bg='#125991', image=self.droite,state=DISABLED,command= lambda:Pion.deplacement_HD(self))
        boutondroit.place (x=750,y=400)

        boutongauche=Button(width=32,height=32,bg='#125991', image=self.gauche,state=DISABLED,command= lambda:Pion.deplacement_HG(self))
        boutongauche.place (x=650,y=400)

        boutonhaut=Button(width=32,height=32,bg='#125991', image=self.haut,state=DISABLED,command= lambda:Pion.deplacement_VH(self))
        boutonhaut.place (x=700,y=350)

        boutonbas=Button(width=32,height=32,bg='#125991', image=self.bas,state=DISABLED,command= lambda:Pion.deplacement_VB(self))
        boutonbas.place (x=700,y=450)

        boutonhautdroit=Button(width=32,height=32,bg='#125991', image=self.hautdroite,state=DISABLED,command= lambda:Pion.deplacement_DHD(self))
        boutonhautdroit.place (x=750,y=350)

        boutonhautgauche=Button(width=32,height=32,bg='#125991', image=self.hautgauche,state=DISABLED,command= lambda:Pion.deplacement_DHG(self))
        boutonhautgauche.place (x=650,y=350)

        boutonbasdroit=Button(width=32,height=32,bg='#125991', image=self.basdroit,state=DISABLED,command= lambda:Pion.deplacement_DBD(self))
        boutonbasdroit.place (x=750,y=450)

        boutonbasgauche=Button(width=32,height=32,bg='#125991', image=self.basgauche,state=DISABLED,command= lambda:Pion.deplacement_DBG(self))
        boutonbasgauche.place (x=650,y=450)

        boutoncentre=Button(width=32,height=32,bg='#125991', image=self.centre,command= lambda:fen_Plateau.passetour(self))
        boutoncentre.place (x=700,y=400)

        self.LabelRepPion=Label(text='representation de votre pion',font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        self.LabelRepPion.place(x=650,y=100)
        self.repPion=Canvas(bg='black',width=50,height=50,relief=FLAT,bd=0)
        self.repPion.place(x=650,y=150)
        self.labJoueurTour=Label(text="",font=("French Script MT", 28),fg="white",bg='black', relief=FLAT)
        self.labJoueurTour.place(x=600,y=250)
        fen_Plateau.partie(self)
    def passetour(self):
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)
        fen_Plateau.partie(self)

    def ajouterCarre(self,joueur):

        #print('coucou')
        if joueur==1:
            self.c.execute("""select camenbertJoueur1 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            #print('longueur1',carrecouleur)
        elif joueur==2:
            self.c.execute("""select camenbertJoueur2 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
        elif joueur==3:
            self.c.execute("""select camenbertJoueur3 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
        elif joueur==4:
            self.c.execute("""select camenbertJoueur4 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
        try:

            #print('len',len(carrecouleur))
            if len(carrecouleur)==1:
                fen_Plateau.verifierlettre(self,1,carrecouleur)
                couleur1=self.couleur
                #print(couleur1)

                retc1=self.repPion.create_rectangle((1, 1, 23, 23), outline=couleur1, fill=couleur1, width=2)
                retc4=self.repPion.create_rectangle((27, 27,49, 49), outline="WHITE", fill="WHITE", width=2)
                retc4=self.repPion.create_rectangle((1, 27,23, 49), outline="WHITE", fill="WHITE", width=2)
                retc4=self.repPion.create_rectangle((27, 1,49, 23), outline="WHITE", fill="WHITE", width=2)

            if len(carrecouleur)==2:
                fen_Plateau.verifierlettre(self,1,carrecouleur)
                couleur1=self.couleur
                fen_Plateau.verifierlettre(self,2,carrecouleur)
                couleur2=self.couleur

                retc1=self.repPion.create_rectangle((1, 1, 23, 23), outline=couleur1, fill=couleur1, width=2)
                retc2=self.repPion.create_rectangle((27,27, 49, 49), outline=couleur2, fill=couleur2, width=2)
                retc4=self.repPion.create_rectangle((1, 27,23, 49), outline="WHITE", fill="WHITE", width=2)
                retc4=self.repPion.create_rectangle((27, 1,49, 23), outline="WHITE", fill="WHITE", width=2)
            if len(carrecouleur)==3:
                fen_Plateau.verifierlettre(self,1,carrecouleur)
                couleur1=self.couleur
                fen_Plateau.verifierlettre(self,2,carrecouleur)
                couleur2=self.couleur
                fen_Plateau.verifierlettre(self,3,carrecouleur)
                couleur3=self.couleur
                retc1=self.repPion.create_rectangle((1, 1, 23, 23), outline=couleur1, fill=couleur1, width=2)
                retc2=self.repPion.create_rectangle((27,27, 49, 49), outline=couleur2, fill=couleur2, width=2)
                retc3=self.repPion.create_rectangle((1, 27, 23, 49), outline=couleur3, fill=couleur3, width=2)
                retc4=self.repPion.create_rectangle((27, 1,49, 23), outline="WHITE", fill="WHITE", width=2)

            if len(carrecouleur)==4:
                retc1=self.repPion.create_rectangle((1, 1, 23, 23), outline="green", fill="green", width=2)
                retc2=self.repPion.create_rectangle((27,27, 49, 49), outline="Blue", fill="Blue", width=2)
                retc3=self.repPion.create_rectangle((1, 27, 23, 49), outline="orange", fill="orange", width=2)
                retc4=self.repPion.create_rectangle((27, 1,49, 23), outline="red", fill="red", width=2)
        except UnboundLocalError:
            retc1=self.repPion.create_rectangle((1, 1, 23, 23), outline="WHITE", fill="WHITE", width=2)
            retc4=self.repPion.create_rectangle((27, 27,49, 49), outline="WHITE", fill="WHITE", width=2)
            retc4=self.repPion.create_rectangle((1, 27,23, 49), outline="WHITE", fill="WHITE", width=2)
            retc4=self.repPion.create_rectangle((27, 1,49, 23), outline="WHITE", fill="WHITE", width=2)
    def verifierlettre(self,num,mot):
        num=num-1
        mot=mot
        if mot[num]=='V':
            self.couleur="green"

        if mot[num]=='R':
            self.couleur="red"
        if mot[num]=='O':
            self.couleur="orange"
        if mot[num]=='B':
            self.couleur="blue"
        #print(self.couleur)
        return self.couleur
    def plateau(self):
        """dessiner le plateau"""

        x=0
        y=5
        # Effacer d'abord tout dessin preexistant :
        self.canevas.delete(ALL)

        self.canevas.create_image(5,5,image=self.imageplateau,anchor=NW)


        self.c.execute('''select max(NUM_Pion) from Pion''')
        for row in self.c:
            row[0]
        row=int(row[0])
        #print(row,'numpion')
        self.numPion=row
        if self.numPion>=2:

            self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_Pion==(%s)'''%(6,1))
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(1)) :
                    x=row[1]
                    y=row[2]
            self.canevas.create_oval(x-20, y-20, x+20, y+20, fill='red')

            self.c.execute("""UPDATE Pion SET NUM_cases=(%s) where NUM_Pion==(%s)"""%(28,2))
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(2)):
                    x=row[1]
                    y=row[2]
            self.canevas.create_oval(x-20, y-20, x+20, y+20, fill='blue')
            if self.numPion==2:
                return self.numPion
        if self.numPion>=3:


            self.c.execute("""UPDATE Pion SET NUM_cases=(%s) where NUM_Pion==(%s)"""%(23,3))
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(3)) :
                    x=row[1]
                    y=row[2]
            self.canevas.create_oval(x-20, y-20, x+20, y+20, fill='orange')
            if self.numPion==3:
                return self.numPion
        if self.numPion>=4:

            self.c.execute("""UPDATE Pion SET NUM_cases=(%s) where NUM_Pion==(%s)"""%(1,4))
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(4)) :
                    x=row[1]
                    y=row[2]
            self.canevas.create_oval(x-20, y-20, x+20, y+20, fill='green')
            return self.numPion


    def partie(self):

        self.c.execute("""select numeroJoueurTour from Partie""")
        for row in self.c:
            row[0]
        self.numeroJoueurTour=int(row[0])

        self.c.execute('''select NOM from Joueurs where NUM_Joueur in(select NUM_Joueur from Pion where NUM_pion== "%s")'''%(self.numeroJoueurTour))
        for row in self.c:
            row[0]
        JoueurTour=row[0]
        fen_Plateau.fentour(self,JoueurTour)
        self.c.execute('''select couleur from Pion where NUM_pion== "%s"'''%(self.numeroJoueurTour))
        for row in self.c:
            row[0]
        couleur=row[0]

        self.labJoueurTour.configure(text="c'est au tour du Pion "+couleur+" de "+JoueurTour)
        fen_Plateau.tour(self)
    def tour(self):


        if self.nbrPion==2:
            if self.numeroJoueurTour%4==1:
                self.numeroJoueurTour+=1
                self.pion=1
                #print(self.numeroJoueurTour)
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            else :
                self.numeroJoueurTour+=1
                #print('nbr',self.numeroJoueurTour)
                self.pion=2
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion-1))
        if self.nbrPion==3:

            if self.numeroJoueurTour%4==1:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=1
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            elif self.numeroJoueurTour%4==2:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=2
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            else:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=3
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion-2))

        if self.nbrPion==4:

            if self.numeroJoueurTour%4==1:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=1
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            elif self.numeroJoueurTour%4==2:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=2
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            elif self.numeroJoueurTour%4==3:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=3
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion+1))
            else:
                self.numeroJoueurTour+=1
                #print(self.numeroJoueurTour)
                self.pion=4
                self.c.execute("""UPDATE Partie SET numeroJoueurTour=(%s)"""%(self.pion-3))
        fen_Plateau.ajouterCarre(self,self.pion)
        fen_Plateau.poserquestion(self)

    def poserquestion(self):
        if  self.pion==1:
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :#je vais chercher la position du pion dans la base de donnÃƒÆ’Ã‚Â©e
                x=row[1]
                y=row[2]
                case=row[0]
        elif self.pion==2:
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
                x=row[1]
                y=row[2]
                case=row[0]
        elif self.pion==3:
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
                x=row[1]
                y=row[2]
                case=row[0]
        elif self.pion==4:
            for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
                x=row[1]
                y=row[2]
                case=row[0]

        fen=Tk()
        FenQuestion(fen,self.dif,case,self.pion)
        self.conn.commit()

    def DISABLEDBouton(self):
        boutondroit.configure(state=DISABLED)
        boutongauche.configure(state=DISABLED)
        boutonhaut.configure(state=DISABLED)
        boutonbas.configure(state=DISABLED)

    def activeBouton(self):
        boutondroit.configure(state=ACTIVE)
        boutongauche.configure(state=ACTIVE)
        boutonhaut.configure(state=ACTIVE)
        boutonbas.configure(state=ACTIVE)
    def activeDiagonale(self):
        boutonhautdroit.configure(state=ACTIVE)
        boutonbasgauche.configure(state=ACTIVE)
        boutonhautgauche.configure(state=ACTIVE)
        boutonbasdroit.configure(state=ACTIVE)

    def DISABLEDDiagonale(self):
        boutonhautdroit.configure(state=DISABLED)
        boutonbasgauche.configure(state=DISABLED)
        boutonhautgauche.configure(state=DISABLED)
        boutonbasdroit.configure(state=DISABLED)

    def fentour(self,nom):
        nom=nom
        fen3 = Toplevel(self.fen)
        fen3.attributes('-topmost', 1)
        Fond2=PhotoImage(file='image/fon2.gif')
        emplacementX=(fen3.winfo_screenwidth()-300)//2
        emplacementY=(fen3.winfo_screenheight()-100)//2
        fen3.geometry("%dx%d%+d%+d"%(300,100,emplacementX,emplacementY))
        fen3.resizable(width=False,height=False)
        fen3.title('Culture Quest')

        can=Canvas(fen3,bg="black",width=300, height=100)
        can.create_image( 0,0, image=Fond2, anchor=NW )
        INFOTOUR=Label(can,text=nom+" c'est a  vous de jouer",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        boutonvalider=Button(can,text="ok",bg='black',fg='white',font=("Harlow Solid Italic", 20), relief=FLAT, command=fen3.destroy)
        can.place(x=0,y=0)
        INFOTOUR.place(x=10,y=10)
        boutonvalider.place(x=130,y=50)
    def erreur(self):

        fen4 = Toplevel(self.fen)
        fen4.attributes('-topmost', 1)
        Fond2=PhotoImage(file='image/fon2.gif')
        emplacementX=(fen4.winfo_screenwidth()-350)//2
        emplacementY=(fen4.winfo_screenheight()-100)//2
        fen4.geometry("%dx%d%+d%+d"%(350,100,emplacementX,emplacementY))
        fen4.resizable(width=False,height=False)
        fen4.title('erreur')

        can=Canvas(fen4,bg="black",width=400, height=100)
        can.create_image( 0,0, image=Fond2, anchor=NW )
        INFOTOUR=Label(can,text="veuillez choisir une autre direction car la \n direction demandÃƒÆ’Ã‚Â© n'est pas possible",font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        boutonvalider=Button(can,text="ok",bg='black',fg='white',font=("Harlow Solid Italic", 20), relief=FLAT, command=fen4.destroy)
        can.place(x=0,y=0)
        INFOTOUR.place(x=10,y=10)
        boutonvalider.place(x=130,y=70)

class FenQuestion(fenetre):

    def __init__(self,parent,dif,case,pion):
        self.fen2=parent

        self.dif=dif
        self.case=case
        self.fen=fen
        self.pion=pion
        ptifenetre.__init__(self,self.fen2)
        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        self.entreeQuestion=Label(self.fen2,text='', font=("helvetica",9))
        self.entreeQuestion.pack()
        self.boutonReponse1=Button(self.fen2,text="",width=26,font=("helvetica", 12),bg='#06192a',fg='white', relief=FLAT,command= lambda:FenQuestion.verification(self,3,self.questionChoisit,self.case))
        self.boutonReponse1.place(y=75,x=130)
        self.boutonReponse2=Button(self.fen2,text="",width=26,font=("helvetica", 12),bg='#06192a',fg='white', relief=FLAT,command= lambda:FenQuestion.verification(self,4,self.questionChoisit,self.case))
        self.boutonReponse2.place(y=140,x=130)
        self.boutonReponse3=Button(self.fen2,text="",width=26,font=("helvetica", 12),bg='#06192a',fg='white', relief=FLAT,command= lambda:FenQuestion.verification(self,5,self.questionChoisit,self.case))
        self.boutonReponse3.place(y=205,x=130)
        self.boutonReponse4=Button(self.fen2,text="",width=26,font=("helvetica", 12),bg='#06192a',fg='white', relief=FLAT,command= lambda:FenQuestion.verification(self,6,self.questionChoisit,self.case) )
        self.boutonReponse4.place(y=270,x=130)
        self.entreegagnee=Label(self.fen2,text='',width=44, font=("helvetica",12))
        self.entreegagnee.place(y=335,x=50)
        self.boutonquitter=Button(self.fen2,text="",font=("helvetica", 12),bg='black',fg='white',state=DISABLED,  relief=FLAT,command= self.fen2.destroy)
        self.boutonquitter.place(y=360,x=400)
        FenQuestion.choixQuestionDifType(self)
    def verificationouverturecasemobile(self):
        self.c.execute("""select casesMobile1 from Partie""")
        for row in self.c:
            self.ouverturediagonale1=row[0]

        self.c.execute("""select casesMobile2 from Partie""")
        for row in self.c:
            self.ouverturediagonale2=row[0]
        self.c.execute("""select casesMobile3 from Partie""")
        for row in self.c:
            self.ouverturediagonale3=row[0]
        self.c.execute("""select casesMobile4 from Partie""")
        for row in self.c:
            self.ouverturediagonale4=row[0]
        return self.ouverturediagonale1
        return self.ouverturediagonale2
        return self.ouverturediagonale3
        return self.ouverturediagonale4
    def verificationCamenbert(self,typedecase,Lettre):
        typedecase=typedecase
        Lettre=Lettre

        if self.pion==1:
            self.c.execute("""select camenbertJoueur1 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            #print('coucou2')
        elif self.pion==2:
            self.c.execute("""select camenbertJoueur2 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]

        elif self.pion==3:
            self.c.execute("""select camenbertJoueur3 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
        elif self.pion==4:
            self.c.execute("""select camenbertJoueur4 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
        #print('coucou3')
        liste=[]
        i=0
        #print(len(carrecouleur),'coucou4')
        while i < len(carrecouleur):
            liste.append(carrecouleur[i])
            #print(liste,'coucou5')
            i=i+1
        #print('coucou6')
        if Lettre not in liste:
            #print('coucou7')
            carrecouleur=carrecouleur+Lettre
            if self.pion==1:
                self.c.execute('''UPDATE Partie SET camenbertJoueur1='%s'  '''%(carrecouleur))
            if self.pion==2:
                self.c.execute('''UPDATE Partie SET camenbertJoueur2='%s' '''%(carrecouleur))
            if self.pion==3:
                self.c.execute('''UPDATE Partie SET camenbertJoueur3='%s' '''%(carrecouleur))
            if self.pion==4:
                self.c.execute('''UPDATE Partie SET camenbertJoueur4='%s' '''%(carrecouleur))
        else:

            pass
        FenQuestion.verificationlongueurchaine(self)
    def verificationlongueurchaine(self):
        if self.pion==1:
            self.c.execute("""select camenbertJoueur1 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            if len(carrecouleur)==4:
                self.ouverturediagonale1=1
                self.c.execute('''UPDATE Partie SET casesMobile1='%s'  '''%(self.ouverturediagonale1))
        elif self.pion==2:
            self.c.execute("""select camenbertJoueur2 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            if len(carrecouleur)==4:
                self.ouverturediagonale2=1
                self.c.execute('''UPDATE Partie SET casesMobile2='%s'  '''%(self.ouverturediagonale2))
        elif self.pion==3:
            self.c.execute("""select camenbertJoueur3 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            if len(carrecouleur)==4:
                self.ouverturediagonale3=1
                self.c.execute('''UPDATE Partie SET casesMobile3='%s'  '''%(self.ouverturediagonale3))
        elif self.pion==4:
            self.c.execute("""select camenbertJoueur4 from Partie""")
            for row in self.c:
                row[0]
            carrecouleur=row[0]
            if len(carrecouleur)==4:
                self.ouverturediagonale4=1
                self.c.execute('''UPDATE Partie SET casesMobile4='%s'  '''%(self.ouverturediagonale4))

    def verification(self,numCase,NumQuestion,case):

        numCase=numCase
        NumQuestion=NumQuestion
        case=case

        for row in self.c.execute('''select numReponseCase from question where NUM_question=="%s"'''%(NumQuestion)):
            numCasereponse=row[0]

        for row in self.c.execute('''select typeDeCases from Cases where NUM_cases==%s'''%(case)):
            typedecase=row[0]
            #print(typedecase,'type')
        for row in self.c.execute('''select Couleur from Cases where NUM_cases==%s'''%(case)):
            couleur=row[0]
            if couleur =='vert':
                Lettre='V'
            if couleur =='rouge':
                Lettre='R'
            if couleur =='orange':
                Lettre='O'
            if couleur =='bleu':
                Lettre='B'

        if numCasereponse==numCase:
            if typedecase=='S':
                FenQuestion.verificationCamenbert(self,typedecase,Lettre)


            self.entreegagnee.configure(text='BRAVO, vous avez trouve la bonne reponse')
            self.boutonquitter.configure(text='Quitter',state=ACTIVE)
            for row in self.c.execute( '''select avancement from Pion where NUM_pion==%s'''%(self.pion)):
                self.gagnee=row[0]

            if self.gagnee<=0:
                self.gagnee=1
                self.c.execute('''UPDATE Pion SET avancement=%s where NUM_pion=%s'''%(self.gagnee,self.pion))
                self.conn.commit()
                if self.ouverturediagonale1==1:
                    if self.pion==1:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)

                if self.ouverturediagonale2==1:
                    if self.pion==2:
                       fen_Plateau.activeDiagonale(self)
                       if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)
                if self.ouverturediagonale3==1:
                    if self.pion==1:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)
                if self.ouverturediagonale4==1:
                    if self.pion==1:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)

                else:
                    fen_Plateau.activeBouton(self)



            if self.gagnee>0:
                self.gagnee=+1
                self.c.execute('''UPDATE Pion SET avancement=%s where NUM_pion=%s'''%(self.gagnee,self.pion))
                if typedecase==S:
                    print('coucou,oiu')
                self.conn.commit()
                if self.ouverturediagonale1==1:
                    if self.pion==1:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)
                if self.ouverturediagonale2==1:
                    if self.pion==2:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)


                if self.ouverturediagonale3==1:
                    if self.pion==1:
                       fen_Plateau.activeDiagonale(self)
                       if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)
                if self.ouverturediagonale4==1:
                    if self.pion==1:
                        fen_Plateau.activeDiagonale(self)
                        if typedecase=='S':
                            self.fen.destroy()
                            self.fen2.destroy()
                            fen=Tk()
                            fenecranfin(fen,self.pion)
                else:
                     fen_Plateau.activeBouton(self)


        else:
            self.entreegagnee.configure(text="Desole,mais ce n'etait pas la bonne reponse")
            self.boutonquitter.configure(text='Quitter',state=ACTIVE)

    def choixQuestionDifType(self):

        num_question=[]
        question1=""
        #print(self.dif)
        for row in self.c.execute('''select NUM_question from Lien where NUM_cases= "%s" and NUM_Difficulter == "%s"'''%(self.case,self.dif)):

            num_question.append(row[0])

        #print('num_question',num_question)
        nbr_question=len(num_question)
        #print('nbe',nbr_question-1)
        numero_question=randint(0,nbr_question-1)

        self.questionChoisit=num_question[numero_question]


        for row in self.c.execute('''select * from question where NUM_question=="%s"'''%(self.questionChoisit)):
            question=row[1]
            reponse1=row[3]
            reponse2=row[4]
            reponse3=row[5]
            reponse4=row[6]
        num=len(question)

        passealaligne=0
        x=0
        if num>90:
            while passealaligne==0:

                question1=question1+question[x]

                num1=num-x
                x=x+1
                if x>=81 and question[x]==" ":
                    passealaligne=1
            question1=question1+"\n"

            for x in range (num1-1):


                question1=question1+question[x+(num-num1+1)]
        else:
            question1=question
        self.entreeQuestion.configure(text=question1)

        self.boutonReponse1.configure(text=reponse1)

        self.boutonReponse2.configure(text=reponse2)

        self.boutonReponse3.configure(text=reponse3)

        self.boutonReponse4.configure(text=reponse4)

class fenecranfin(fenetre):
   def __init__(self,parent,pion):
        self.fen2=parent
        ptifenetre.__init__(self,self.fen2)
        pion=pion
        for row in self.c.execute('''select NOM from Joueur where NUM_Joueur in(select NUM_Joueur from Pion where NUM_pion==%s'''%(pion)):
           nom=row[0]
        LabelFin=Label(text=nom+' ÃƒÆ’Ã‚Â  gagnÃƒÆ’Ã‚Â©(e) ',font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelFin.place(y=140,x=130)
        LabelJoueur3=Label(text='Joueur 3: ' + self.NOMJoueur1,font=("French Script MT", 20),fg="white",bg='black', relief=FLAT)
        LabelJoueur3.place(x=800,y=350)
class Joueur:
    def __init__ (self,nom,joueurnumero):
        self.nom=nom
        self.joueurnumero=joueurnumero

class JoueurHumain:
    def __init__(self,nom,joueurnumero,NbrPartieJouer,NbrPartieGagner):
        Joueur.__init__(self,nom,joueurnumero)

class Pion:
    def __init__(self,couleur,camenbert,num):
        self.couleur=couleur
        self.camenbert=camenbert
        self.num=num
    def deplacement_HD(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)
        fen_Plateau.DISABLEDDiagonale(self)

        pion=self.pion
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :#je vais chercher la position du pion dans la base de donnÃƒÆ’Ã‚Â©e
            x=row[1]
            y=row[2]
            case=row[0]



        try:
            x=x+83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'M')) :#je cherche si la case de dÃƒÆ’Ã‚Â©placement existe
                case1= row[0]
                #print('cae',case1)
            if case1 >=1 and case1<=28:

                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))#j'enregistre le changement de case du pion
                self.canevas.move(self.pion+1,self.k*self.var1*83,self.k*self.var2*0)#je dÃƒÆ’Ã‚Â©place mon pion visuellement
                fen_Plateau.partie(self)


        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)


    def deplacement_HG(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)
        pion=self.pion
        sortecase=""
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]

        try:
            x=x-83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'M')) :
                case1= row[0]
                sortecase= row[3]
            if case1 >=1 and case1<=28 :

                #print(case)
                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*-83,self.k*self.var2*0)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)
    def deplacement_VH(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)

        pion=self.pion
        #print(pion)
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]

        try:
            y=y-83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'M')) :
                case1= row[0]
            if case1 >=1 and case1<=28:

                #print('case',case1)
                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*0,self.k*self.var2*-83)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)
    def deplacement_VB(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4
        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)

        pion=self.pion

        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]


        try:
            y=y+83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'M')) :
                case1= row[0]
            if case1 >=1 and case1<=28:


                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion=(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*0,self.k*self.var2*83)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)







    def deplacement_DHD(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)

        pion=self.pion
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :#je vais chercher la position du pion dans la base de donnÃƒÆ’Ã‚Â©e
            x=row[1]
            y=row[2]
            case=row[0]



        try:
            x=x+83
            y=y-83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'N')) :#je cherche si la case de dÃƒÆ’Ã‚Â©placement existe
                case1= row[0]
                #print('cae',case1)
            if case1 >=1 and case1<=28:

                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))#j'enregistre le changement de case du pion
                self.canevas.move(self.pion+1,self.k*self.var1*83,self.k*self.var2*-83)#je dÃƒÆ’Ã‚Â©place mon pion visuellement
                fen_Plateau.partie(self)


        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)


    def deplacement_DHG(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)

        FenQuestion.verificationouverturecasemobile(self)
        self.ouverturediagonale1=self.ouverturediagonale1
        self.ouverturediagonale2=self.ouverturediagonale2
        self.ouverturediagonale3=self.ouverturediagonale3
        self.ouverturediagonale4=self.ouverturediagonale4

        if   self.ouverturediagonale1 == 1 or   self.ouverturediagonale2 ==1   or  self.ouverturediagonale3 ==1 or self.ouverturediagonale4 ==1:

            fen_Plateau.DISABLEDDiagonale(self)

        pion=self.pion
        sortecase=""
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]

        try:
            x=x-83
            y=y-83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'N')) :
                case1= row[0]
                sortecase= row[3]
            if case1 >=1 and case1<=28 :

                #print(case)
                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*-83,self.k*self.var2*-83)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)
    def deplacement_DBD(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)
        pion=self.pion
        #print(pion)
        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]

        try:
            y=y+83
            x=x+83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'N')) :
                case1= row[0]
            if case1 >=1 and case1<=28:
                #print('case',case1)
                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion==(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*83,self.k*self.var2*83)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)
    def deplacement_DBG(self):
        self.conn=sqlite3.connect("basededonnee\dbTfe11.db3")
        self.conn.row_factory=sqlite3.Row
        self.c=self.conn.cursor()
        fen_Plateau.DISABLEDBouton(self)
        pion=self.pion

        for row in self.c.execute('''select * from Cases where NUM_cases in(select NUM_cases from Pion where NUM_pion== "%s")'''%(self.pion)) :
            x=row[1]
            y=row[2]
            case=row[0]


        try:
            y=y+83
            x=x-83
            for row in self.c.execute('''select * from Cases where PositionX == "%s" and PositionY =="%s" and not typeDeCases=="%s"'''%(x,y,'N')) :
                case1= row[0]
            if case1 >=1 and case1<=28:


                self.c.execute('''UPDATE Pion SET NUM_cases=(%s) where NUM_pion=(%s)'''%(case1,pion))
                self.canevas.move(self.pion+1,self.k*self.var1*-83,self.k*self.var2*83)
                fen_Plateau.partie(self)
        except UnboundLocalError:

            fen_Plateau.activeBouton(self)
            fen_Plateau.erreur(self)



fen=Tk()
fen1=fenetreNombreJoueur(fen)
fen.mainloop()
