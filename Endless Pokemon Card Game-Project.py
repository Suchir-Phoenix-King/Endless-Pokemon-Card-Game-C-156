# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:28:41 2022

@author: PC_RC
"""

from tkinter import*
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Pokemon Card Game")
root.geometry("600x400")

root.configure(background = "orange")

abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open ("button.jpg"))
charmender = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
persion = ImageTk.PhotoImage(Image.open ("persion.jpg"))
paras = ImageTk.PhotoImage(Image.open ("paras.jpg"))
pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open ("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_score_label = Label(root, bg = "royal blue", fg = "white")
player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_score_label = Label(root, bg = "royal blue", fg = "white")
player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_pokemon_card_label = Label(root, bg = "white", fg = "black")
random_pokemon_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()