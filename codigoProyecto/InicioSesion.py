from ast import main
import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from Opciones import mainform 
import mysql.connector

#---Conexión con MySQL---#
root = Tk()
connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='Rs220802', database='datosProyecto')
c = connection.cursor()

w = 430
h = 500
bgcolor = '#bdc3c7'
fgcolor = '#FFFFFF'
azul = '#001b2e'
fuente = 'Lucida Sans'

root.overrideredirect(1)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
headerFrame.pack()

titleLabel = tk.Label(headerFrame, text='Iniciar Sesión', padx=20, pady=5, bg='#001b2e', fg=fgcolor, font=(fuente,30),
                      width=20, height=2)
titleLabel.pack()

salirButton = tk.Button(root, text=' X ', borderwidth=1, relief='raised')
salirButton.config(bg=bgcolor, font='Cambria 12 bold', fg= azul)
salirButton.pack()
salirButton.place(x=390, y=18)

def salir():
    root.destroy()
salirButton['command'] = salir

# ----------- Página Inicio Sesión ------------- #
mainframe = tk.Frame(root, width=w, height=h)
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=30, pady=100, bg=bgcolor)

rolLabel = tk.Label(login_contentframe, text='Rol:', font=(fuente,16), bg=bgcolor, fg=azul)
rolLabel.place(x=72, y=-70)

rolEntry = tk.Entry(login_contentframe, font=(fuente,16))
rolEntry.place(x=120, y=-70, width=250)

usuarioLabel = tk.Label(login_contentframe, text='ID:', font=(fuente,16), bg=bgcolor, fg=azul)
usuarioLabel.place(x=82, y=-20)

usuarioEntry = tk.Entry(login_contentframe, font=(fuente,16))
usuarioEntry.place(x=120, y=-20, width=250)

contraLabel = tk.Label(login_contentframe, text='Contraseña:', font=(fuente,16), bg=bgcolor, fg=azul)
contraLabel.place(x=-10, y=30)

contraEntry = tk.Entry(login_contentframe, font=(fuente,16), show='⭐')
contraEntry.place(x=120, y=30, width=250)

entrarButton = tk.Button(login_contentframe,text="ENTRAR", font=(fuente,18), bg=azul,fg=fgcolor, padx=30, pady=15)
entrarButton.place(x=30, y=150, width=300)

irRegistroLabel = tk.Label(login_contentframe, text=">REGISTRAR NUEVO USUARIO<" , font=(fuente,12), bg=bgcolor, fg=azul)
irRegistroLabel.place(x=55, y=90)

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

#---Desplegar el Menú de Registro---#
def irRegistro():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)
    titleLabel['text'] = 'Registrar'
    titleLabel['font'] = fuente, 25
    titleLabel['bg'] = azul

irRegistroLabel.bind("<Button-1>", lambda page: irRegistro())


# ---Página de Registro --- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=15, pady=15, bg=bgcolor)

texto = tk.Label(register_contentframe, text='Tipos de Rol:\n'
                 'Admin: 1\n'
                 'Consultor: 2\n',
                 bg=bgcolor, font=(fuente, 12), justify='left')
texto.place(x=2,y=-8)

usuarioLabelPR = tk.Label(register_contentframe, text='ID:', font=(fuente,16), bg=bgcolor)
usuarioLabelPR.place(x=96, y=50)

usuarioEntryPR = tk.Entry(register_contentframe, font=(fuente,14))
usuarioEntryPR.place(x=135, y=52, width=250)

rolLabelPR = tk.Label(register_contentframe, text='Rol:', font=(fuente,16), bg=bgcolor)
rolLabelPR.place(x=86, y=90)

rolEntryPR = tk.Entry(register_contentframe, font=(fuente,14))
rolEntryPR.place(x=135, y=92, width=250)
                                                    
correoLabelPR = tk.Label(register_contentframe, text='Correo:', font=(fuente,16), bg=bgcolor)
correoLabelPR.place(x=48, y=128)

correoEntryPR = tk.Entry(register_contentframe, font=(fuente,14))
correoEntryPR.place(x=135, y=130, width=250)

contraLabelPR = tk.Label(register_contentframe, text='Contraseña:', font=(fuente,16), bg=bgcolor)
contraLabelPR.place(x=0, y=170)

contraEntryPR = tk.Entry(register_contentframe, font=(fuente,16), width=22, show='⭐')
contraEntryPR.place(x=135, y=172, width=250)

confirmarLabelPR = tk.Label(register_contentframe, text='Confirmar\nContraseña:', font=(fuente,16), bg=bgcolor, justify='left')
confirmarLabelPR.place(x=0, y=200)

confirmarEntryPR = tk.Entry(register_contentframe, font=(fuente,16), width=22, show='⭐')
confirmarEntryPR.place(x=135, y=222, width=250)

registrarButton = tk.Button(register_contentframe,text="Registrar", font=(fuente,18), bg=azul,fg=fgcolor, padx=30, pady=10)
registrarButton.place(x=50, y=265, width=300)

irLoginLabel = tk.Label(register_contentframe, text=">Sí ya tiene una cuenta. Inicie Sesión<",font=(fuente,12),bg=bgcolor,fg=azul)
irLoginLabel.place(x=50,y=350)

register_contentframe.pack(fill='both', expand=1)

def login():
    username = usuarioEntry.get().strip()
    password = contraEntry.get().strip()
    rol = rolEntry.get().strip()
    vals = (username, password, rol)
    select_query = "SELECT idUsuario, contrasena, idRol FROM usuario WHERE idUsuario = %s and contrasena = %s and idRol = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        mainformwindow = tk.Toplevel()
        app = ventanaMenuOpciones(mainformwindow)
        root.withdraw() 
        mainformwindow.protocol("WM_DELETE_WINDOW", salir) 

    else:
        messagebox.showwarning('Error','Rol o Usuario o Contraseña INCORRECTA')
entrarButton['command'] = login


#---Desplegar el menú de Iniciar Sesión---#
def irLogin():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    titleLabel['text'] = 'Iniciar Sesión'
    titleLabel['font'] = fuente, 25
    titleLabel['bg'] = azul


irLoginLabel.bind("<Button-1>", lambda page: irLogin())

#---Función que valida sí ya existe un usuario---#
def checkUsuario(usuario):
    usuario = usuarioEntryPR.get().strip()
    vals = (usuario,)
    select_query = "SELECT idUsuario FROM usuario WHERE idUsuario = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False

#---Función para registrar un nuevo usuario---#
def registrar():
    usuario = usuarioEntryPR.get().strip()
    email = correoEntryPR.get().strip()
    contra = contraEntryPR.get().strip()
    confirmar = confirmarEntryPR.get().strip()
    rol = rolEntryPR.get().strip()

    if len(usuario) > 0 and len(contra) > 0:
        if checkUsuario(usuario) == False: 
            if contra == confirmar:
                vals = (usuario, email, contra, rol)
                insert_query = "INSERT INTO usuario(idUsuario, emailUsuario, contrasena, idRol) VALUES (%s, %s, %s, %s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Registrado','Su usuario ha sido registrado')
            else:
                messagebox.showwarning('Contraseña','Las contraseñas no coinciden')
        else:
            messagebox.showwarning('Usuario No Válido','El nombre de usuario ya existe, elija otro')
    else:
        messagebox.showwarning('Espacios vacíos','Por favor llenar todos los espacios')

registrarButton['command'] = registrar

#---------------------------------------------------Menú de Opciones---------------------------------------------------#

def ventanaMenuOpciones(root):
    w = 1000
    h = 600
    root.overrideredirect(1)
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
    headerFrame.pack()

    salirButton = tk.Button(root, text=' X ', borderwidth=1, relief='raised')
    salirButton.config(bg=bgcolor, font='Cambria 12 bold', fg= azul)
    salirButton.pack()
    salirButton.place(x=950, y=18)
    salirButton['command'] = salir
        
    menuLabel = tk.Label(headerFrame, text='MENÚ DE OPCIONES', font=(fuente,30, 'bold'), fg=fgcolor,bg=azul)
    menuLabel.place(x=300,y=10)

    adminLabel = tk.Label(root, text='Opciones del Admin',font=(fuente,20, 'bold'), fg=azul)
    adminLabel.place(x=60, y=80)

    consultLabel = tk.Label(root, text='Opciones del Consultor',font=(fuente,20, 'bold'), fg=azul)
    consultLabel.place(x=600, y=80)

    modiLabel = tk.Label(root, text='Modificaciones',font=(fuente,20, 'bold'), fg=azul)
    modiLabel.place(x=380, y=400)

    botonRE = tk.Button(root, text='Registrar Escuela/\nÁrea Académica', borderwidth=1, relief='raised')
    botonRE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRE.pack()
    botonRE.place(x=60, y=130, width=300)

    botonRC = tk.Button(root, text='Registrar Curso', borderwidth=1, relief='raised')
    botonRC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRC.pack()
    botonRC.place(x=60, y=210, width=300)

    botonRCR = tk.Button(root, text='Asignar Requisito y/o \n Correquisitos a un Curso', borderwidth=1, relief='raised')
    botonRCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRCR.pack()
    botonRCR.place(x=60, y=260, width=300)

    botonRPE = tk.Button(root, text='Registrar Plan de Estudio', borderwidth=1, relief='raised')
    botonRPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRPE.pack()
    botonRPE.place(x=60, y=340, width=300)

    botonCPE = tk.Button(root, text='Consultar Plan de Estudio', borderwidth=1, relief='raised')
    botonCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCPE.pack()
    botonCPE.place(x=620, y=130, width=300)

    botonCCPE = tk.Button(root, text='Consultar Curso en \nPlan de Estudio', borderwidth=1, relief='raised')
    botonCCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCCPE.pack()
    botonCCPE.place(x=620, y=190, width=300)

    botonCR = tk.Button(root, text='Consultar Requisitos', borderwidth=1, relief='raised')
    botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCR.pack()
    botonCR.place(x=620, y=280, width=300)

    botonCCR = tk.Button(root, text='Consultar Correquisitos', borderwidth=1, relief='raised')
    botonCCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCCR.pack()
    botonCCR.place(x=620, y=340, width=300)

    botonER = tk.Button(root, text='Eliminar Requisito ', borderwidth=1, relief='raised')
    botonER.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonER.pack()
    botonER.place(x=30, y=480, width=300)

    botonECR = tk.Button(root, text='Eliminar Correquisito ', borderwidth=1, relief='raised')
    botonECR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonECR.pack()
    botonECR.place(x=345, y=480, width=300)

    botonC = tk.Button(root, text='Eliminar Curso ', borderwidth=1, relief='raised')
    botonC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonC.pack()
    botonC.place(x=660, y=480, width=300)
    botonC['command']=abrirVentana

'''
def abrirVentana():
    win = tk.Toplevel()
    app = registro(win)
    root.withdraw()
    win.protocol("WM_DELETE_WINDOW", salir) 

def registro(root):
    w = 1000
    h = 600
    root.overrideredirect(1)
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
    headerFrame.pack()
'''




root.mainloop()






























