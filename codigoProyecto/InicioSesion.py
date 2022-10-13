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
connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='atiDBPruebas$', database='datosProyecto')
c = connection.cursor()

w = 430
h = 500
bgcolor = '#bdc3c7'
fgcolor = '#FFEFD3'
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

#---Ingreso de datos---#
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
        app = mainform(mainformwindow)
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

root.mainloop()






























