# Alexandre Burlot
# début le 20 janvier 2021 
# Programme principale du jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
# 

import tkinter as tk
import lib_snake as ls

dimension_serpent = 20 # dimension correcte

def jeu():
    global dimension_serpent

    window = tk.Tk()
    window.geometry("1000x1000")
    quitter = tk.Button(window, text = "Quitter", command = window.destroy)
    canvas = tk.Canvas(window, height = 600, width = 600, background = "grey")
    canvas.pack()
    quitter.pack()
    serpent = ls.Snake(dimension_serpent,dimension_serpent,canvas)
    canvas.bind_all("<Key>",serpent.evenement)
    window.mainloop()

jeu()