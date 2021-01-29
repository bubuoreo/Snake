# Alexandre Burlot
# bibliothèque lié au jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
#  

import tkinter as tk
from random import randint

pas_mouvementX = 20
pas_mouvementY = 20
nourriture = None
serpent = []

class Tete:

    def __init__(self,_posX,_posY,_canvas,_window):
        global serpent
        self.__posX = _posX
        self.__posY = _posY
        self.__height = 20
        self.__width = 20
        self.__pattern = _canvas.create_rectangle(self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height,fill="green")
        self.__canvas = _canvas
        self.__window = _window
        self.__score = 0
        self.__arret = True
        self.__winning = True
        self.__mange = False
        serpent.append(self)

    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY
    
    def get_score(self):
        return self.__score
    
    def set_score(self,points):
        self.__score += points

    def evenement(self,event):
        global pas_mouvementX,pas_mouvementY

        touche = event.keysym

        if touche == "Down":
            pas_mouvementX = 0
            pas_mouvementY = 20
            if self.__arret :
                self.__arret = False
                self.deplacement()

        if touche == "Up":
            pas_mouvementX = 0
            pas_mouvementY = -20
            if self.__arret :
                self.__arret = False
                self.deplacement()

        if touche == "Left":
            pas_mouvementX = -20
            pas_mouvementY = 0
            if self.__arret :
                self.__arret = False
                self.deplacement()

        if touche == "Right":
            pas_mouvementX = 20
            pas_mouvementY = 0
            if self.__arret :
                self.__arret = False
                self.deplacement()
        
        if touche == "p":
            self.__arret = True
    
    def deplacement(self):
        global pas_mouvementX, pas_mouvementY, nourriture

        if self.__arret:
            return

        if self.__posX < 0:
            self.__winning = False
            return

        if self.__posX+self.__height > 600:
            self.__winning = False
            return

        if self.__posY < 0:
            self.__winning = False
            return

        if self.__posY+self.__width > 600:
            self.__winning = False
            return
        
        if (self.__posX == nourriture.get_posX() and
            self.__posY == nourriture.get_posY()): # collision avec la pomme
            self.__canvas.delete(nourriture.get_pattern())
            del nourriture
            Apple(10 + 20*randint(0,28),10 + 20*randint(0,28),self.__canvas,self.__window)
            self.__score += 1
            self.__mange = True

        # deplacement du corps
        for i in range(len(serpent)):
            if i != 0:
                if i == len(serpent)-1 and self.__mange:
                    save1 = serpent[i].get_posX()
                    save2 = serpent[i].get_posY()
                serpent[-i].set_posX(serpent[-i-1].get_posX())
                serpent[-i].set_posY(serpent[-i-1].get_posY())
                self.__canvas.coords(serpent[-i].get_pattern(),serpent[-i].get_posX(),serpent[-i].get_posY(),serpent[-i].get_posX()+self.__width,serpent[-i].get_posY()+self.__height)
        
        # création de l'objet de corp à la fin du serpent
        if self.__mange:
            Corps(save1,save2,self.__canvas,self.__window)
            save1,save2 = None,None
            self.__mange = False

        # déplaement de la tête
        self.__posX += pas_mouvementX
        self.__posY += pas_mouvementY
        self.__canvas.coords(self.__pattern,self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height)

        for i in range(len(serpent)):
            if i != 0:
                if self.__posX == serpent[i].get_posX() and self.__posY == serpent[i].get_posY():
                    print(self.__posX,serpent[i].get_posX())
                    self.__winning = False
                    return
        
        self.__window.after(100,self.deplacement)


class Apple:

    def __init__(self,_posX,_posY,_canvas,_window):
        global nourriture
        self.__posX = _posX
        self.__posY = _posY
        self.__height = 20
        self.__width = 20
        self.__pattern = _canvas.create_oval(self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height,fill="red")
        self.__canvas = _canvas
        self.__window = _window
        nourriture = self
    
    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY
    
    def get_height(self):
        return self.__height
    
    def get_width(self):
        return self.__width
    
    def get_pattern(self):
        return self.__pattern

    
class Corps:
    
    def __init__(self,_posX,_posY,_canvas,_window):
        global serpent
        self.__posX = _posX
        self.__posY = _posY
        self.__height = 20
        self.__width = 20
        self.__pattern = _canvas.create_rectangle(self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height,fill="lightgreen")
        self.__canvas = _canvas
        self.__window = _window
        serpent.append(self)
    
    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY
    
    def set_posX(self,new_posX):
        self.__posX = new_posX
    
    def set_posY(self,new_posY):
        self.__posY = new_posY

    def get_pattern(self):
        return self.__pattern