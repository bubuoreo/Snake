# Alexandre Burlot
# début le 20 janvier 2021 
# Programme principale du jeu snake
# Objectif : faire un jeu snake stylé
# 
# Problèmes à corriger :
# 
# fond du canvas avec une image d'herbe peut-être
# titre à la fenêtre
# travailler la disposition
# mettre un écran de fin de partie
# mettre un peu de couleur tout simplement
#  

import tkinter as tk
import lib_snake as ls
from random import randint

dimension_serpent = 20 # dimension correcte

def jeu():
    global dimension_serpent
    ls.serpent = []
    window = tk.Tk()
    window.geometry("600x600")
    quitter = tk.Button(window, text = "Quitter", command = window.destroy)
    restart = tk.Button(window,text = "rejouer",command = lambda:[window.destroy(),jeu()])
    canvas = tk.Canvas(window, height = 401, width = 401, background = "grey")
    score = tk.Label(window,text = "Score : null")
    canvas.pack()
    score.pack()
    restart.pack()
    quitter.pack()
    tete = ls.Tete(303,303,canvas,window)
    pomme = ls.Apple(3 + 20*randint(0,19),3 + 20*randint(0,19),canvas,window)
    block = ls.Corps(323,303,canvas,window)
    canvas.bind_all("<Key>",tete.evenement)
    check_score(score,tete,window)
    window.mainloop()

def check_score(label_score,tete_serpent,fenetre):
    if label_score["text"] != "Score : "+str(tete_serpent.get_score()):
        label_score["text"] = "Score : "+str(tete_serpent.get_score())
    fenetre.after(100,lambda:[check_score(label_score,tete_serpent,fenetre)])


jeu()