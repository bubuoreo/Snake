# Alexandre Burlot
# début le 20 janvier 2021 
# Programme principale du jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
# 

import tkinter as tk
import lib_snake as ls
from random import randint

dimension_serpent = 20 # dimension correcte

def jeu():
    global dimension_serpent
    ls.serpent = []
    window = tk.Tk()
    window.geometry("1000x1000")
    quitter = tk.Button(window, text = "Quitter", command = window.destroy)
    restart = tk.Button(window,text = "rejouer",command = lambda:[window.destroy(),jeu()])
    canvas = tk.Canvas(window, height = 600, width = 600, background = "grey")
    canvas.pack()
    restart.pack()
    quitter.pack()
    tete = ls.Tete(30,10,canvas,window)
    pomme = ls.Apple(10 + 20*randint(0,28),10 + 20*randint(0,28),canvas,window)
    block = ls.Corps(10,10,canvas,window)
    canvas.bind_all("<Key>",tete.evenement)
    window.mainloop()

jeu()