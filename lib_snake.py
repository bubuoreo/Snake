# Alexandre Burlot
# bibliothèque lié au jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
# 

import tkinter as tk

class Snake:

    def __init__(self,_height,_width,_canvas):
        self.__corp = []
        self.__height = _height
        self.__width = _width
        self.__pattern = _canvas.create_rectangle(100,100,100+_height,100+_width,fill="green")
        self.__canvas = _canvas


class Food:

    def __init__(self,):
        # self.__

