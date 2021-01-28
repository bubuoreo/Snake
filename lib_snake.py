# Alexandre Burlot
# bibliothèque lié au jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
# 

import tkinter as tk

pas_mouvementX = 4
pas_mouvementY = 4

class Snake:
    global pas_mouvementX,pas_mouvementY

    def __init__(self,_height,_width,_canvas):
        self.__corp = [[100,100],[120,100]]
        self.__height = _height
        self.__width = _width
        self.__pattern = _canvas.create_rectangle(100,100,100+_height,100+_width,fill="green")
        self.__canvas = _canvas

    def evenement(self,event):
        touche = event.keysym

        if touche == "Down":
            pas_mouvementX = 0
            pas_mouvementY = 4

        if touche == "Up":
            pas_mouvementX = 0
            pas_mouvementY = -4

        if touche == "Left":
            pas_mouvementX = -4
            pas_mouvementY = 0

        if touche == "Right":
            pas_mouvementX = 4
            pas_mouvementY = 0
    
    def deplacement(self):
        for liste in self.__corp:
            liste[0] += pas_mouvementX
            liste[1] += pas_mouvementY

        


# class Food:

#     def __init__(self,):
#         self.__

