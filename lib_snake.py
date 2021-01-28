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

class Tete:

    def __init__(self,_height,_width,_canvas,_window):
        self.__posX = 10
        self.__posY = 10
        self.__height = _height
        self.__width = _width
        self.__pattern = _canvas.create_rectangle(self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height,fill="green")
        self.__canvas = _canvas
        self.__window = _window
        self.__arret = True
        self.__winning = True

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
    
    def deplacement(self):
        global pas_mouvementX, pas_mouvementY, nourriture

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
            Apple(20,20,self.__canvas,self.__window)

        self.__posX += pas_mouvementX
        self.__posY += pas_mouvementY
        self.__canvas.coords(self.__pattern,self.__posX,self.__posY,self.__posX+self.__width,self.__posY+self.__height)
        self.__window.after(100,self.deplacement)


class Apple:

    def __init__(self,_height,_width,_canvas,_window):
        global nourriture

        self.__posX = 10 + 20*randint(0,28)
        self.__posY = 10 + 20*randint(0,28)
        self.__height = _height
        self.__width = _width
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