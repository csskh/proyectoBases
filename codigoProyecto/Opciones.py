import tkinter as tk
from tkinter import *

w = 1000
h = 600
fgcolor = '#FFFFFF'
bgcolor = '#bdc3c7'
azul = '#001b2e'
fuente = 'Lucida Sans'

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

        salirButton = tk.Button(self.master, text=' X ', borderwidth=1, relief='raised')
        salirButton.config(bg=bgcolor, font='Cambria 12 bold', fg= azul)
        salirButton.pack()
        salirButton.place(x=950, y=18)

        def salir():
            self.master.destroy()
        salirButton['command'] = salir
        
        menuLabel = tk.Label(headerFrame, text='MENÚ DE OPCIONES', font=(fuente,30, 'bold'), fg=fgcolor,bg=azul)
        menuLabel.place(x=300,y=10)

        adminLabel = tk.Label(self.master, text='Opciones del Admin',font=(fuente,20, 'bold'), fg=azul)
        adminLabel.place(x=60, y=80)

        consultLabel = tk.Label(self.master, text='Opciones del Consultor',font=(fuente,20, 'bold'), fg=azul)
        consultLabel.place(x=600, y=80)

        botonRE = tk.Button(self.master, text='Registrar Escuela/\nÁrea Académica', borderwidth=1, relief='raised')
        botonRE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonRE.pack()
        botonRE.place(x=60, y=130, width=300)

        botonRC = tk.Button(self.master, text='Registrar Curso', borderwidth=1, relief='raised')
        botonRC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonRC.pack()
        botonRC.place(x=60, y=230, width=300)

        botonRC = tk.Button(self.master, text='Registrar Curso', borderwidth=1, relief='raised')
        botonRC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonRC.pack()
        botonRC.place(x=60, y=230, width=300)
        
        

    
    def registroEscuela(self, master):
        registroFrame = tk.Frame(self.master, width=w, height=h)
        registroFrame.pack()
        registroEscLabel = tk.Label(registroFrame, text='Registro de escuela o area academica:', font=(fuente,16), fg='#2A2C2B',bg="#ecf0f1")
        registroEscLabel.place(x=72, y=-70)

        escuelaLabel = tk.Label(registroFrame, text='Nombre:', font=(fuente,16), fg='#2A2C2B',bg="#ecf0f1")
        registroEscLabel.place(x=82, y=-20)
        escuelaEntry = tk.Entry(registroFrame, font=(fuente,16))
        escuelaEntry.place(x=120, y=-20, width=250)

        botonRE = tk.Button(self.master, text='Registrar Escuela', borderwidth=1, relief='raised')
        botonRE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonRE.pack()
        botonRE.place(x=60, y=130, width=300)
        botonRE["command"] = registroEscuela()








