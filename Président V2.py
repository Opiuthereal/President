import tkinter as tk 
import pygame
import time
import random

racine = tk.Tk() #Creating the window
racine.title("Président???")
racine.geometry('1025x595')
racine.resizable(height=False,width=False)

FondJour = tk.PhotoImage(file="Images/Bombe.png") #Importation des photos nécessaires pour la classe jour (dont l'unique instance est journéee)
levierJ = tk.PhotoImage(file="Images/Lumière haut.png")
boutonJ = tk.PhotoImage(file="Images/bouton bombe jour.png")
boutonJourA =tk.PhotoImage(file="Images/bouton appuie bombe jour.png")
TiroirJ = tk.PhotoImage(file="Images/tiroir jour.png")
tasdefeuilles = tk.PhotoImage(file="Images/tas de feuille.png")
feuille = tk.PhotoImage(file="Images/Feuille non signée.png")
feuillesignée = tk.PhotoImage(file="Images/Feuille signée.png")
feuilleincurvée = tk.PhotoImage(file="Images/Feuille Incurvée.png")
feuilleincurvéesignée = tk.PhotoImage(file="Images/Feuille incurvée signée.png")
cléT = tk.PhotoImage(file="Images/clée tiroir.png")
cod = tk.PhotoImage(file="Images/code.png")
bc1 = tk.PhotoImage(file="Images/barre code 1.png")
bc2 = tk.PhotoImage(file="Images/barre code 2.png")
bc3 = tk.PhotoImage(file="Images/barre code 3.png")
bc4 = tk.PhotoImage(file="Images/barre code 4.png")
bc5 = tk.PhotoImage(file="Images/barre code 5.png")
b0 = tk.PhotoImage(file="Images/0.png")
b1 = tk.PhotoImage(file="Images/1.png")
b2 = tk.PhotoImage(file="Images/2.png")
b3 = tk.PhotoImage(file="Images/3.png")
b4 = tk.PhotoImage(file="Images/4.png")
b5 = tk.PhotoImage(file="Images/5.png")
b6 = tk.PhotoImage(file="Images/6.png")
b7 = tk.PhotoImage(file="Images/7.png")
b8 = tk.PhotoImage(file="Images/8.png")
b9 = tk.PhotoImage(file="Images/9.png")
sim = tk.PhotoImage(file="Images/Simon.png")
simvi = tk.PhotoImage(file="Images/simon violet.png")
simve = tk.PhotoImage(file="Images/simon vert.png")
simro = tk.PhotoImage(file="Images/simon rouge.png")
simma = tk.PhotoImage(file="Images/simon marron.png")
simbl = tk.PhotoImage(file="Images/simon bleu.png")
simja = tk.PhotoImage(file="Images/simon jaune.png")
simvia = tk.PhotoImage(file="Images/simon violet allumé.png")
simvea = tk.PhotoImage(file="Images/simon vert allumé.png")
simroa = tk.PhotoImage(file="Images/simon rouge allumé.png")
simmaa = tk.PhotoImage(file="Images/simon marron allumé.png")
simbla = tk.PhotoImage(file="Images/simon bleu allumé.png")
simjaa = tk.PhotoImage(file="Images/simon jaune allumé.png")
cléj = tk.PhotoImage(file="Images/clée icone Jaune.png")
cléb = tk.PhotoImage(file="Images/clée icone bleue.png")


FondNuit=tk.PhotoImage(file="Images/Bombe  noir.png") #Importation des photos nécessaires pour la classe nuit (dont l'unique instance est nuitée)
levierN=tk.PhotoImage(file="Images/Lumière bas.png")
boutonN = tk.PhotoImage(file="Images/bouton bombe nuit.png")
boutonNuitA = tk.PhotoImage(file="Images/bouton appuie bombe nuit.png")
TiroirN = tk.PhotoImage(file="Images/tiroir nuit.png")
tasdefeuillesN = tk.PhotoImage(file="Images/tas de feuille nuit.png")
feuilleN = tk.PhotoImage(file="Images/Feuille non signée nuit.png")
feuillesignéeN = tk.PhotoImage(file="Images/Feuille signée nuit.png")
feuilleincurvéeN = tk.PhotoImage(file="Images/Feuille Incurvée nuit.png")
feuilleincurvéesignéeN = tk.PhotoImage(file="Images/Feuille incurvée signée nuit.png")
feuilleindice = tk.PhotoImage(file="Images/feuille indice.png")

def keep_flat(event): #Fonction qui empêche les boutons désignés de s'enfoncer('Sunken') lorsqu'on clique dessus.        
    if event.widget is journée.BoutonBombe or event.widget is journée.levier or event.widget is nuitée.BoutonBombe or event.widget is nuitée.levier or event.widget is journée.clée or event.widget is nuitée.FeuilleIncurvée or event.widget is journée.FeuilleIncurvée : 
        event.widget.config(relief='flat')
        
racine.bind('<Button-1>', keep_flat)#Appel de la fonction précédente

class jour:
    def __init__(self,père,lev,Bout,boutJA,tiroir,tdf,feuill,FS,FI,FIS,clé,C,BC1,BC2,BC3,BC4,BC5,B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,simon,simonvert,simonviolet,simonbleu,simonrouge,simonmarron,simonjaune,simonvertallumé,simonvioletallumé,simonbleuallumé,simonrougeallumé,simonmarronallumé,simonjauneallumé,CléB,CléJ):
        #Création des boutons et Labels composant la classe jour
        self.root = père
        self.fond = tk.Label(self.root,image=FondJour,bd=0)
        self.levier = tk.Button(self.root,image=lev,bd=0,bg='#8a8ea3',relief='flat', activebackground='#8a8ea3')
        self.BoutonBombe = tk.Button(self.root,image=Bout,bd=0,bg='#afb3b6',relief='flat', activebackground='#afb3b6',command=self.appuie)
        self.BoutonBombeAppuie = tk.Button(self.root,image=boutJA,bd=0,bg='#afb3b6',relief='flat', activebackground='#afb3b6')
        self.Tiroir = tk.Label(self.root,image=tiroir,bd=0)
        self.clée = tk.Button(self.root,image=clé,bd=0,bg='#afb3b6',relief='flat', activebackground='#afb3b6')
        self.TasDeFeuille = tk.Label(self.root,image=tdf,bd=0)
        self.TasDeFeuille2 = tk.Label(self.root,image=tdf,bd=0)
        self.Feuille = tk.Label(self.root,image=feuill,bd=0)
        self.Feuille2 = tk.Label(self.root,image=feuill,bd=0)
        self.Feuille3 = tk.Label(self.root,image=feuill,bd=0)
        self.FeuilleSignée = tk.Label(self.root,image=FS,bd=0)
        self.FeuilleIncurvée = tk.Button(self.root,image=FI,bd=0,bg='#afb3b6',relief='flat', activebackground='#afb3b6', command=self.signature)
        self.feuilleIncurvéeSignée = tk.Label(self.root,image=FIS,bd=0)
        self.Code = tk.Label(self.root,image=C,bd=0)
        self.BarreCode1 = tk.Label(self.root,image=BC1,bd=0)
        self.BarreCode2 = tk.Label(self.root,image=BC2,bd=0)
        self.BarreCode3 = tk.Label(self.root,image=BC3,bd=0)
        self.BarreCode4 = tk.Label(self.root,image=BC4,bd=0)
        self.BarreCode5 = tk.Label(self.root,image=BC5,bd=0)
        self.cptcode=[]
        self.Bouton0 = tk.Button(self.root,image=B0,bd=0,bg='#afb3b6',relief='flat', activebackground='#000000',command=lambda:self.verifcode(0))
        self.Bouton1 = tk.Button(self.root,image=B1,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(1))
        self.Bouton2 = tk.Button(self.root,image=B2,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(2))
        self.Bouton3 = tk.Button(self.root,image=B3,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(3))
        self.Bouton4 = tk.Button(self.root,image=B4,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(4))
        self.Bouton5 = tk.Button(self.root,image=B5,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(5))
        self.Bouton6 = tk.Button(self.root,image=B6,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(6))
        self.Bouton7 = tk.Button(self.root,image=B7,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(7))
        self.Bouton8 = tk.Button(self.root,image=B8,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(8))
        self.Bouton9 = tk.Button(self.root,image=B9,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifcode(9))
        self.Simon = tk.Label(self.root,image=simon,bd=0)
        self.SimonVert = tk.Button(self.root,image=simonvert,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(1))
        self.SimonViolet = tk.Button(self.root,image=simonviolet,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(2))
        self.SimonRouge = tk.Button(self.root,image=simonrouge,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(3))
        self.SimonBleu = tk.Button(self.root,image=simonbleu,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(4))
        self.SimonMarron = tk.Button(self.root,image=simonmarron,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(5))
        self.SimonJaune = tk.Button(self.root,image=simonjaune,bd=0,bg='#000000',relief='flat', activebackground='#000000',command=lambda:self.verifSimon(6))
        self.SimonVertAllumé = tk.Label(self.root,image=simonvertallumé,bd=0)
        self.SimonVioletAllumé = tk.Label(self.root,image=simonvioletallumé,bd=0)
        self.SimonRougeAllumé = tk.Label(self.root,image=simonrougeallumé,bd=0)
        self.SimonBleuAllumé = tk.Label(self.root,image=simonbleuallumé,bd=0)
        self.SimonMarronAllumé = tk.Label(self.root,image=simonmarronallumé,bd=0)
        self.SimonJauneAllumé = tk.Label(self.root,image=simonjauneallumé,bd=0)
        self.CléeBleue = tk.Label(self.root,image=CléB,bd=0)
        self.CléeJaune =tk.Label(self.root,image=CléJ,bd=0)
        self.RéponseSimon = [5,6,2,5,4,4,3,5,6,1,5,3,3,2]
        self.RepSim=[]
        self.cptappuie = 0
        self.cptfeuilles = 0
        self.SimonStart = True
                
    def jour(self): #Affichage du plan de base de la journée (appelé par le levier qui fait varier le jour et la nuit)
        for child in self.root.winfo_children(): #Comme ça sert a rien de toujours supprimer l'affichage entier de la fenêtre seulement pour réafficher l'image jour, j'ai fait en sorte d'utiliser cette fonction le moins possible dans les méthodes de classes qui suivent
            child.place_forget()
            
        self.fond.place(x=0,y=0)
        self.levier.place(x=363,y=512)
        self.BoutonBombe.place(x=630,y=380)
        
        if self.cptappuie>=1:
            self.Code.place(x=299,y=401)
            self.Bouton0.place(x=320,y=468)
            self.Bouton1.place(x=302,y=423)
            self.Bouton2.place(x=319,y=423)
            self.Bouton3.place(x=336,y=423)
            self.Bouton4.place(x=302,y=438)
            self.Bouton5.place(x=319,y=438)
            self.Bouton6.place(x=336,y=438)
            self.Bouton7.place(x=302,y=452)
            self.Bouton8.place(x=319,y=452)
            self.Bouton9.place(x=336,y=452)
        
        if self.cptappuie>=3:
            self.Tiroir.place(x=922,y=415)
            self.clée.place(x=922,y=425)
            
        if self.cptcode == [6,6,6,6,6]:
            self.BarreCode5.place(x=304,y=407)
            self.CléeBleue.place(x=299,y=370)
            
        if self.cptfeuilles<=21:
            self.TasDeFeuille.place(x=743,y=418)
            self.Feuille.place(x=743,y=322+(2*self.cptfeuilles))
            
        elif self.cptfeuilles==21:
            self.Feuille.place(x=743,y=322+(2*self.cptfeuilles))
            
        if self.cptfeuilles>22 and self.cptfeuilles<43:
            self.Feuille3.place(x=823,y=322+(2*(self.cptfeuilles-21)))
            self.TasDeFeuille2.place(x=823,y=418)
            
        elif self.cptfeuilles<=22:
            self.Feuille3.place(x=823,y=322)
            self.TasDeFeuille2.place(x=823,y=418)
            
        if self.cptfeuilles<=43:
            self.FeuilleIncurvée.place(x=411,y=360)
        
        else:
            self.Simon.place(x=754,y=366)
            self.SimonVert.place(x=788,y=369)
            self.SimonViolet.place(x=788,y=415)
            self.SimonRouge.place(x=821,y=369)
            self.SimonBleu.place(x=757,y=415)
            self.SimonMarron.place(x=757,y=369)
            self.SimonJaune.place(x=821,y=415)
            if self.SimonStart:
                self.SimonDémonstration()
                self.SimonStart = False
                
        if self.RepSim == [5,6,2,5,4,4,3,5,6,1,5,3,3,2]:
            self.CléeJaune.place(x=778,y=317)
            
        self.root.mainloop()
    
    def appuie(self): #Lorsque l'on appuie sur le bouton rouge (animation et compteur)
        self.cptappuie+=1
        self.BoutonBombeAppuie.place(x=630,y=380)
        self.root.update()
        time.sleep(0.3)
        self.jour()
        
    def signature(self):#Lorsque l'on appuie sur la feuille incurvée au centre du bureau(animation et compteur)
        self.FeuilleIncurvée.place_forget()
        self.feuilleIncurvéeSignée.place(x=411,y=360)
        self.root.update()
        time.sleep(0.3)
        self.feuilleIncurvéeSignée.place_forget()
        self.FeuilleSignée.place(x=290,y=300)
        self.root.update()
        time.sleep(0.3)
        self.FeuilleSignée.place_forget()
        
        if self.cptfeuilles<21:
            self.Feuille.place(x=743,y=324+(2*self.cptfeuilles))
            self.Feuille2.place(x=636,y=349)
            self.root.update()
            time.sleep(0.3)
            self.FeuilleIncurvée.place(x=411,y=360)
            self.Feuille2.place_forget()
            
        elif self.cptfeuilles==21:
            self.Feuille.place_forget()
            self.TasDeFeuille.place_forget()
            self.FeuilleIncurvée.place(x=411,y=360)
            
        elif self.cptfeuilles<43:
            self.Feuille3.place(x=823,y=322+(2*(self.cptfeuilles-21)))
            self.Feuille2.place(x=636,y=349)
            self.root.update()
            time.sleep(0.3)
            self.FeuilleIncurvée.place(x=411,y=360)
            self.Feuille2.place_forget()
            
        elif self.cptfeuilles==43:
            self.Feuille3.place_forget()
            self.TasDeFeuille2.place_forget()
            self.FeuilleIncurvée.place(x=411,y=360)
            
        else:
            self.jour()
            
        self.cptfeuilles+=1
        self.root.mainloop()
    
    def verifcode(self,x):#Vérifie le code qui est entré dans la machine sur la gauche du bureau
        self.cptcode.append(x)
        
        if len(self.cptcode)==1:
            self.BarreCode1.place(x=304,y=407)
            self.root.update()
            
        elif len(self.cptcode)==2:
            self.BarreCode1.place_forget()
            self.BarreCode2.place(x=304,y=407)
            self.root.update()
            
        elif len(self.cptcode)==3:
            self.BarreCode2.place_forget()
            self.BarreCode3.place(x=304,y=407)
            self.root.update()
            
        elif len(self.cptcode)==4:
            self.BarreCode3.place_forget()
            self.BarreCode4.place(x=304,y=407)
            self.root.update()
            
        elif len(self.cptcode)==5:
            self.BarreCode4.place_forget()

            if self.cptcode == [6,6,6,6,6]:
                self.CléeBleue.place(x=299,y=370)
                self.Bouton0.place_forget()
                self.Bouton1.place_forget()
                self.Bouton2.place_forget()
                self.Bouton3.place_forget()
                self.Bouton4.place_forget()
                self.Bouton5.place_forget()
                self.Bouton6.place_forget()
                self.Bouton7.place_forget()
                self.Bouton8.place_forget()
                self.Bouton9.place_forget()
                self.BarreCode5.place(x=304,y=407)
                self.root.mainloop()
                
            else:
                self.cptcode=[]
                self.BarreCode5.place(x=304,y=407)
                self.root.update()
                time.sleep(0.3)
                self.BarreCode5.place_forget()
                self.root.update()

    def SimonDémonstration(self):#Affiche le code qu'il faut entrer dans le jeu de lumière sur la gauche du bureau(animation)
        self.SimonMarronAllumé.place(x=757,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonJauneAllumé.place(x=821,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonJauneAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonVioletAllumé.place(x=788,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonVioletAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place(x=757,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonBleuAllumé.place(x=757,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonBleuAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonBleuAllumé.place(x=757,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonBleuAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place(x=821,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place(x=757,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonJauneAllumé.place(x=821,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonJauneAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonVertAllumé.place(x=788,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonVertAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place(x=757,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonMarronAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place(x=821,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place(x=821,y=369)
        self.root.update()
        time.sleep(0.5)
        self.SimonRougeAllumé.place_forget()
        self.root.update()
        time.sleep(0.5)
        self.SimonVioletAllumé.place(x=788,y=415)
        self.root.update()
        time.sleep(0.5)
        self.SimonVioletAllumé.place_forget()
        self.root.update()
    
    def verifSimon(self,x):#Vérifie si le code tapé dans le jeu de lumière est bon ou pas 
        self.RepSim.append(x)
        if len(self.RepSim) == len(self.RéponseSimon):
            if self.RepSim == [5,6,2,5,4,4,3,5,6,1,5,3,3,2]:
                self.CléeJaune.place(x=778,y=317)
                self.root.mainloop()
            else:
                self.RepSim=[]
                self.SimonDémonstration()
        
        
class nuit:
    def __init__(self,père,lev,Bout,boutNA,tiroir,tdf,feuill,FS,FI,FIS,indice):
        #Création des boutons et Labels composant la classe jour
        self.root = père
        self.fond = tk.Label(self.root,image=FondNuit,bd=0)
        self.levier = tk.Button(self.root,image=lev,bd=0,bg='#202b35',relief='flat', activebackground='#202b35')
        self.BoutonBombe = tk.Button(self.root,image=Bout,bd=0,bg='#8a8ea3',relief='flat', activebackground='#8a8ea3',command=self.appuie)
        self.BoutonBombeAppuie = tk.Button(self.root,image=boutNA,bd=0,bg='#8a8ea3',relief='flat', activebackground='#8a8ea3')
        self.Tiroir = tk.Label(self.root,image=tiroir,bd=0)
        self.TasDeFeuille = tk.Label(self.root,image=tdf,bd=0)
        self.Feuille = tk.Label(self.root,image=feuill,bd=0)
        self.Feuille2 = tk.Label(self.root,image=feuill,bd=0)
        self.FeuilleSignée = tk.Label(self.root,image=FS,bd=0)
        self.FeuilleIncurvée = tk.Button(self.root,image=FI,bd=0,bg='#8a8ea3',relief='flat', activebackground='#8a8ea3', command=self.signature)
        self.feuilleIncurvéeSignée = tk.Label(self.root,image=FIS,bd=0)
        self.feuilleIndice = tk.Label(self.root,image=indice,bd=0)
        self.cptappuie = 0
        self.cptfeuilles = 0
        
    def nuit(self): #Affichage du plan de base de la nuit (appelé par le levier qui fait varier le jour et la nuit)
        for child in self.root.winfo_children():#Comme ça sert a rien de toujours supprimer l'affichage entier de la fenêtre seulement pour réafficher l'image jour, j'ai fait en sorte d'utiliser cette fonction le moins possible dans les méthodes de classes qui suivent
            child.place_forget()       
        self.fond.place(x=0,y=0)
        self.levier.place(x=363,y=512)
        self.BoutonBombe.place(x=630,y=380)
        self.TasDeFeuille.place(x=743,y=418)
        self.Feuille.place(x=743,y=322+(2*self.cptfeuilles))
        if self.cptfeuilles>=6:
            self.feuilleIndice.place(x=411,y=360)
        else:
            self.FeuilleIncurvée.place(x=411,y=360)
        if self.cptappuie>=3:
            self.Tiroir.place(x=922,y=415)
        self.root.mainloop()
        
    def appuie(self): #Lorsque l'on appuie sur le bouton rouge (animation et compteur)
        self.cptappuie+=1
        self.BoutonBombeAppuie.place(x=630,y=380)
        self.root.update()
        time.sleep(0.3)
        if self.cptappuie>=3:
            self.Tiroir.place(x=922,y=415)
        self.BoutonBombeAppuie.place_forget()
        
    def signature(self):#Lorsque l'on appuie sur la feuille incurvée au centre du bureau(animation et compteur)
        self.FeuilleIncurvée.place_forget()
        self.feuilleIncurvéeSignée.place(x=411,y=360)
        self.root.update()
        time.sleep(0.3)
        self.feuilleIncurvéeSignée.place_forget()
        self.FeuilleSignée.place(x=290,y=300)
        self.root.update()
        time.sleep(0.3)
        self.FeuilleSignée.place_forget()
        
        if self.cptfeuilles<6:
            self.Feuille.place(x=743,y=324+(2*self.cptfeuilles))
            self.Feuille2.place(x=636,y=349)
            self.root.update()
            time.sleep(0.3)
            self.FeuilleIncurvée.place(x=411,y=360)
            self.Feuille2.place_forget()
            
        elif self.cptfeuilles==6:
            self.feuilleIndice.place(x=411,y=360)
            
        self.cptfeuilles+=1
        self.root.mainloop()
#Création des instance journée et nuitée issu des classe respectives jour et nuit
journée = jour(racine,levierJ,boutonJ,boutonJourA,TiroirJ,tasdefeuilles,feuille,feuillesignée,feuilleincurvée,feuilleincurvéesignée,cléT,cod,bc1,bc2,bc3,bc4,bc5,b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,sim,simve,simvi,simbl,simro,simma,simja,simvea,simvia,simbla,simroa,simmaa,simjaa,cléb,cléj)
nuitée = nuit(racine,levierN,boutonN,boutonNuitA,TiroirN,tasdefeuillesN,feuilleN,feuillesignéeN,feuilleincurvéeN,feuilleincurvéesignéeN,feuilleindice)
journée.levier.config(command=nuitée.nuit)#Je configure la command du leviers ici car sinon il ne connait pas les instances journée et nuitée
nuitée.levier.config(command=journée.jour)
journée.jour()#Lancement du jeu en plein jour