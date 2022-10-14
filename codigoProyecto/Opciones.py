import tkinter as tk
from tkinter import *


w = 1000
h = 600
fgcolor = '#FFEFD3'
azul = '#001b2e'
fuente = 'Lucida Sans'
'''
class mainform:
    def __init__(self, master):
        self.master = master
        self.master.overrideredirect(1)
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        selflbl = tk.Label(self.master, text='Hola', font=('verdana',25, 'bold'),
                            fg='#2A2C2B',bg="#ecf0f1")
        selflbl.place(x=300,y=200)

       
        headerFrame = tk.Frame(self.master, bg='#001b2e', width=w, height=70)
        headerFrame.pack()'''

class mainform:
    def __init__(self, master):
        self.master = master
        self.master.overrideredirect(1)
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        headerFrame = tk.Frame(self.master, bg='#001b2e', width=w, height=70)
        headerFrame.pack()
        menuLabel = tk.Label(headerFrame, text='MENÚ DE OPCIONES', font=(fuente,30, 'bold'), fg=fgcolor,bg=azul)
        menuLabel.place(x=300,y=10)

        adminLabel = tk.Label(self.master, text='Opciones del Admin',font=(fuente,20, 'bold'), fg=azul)
        adminLabel.place(x=60, y=80)

        consultLabel = tk.Label(self.master, text='Opciones del Consultor',font=(fuente,20, 'bold'), fg=azul)
        consultLabel.place(x=600, y=80)

        botonRE = tk.Button(self.master, text='Registrar Escuela', borderwidth=1, relief='raised')
        botonRE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonRE.pack()
        botonRE.place(x=60, y=130, width=300)


        







