from ast import main
from calendar import month
import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from turtle import width
import mysql.connector

#---Conexión con MySQL---#
root = Tk()
base = 'datosProyectoProgramado'
connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='Rs220802', database=base)
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

rol = None
def login():
    global rol 
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

#---Función que valida sí ya existe un usuario o un correo---#
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

def checkEmail(email):
    email = correoEntryPR.get().strip()
    vals = (email,)
    select_query = "SELECT emailUsuario FROM usuario WHERE emailUsuario = %s"
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
    emailVar = '@' in email
    mailVar = '.' in email

    if len(usuario) > 0 and len(contra) > 0:
        if emailVar == True and mailVar == True:
            if checkUsuario(usuario) == False and checkEmail(email) == False: 
                if contra == confirmar:
                    vals = (usuario, email, contra, rol)
                    insert_query = "INSERT INTO usuario(idUsuario, emailUsuario, contrasena, idRol) VALUES (%s, %s, %s, %s)"
                    c.execute(insert_query, vals)
                    connection.commit()
                    messagebox.showinfo('Registrado','Su usuario ha sido registrado')
                else:
                    messagebox.showwarning('Contraseña','Las contraseñas no coinciden')
            else:
                messagebox.showwarning('Usuario o Correo No Válido','El nombre de usuario o el correo ya existe, elija otro')
        else:
            messagebox.showwarning('Correo No Válido','Ingrese un correo que contenga @ y .')
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
    botonRE['command']= registrarEscuela

    botonRC = tk.Button(root, text='Registrar Curso', borderwidth=1, relief='raised')
    botonRC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRC.pack()
    botonRC.place(x=60, y=210, width=300)
    botonRC['command']= registrarCurso

    botonRCR = tk.Button(root, text='Asignar Requisito y/o \n Correquisitos a un Curso', borderwidth=1, relief='raised')
    botonRCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRCR.pack()
    botonRCR.place(x=60, y=260, width=300)
    botonRCR['command']=asignarRC

    botonRPE = tk.Button(root, text='Registrar Plan de Estudio', borderwidth=1, relief='raised')
    botonRPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonRPE.pack()
    botonRPE.place(x=60, y=340, width=300)
    botonRPE['command']=registrarPE

    botonCPE = tk.Button(root, text='Consultar Plan de Estudio', borderwidth=1, relief='raised')
    botonCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCPE.pack()
    botonCPE.place(x=620, y=130, width=300)
    botonCPE['command']=consultarPlan

    botonCCPE = tk.Button(root, text='Consultar Curso en \nPlan de Estudio', borderwidth=1, relief='raised')
    botonCCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCCPE.pack()
    botonCCPE.place(x=620, y=190, width=300)
    botonCCPE['command']=consultarCurso

    botonCR = tk.Button(root, text='Consultar Requisitos', borderwidth=1, relief='raised')
    botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCR.pack()
    botonCR.place(x=620, y=280, width=300)
    botonCR['command']=consultarReq

    botonCCR = tk.Button(root, text='Consultar Correquisitos', borderwidth=1, relief='raised')
    botonCCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonCCR.pack()
    botonCCR.place(x=620, y=340, width=300)
    botonCCR['command']=consultarReq

    botonER = tk.Button(root, text='Eliminar Requisito ', borderwidth=1, relief='raised')
    botonER.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonER.pack()
    botonER.place(x=30, y=480, width=300)
    botonER['command']=eliminarReq

    botonECR = tk.Button(root, text='Eliminar Correquisito ', borderwidth=1, relief='raised')
    botonECR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonECR.pack()
    botonECR.place(x=345, y=480, width=300)
    botonECR['command']=eliminarCo

    botonC = tk.Button(root, text='Eliminar Curso ', borderwidth=1, relief='raised')
    botonC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
    botonC.pack()
    botonC.place(x=660, y=480, width=300)
    botonC['command']=eliminarCurso

#---------------------------------- Rol del Admin ----------------------------------#

def registrarEscuela():
    if rol == '1':
        ventana = tk.Toplevel()
        ventana.title('Registrar Escuela')
        w = 600
        h = 600
        ws = ventana.winfo_screenwidth()
        hs = ventana.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        ventana.geometry("%dx%d+%d+%d" % (w, h, x, y))
        ventana.resizable(0,0)
        headerFrame = tk.Frame(ventana, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Registrar Escuela o Área Académica', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=20, y=15)

        nombreLabel = tk.Label(ventana, text='Nombre Escuela:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=60, y=130)

        nombreEntry = tk.Entry(ventana, font=(fuente,16))
        nombreEntry.place(x=60, y=180, width=480, height=40)

        codigoLabel = tk.Label(ventana, text='Código:', fg=azul, font=(fuente, 20, 'bold'))
        codigoLabel.pack()
        codigoLabel.place(x=60, y=260)

        codigoEntry = tk.Entry(ventana, font=(fuente,16))
        codigoEntry.place(x=60, y=320, width=480, height=40)
        
        def limpiarCampos():
            nombreEntry.delete(0, "end")
            codigoEntry.delete(0, "end")
            
        botonLC = tk.Button(ventana, text='Limpiar Campos', borderwidth=1, relief='raised', command=limpiarCampos)
        botonLC.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonLC.pack()
        botonLC.place(x=340, y=400, width=200)

        def checkCodigo(codigo):
            codigo = codigoEntry.get().strip()
            var = [(codigo)]
            select_query = "SELECT codigoEscuela FROM escuela WHERE codigoEscuela = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            if user is not None:
                return True
            else:
                return False

        def checkEscuela(escuela):
            escuela = nombreEntry.get().strip()
            var = [(escuela)]
            select_query = "SELECT nombreEscuela FROM escuela WHERE nombreEscuela = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            if user is not None:
                return True
            else:
                return False

        def registroDatos():
            nombre = nombreEntry.get().strip()
            codigo = codigoEntry.get().strip()
            nombreVar = nombre.replace(' ', '')

            if nombreVar != '' and codigo != '': 
                if nombreVar.isalpha() == True and codigo.isalpha() == True:
                    if len(nombre) > 0 and len(codigo) == 2:
                        if checkCodigo(codigo) == False and checkEscuela(nombre) == False:
                            vals = (codigo.upper(), nombre)
                            insert_query = "INSERT INTO escuela(codigoEscuela, nombreEscuela) VALUES (%s, %s)"
                            c.execute(insert_query, vals)
                            connection.commit()
                            messagebox.showinfo('Registrado','La escuela ha sido registrada')
                            root.destroy()
                        else:
                            messagebox.showwarning('Error', 'La escuela o el código ya existe, elija otro')
                    else:
                        messagebox.showwarning('Espacios vacíos','Por favor llenar todos los espacios\nO asignar un Código de 2 letras')
                else:
                    messagebox.showwarning('Error', 'La escuela y el código deben ser LETRAS')
            else:
                    messagebox.showwarning('Error', 'Debe llenar todos los espacios')
             
        botonR = tk.Button(ventana, text='REGISTRAR', borderwidth=1, relief='raised')
        botonR.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonR.pack()
        botonR.place(x=150, y=500, width=300)
        botonR['command']=registroDatos

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

def registrarCurso():
    if rol == '1':
        root = tk.Toplevel()
        root.title('Registrar Curso')
        w = 600
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Registrar Cursos', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=180, y=15)

        nombreLabel = tk.Label(root, text='Nombre Escuela:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=40, y=90)

        escuela = 'select nombreEscuela from escuela'
        c.execute(escuela)
        var = c.fetchall()

        opciones = var
        opcionesVar = tk.StringVar()

        nombreEntry = tk.OptionMenu(root, opcionesVar, *opciones)
        nombreEntry.config(font=(fuente, 16, 'bold'))
        nombreEntry.place(x=40, y=130, width=290, height=40)

        codEscuela = tk.Label(root, text='Código Escuela:', fg=azul, font=(fuente, 20, 'bold'))
        codEscuela.pack()
        codEscuela.place(x=340, y=90)

        codigoEscuela = tk.Entry(root, font = (fuente, 14))
        codigoEscuela.place(x = 350, y = 130, width=210, height=40)
        
        nombreCLabel = tk.Label(root, text='Nombre del Curso:', fg=azul, font=(fuente, 20, 'bold'))
        nombreCLabel.pack()
        nombreCLabel.place(x=40, y=180)

        nombreCEntry = tk.Entry(root, font=(fuente,14))
        nombreCEntry.place(x=40, y=220, width=520, height=40)

        codigoLabel = tk.Label(root, text='Código del Curso:', fg=azul, font=(fuente, 20, 'bold'))
        codigoLabel.pack()
        codigoLabel.place(x=40,y=280)

        codigoEntry = tk.Entry(root, font=(fuente,14))
        codigoEntry.place(x=320, y=280, width=240, height=40)

        creditosLabel = tk.Label(root, text='Créditos:', fg=azul, font=(fuente, 20, 'bold'))
        creditosLabel.pack()
        creditosLabel.place(x=40, y=340)

        creditos = [0,1,2,3,4]
        creditosVar = StringVar()

        creditosEntry = tk.OptionMenu(root, creditosVar, *creditos)
        creditosEntry.config(font=(fuente, 16, 'bold'))
        creditosEntry.place(x=320, y=340, width=240, height=40)

        horasLabel = tk.Label(root, text='Horas Lectivas:', fg=azul, font=(fuente, 20, 'bold'))
        horasLabel.pack()
        horasLabel.place(x=40, y=400)

        horas = [1,2,3,4,5,6,7,8,9]
        horasVar = StringVar()

        horasEntry = tk.OptionMenu(root, horasVar, *horas)
        horasEntry.config(font=(fuente, 16, 'bold'))
        horasEntry.place(x=320, y=400, width=240, height=40)

        def limpiarCampos():
            nombreCEntry.delete(0, "end")
            codigoEntry.delete(0, 'end')
            
        botonLC = tk.Button(root, text='Limpiar Campos', borderwidth=1, relief='raised', command=limpiarCampos)
        botonLC.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonLC.pack()
        botonLC.place(x=350, y=480, width=200)

        def checkCurso(nombreCurso):
            nombreCurso = nombreCEntry.get().strip()
            var = [(nombreCurso)]
            select_query = "SELECT nombreCurso FROM curso WHERE nombreCurso = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            if user is not None:
                return True
            else:
                return False

        def checkCodigo(codCurso):
            codCurso = codigoEntry.get().strip()
            var = [(codCurso)]
            select_query = "SELECT codigoCurso FROM curso WHERE codigoCurso = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            if user is not None:
                return True
            else:
                return False

        def registroCurso():
            nombreCurso = nombreCEntry.get().strip()
            codEscuela = codigoEscuela.get().strip()
            codCurso = codigoEntry.get().strip()
            creditos = creditosVar.get().strip()
            horas = horasVar.get().strip()
            codigo = codEscuela.upper() + codCurso
            nombreVar = nombreCurso.replace(' ', '')
            
            if nombreVar != '' and codEscuela != '' and codCurso != '' and creditos != '' and horas != '':
                if nombreVar.isalpha() == True and codEscuela.isalpha() == True:
                    if len(nombreCurso) > 0 and len(codCurso) == 4 and codCurso.isalpha() == False:
                        if checkCurso(nombreCurso) == False and checkCodigo(codCurso) == False:
                            vals = (nombreCurso, codEscuela.upper(), codEscuela.upper(), codigo, creditos, horas)
                            insert_query = "INSERT INTO curso SET nombreCurso = %s, nombreEscuela = (select nombreEscuela from escuela where codigoEscuela = %s), codigoEscuela = %s, codigoCurso = %s, creditos = %s, horas = %s"
                            c.execute(insert_query, vals)
                            connection.commit()
                            messagebox.showinfo('Registrado','El curso ha sido registrado')
                        else:
                            messagebox.showwarning('Error', 'El curso o el código ya existe, elija otro')
                    else:
                        messagebox.showwarning('Espacios vacíos','Por favor llenar todos los espacios\nO asignar un Código de 4 números')
                else:
                    messagebox.showwarning('Error', 'El nombre del curso y el código de la escuela deben ser LETRAS')
            else:
                messagebox.showwarning('Error', 'Debe llenar todos los espacios')

        botonR = tk.Button(root, text='REGISTRAR', borderwidth=1, relief='raised')
        botonR.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonR.pack()
        botonR.place(x=40, y=480, width=300)
        botonR['command']=registroCurso

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

def asignarRC():
    if rol == '1':
        root = tk.Toplevel()
        w = 600
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Asignar Requisitos y/o Correquisitos', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=20, y=15)

        nombreLabel = tk.Label(root, text='Nombre Escuela:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=40, y=90)

        escuela = 'select nombreEscuela from escuela'
        c.execute(escuela)
        varE = c.fetchall()

        opciones = varE
        opcionesVar = tk.StringVar()

        nombreEntry = tk.OptionMenu(root, opcionesVar, *opciones)
        nombreEntry.config(font=(fuente, 16, 'bold'))
        nombreEntry.place(x=40, y=130, width=520, height=40)

        codigoLabel = tk.Label(root, text='Código del Curso:', fg=azul, font=(fuente, 20, 'bold'))
        codigoLabel.pack()
        codigoLabel.place(x=40,y=200)

        codigoEntry = tk.Entry(root, font=(fuente,14))
        codigoEntry.place(x=320, y=200, width=240, height=40)

        reqLabel = tk.Label(root, text='Requisito:', fg=azul, font=(fuente, 20, 'bold'))
        reqLabel.pack()
        reqLabel.place(x=40, y=260)

        codReq = tk.Label(root, text='Código del Curso:', fg=azul, font=(fuente, 18, 'bold'))
        codReq.pack()
        codReq.place(x=40, y=340)

        codigoR = 'select codigoCurso from curso'
        c.execute(codigoR)
        varR = c.fetchall()
        opcionesR = varR
        opcionesVarR = tk.StringVar()

        codREntry = tk.OptionMenu(root, opcionesVarR, *opcionesR)
        codREntry.config(font=(fuente, 16, 'bold'))
        codREntry.place(x=40, y=400, width=240, height=40)

        corrLabel = tk.Label(root, text='Correquisito:', fg=azul, font=(fuente, 20, 'bold'))
        corrLabel.pack()
        corrLabel.place(x=340, y=260)

        codCorr = tk.Label(root, text='Código del Curso:', fg=azul, font=(fuente, 18, 'bold'))
        codCorr.pack()
        codCorr.place(x=340, y=340)

        codigoC = 'select codigoCurso from curso'
        c.execute(codigoC)
        varC = c.fetchall()
        opcionesC = varC
        opcionesVarC = tk.StringVar()

        codCEntry = tk.OptionMenu(root, opcionesVarC, *opcionesC)
        codCEntry.config(font=(fuente, 16, 'bold'))
        codCEntry.place(x=340, y=400, width=240, height=40)


        def checkRequisito(codCurso, codRequisito):
            codCurso = codigoEntry.get().strip()
            codRequisito = opcionesVarR.get().strip()
            var = (codCurso.upper(), codRequisito)
            select_query = "SELECT codRequisito FROM requisito WHERE codigoCurso = %s and codRequisito != %s"
            c.execute(select_query, var)
            user = c.fetchall()
            x = 0
            asignarReq = codRequisito[2:-3]
            cursoReq = codCurso
            while x < len(user): 
                unionReq = ''.join(user[x])
                concat = cursoReq+asignarReq
                concat2 = cursoReq+unionReq
                while concat != concat2 and x < len(user):
                    unionReq = ''.join(user[x])
                    concat2 = cursoReq+unionReq
                    x += 1
                if concat != concat2:
                    return False
                else:
                    return True
            return False

        def registroRequisito():
            nombreEscuela = opcionesVar.get().strip()
            codCurso = codigoEntry.get().strip()
            codRequisito = opcionesVarR.get().strip()
            escuela = nombreEscuela[2:-3]
            asignarReq = codRequisito[2:-3]
            var = asignarReq 
            
            if escuela != '' and codCurso != '':
                if len(codCurso) == 6:
                    if codCurso != var:
                        if checkRequisito(codCurso, codRequisito) == False:
                            vals = (escuela, codCurso, asignarReq)
                            insert_query = "INSERT INTO requisito SET nombreEscuela = %s, codigoCurso = %s, codRequisito = %s"
                            c.execute(insert_query, vals)
                            connection.commit()
                            messagebox.showinfo('Registrado','El requisito ha sido registrado')
                        else:
                            messagebox.showwarning('Error', 'El requisito ya existe, elija otro')
                    else:
                        messagebox.showwarning('Error', 'El requisito debe ser diferente al código del curso')
                else:
                    messagebox.showwarning('Error', 'El codigo debe ser de longitud 6')
            else:
                 messagebox.showwarning('Error', 'Debe indicar una escuela y un código para \nregistrar un requisito o un correquisito 6')

            
        botonRR = tk.Button(root, text='REGISTRAR', borderwidth=1, relief='raised')
        botonRR.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonRR.pack()
        botonRR.place(x=40, y=480, width=240)
        botonRR['command']=registroRequisito

        def checkCorrequisito(codCurso, codCorrequisito):
            codCurso = codigoEntry.get().strip()
            codCorrequisito = opcionesVarR.get().strip()
            var = (codCurso.upper(), codCorrequisito)
            select_query = "SELECT codCorrequisito FROM correquisito WHERE codigoCurso = %s and codCorrequisito != %s"
            c.execute(select_query, var)
            user = c.fetchall()
            x = 0
            asignarCorreq = codCorrequisito[2:-3]
            cursoCorreq = codCurso
            while x < len(user): 
                unionReq = ''.join(user[x])
                concat = cursoCorreq+asignarCorreq
                concat2 = cursoCorreq+unionReq
                while concat != concat2 and x < len(user):
                    unionReq = ''.join(user[x])
                    concat2 = cursoCorreq+unionReq
                    x += 1
                if concat != concat2:
                    return False
                else:
                    return True
            return False

        def registroCorrequisito():
            nombreEscuela = opcionesVar.get().strip()
            codCurso = codigoEntry.get().strip()
            codCorrequisito = opcionesVarC.get().strip()
            escuela = nombreEscuela[2:-3]
            asignarCorreq = codCorrequisito[2:-3]
            var = asignarCorreq

            if escuela != '' and codCurso != '':
                if len(codCurso) == 6:
                    if codCurso != var:
                        if checkCorrequisito(codCurso, codCorrequisito) == False:
                            vals = (escuela, codCurso, asignarCorreq)
                            insert_query = "INSERT INTO correquisito SET nombreEscuela = %s, codigoCurso = %s, codCorrequisito = %s"
                            c.execute(insert_query, vals)
                            connection.commit()
                            messagebox.showinfo('Registrado','El correquisito ha sido registrado')
                        else:
                            messagebox.showwarning('Error', 'El correquisito ya existe, elija otro')
                    else:
                        messagebox.showwarning('Error', 'El correquisito debe ser diferente al código del curso')
                else:
                    messagebox.showwarning('Error', 'El codigo debe ser de longitud 6')
            else:
                 messagebox.showwarning('Error', 'Debe indicar una escuela y un código para \nregistrar un requisito o un correquisito 6')


        botonRC = tk.Button(root, text='REGISTRAR', borderwidth=1, relief='raised')
        botonRC.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonRC.pack()
        botonRC.place(x=340, y=480, width=240)
        botonRC['command']=registroCorrequisito

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

def registrarPE():
    if rol == '1':
        root = tk.Toplevel()
        root.title('Registrar Plan Estudio')
        w = 600
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Registrar Plan de Estudio', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=120, y=15)

        nombreLabel = tk.Label(root, text='Escuela propietaria del plan:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=40, y=90)

        escuela = 'select nombreEscuela from escuela'
        c.execute(escuela)
        varE = c.fetchall()

        escuela = varE
        escuelaVar = tk.StringVar()

        escuelaEntry = tk.OptionMenu(root, escuelaVar, *escuela)
        escuelaEntry.config(font=(fuente, 16, 'bold'))
        escuelaEntry.place(x=40, y=140, width=520, height=40)

        codigoLabel = tk.Label(root, text='Código del plan:', fg=azul, font=(fuente, 20, 'bold'))
        codigoLabel.pack()
        codigoLabel.place(x=40, y=200)

        codigoEntry = tk.Entry(root, font=(fuente,16))
        codigoEntry.place(x=320, y=200, width=240, height=40)

        vigenciaLabel = tk.Label(root, text='Vigencia del plan:', fg=azul, font=(fuente, 20, 'bold'))
        vigenciaLabel.pack()
        vigenciaLabel.place(x=40, y=260)
        
        vigenciaEntry = tk.Entry(root, font=(fuente,16))
        vigenciaEntry.pack()
        vigenciaEntry.place(x=320, y=260, width=240, height=40)
       
        codigoCurso = tk.Label(root, text='Código del curso que \nforma parte del plan:', fg=azul, font=(fuente, 18, 'bold'), justify='left')
        codigoCurso.pack()
        codigoCurso.place(x=40, y=320)

        codigoCursoEntry = tk.Entry(root, font=(fuente,16))
        codigoCursoEntry.pack()
        codigoCursoEntry.place(x=320, y=330, width=240, height=40)

        bloqueLabel = tk.Label(root, text='Bloque:', fg=azul, font=(fuente, 18, 'bold'))
        bloqueLabel.pack()
        bloqueLabel.place(x=40, y=390)

        bloque = 'select detalleBloque from bloque'
        c.execute(bloque)
        varB = c.fetchall()
        bloque = varB
        bloqueVar = StringVar()

        bloqueEntry = tk.OptionMenu(root, bloqueVar, *bloque)
        bloqueEntry.config(font=(fuente, 20, 'bold'))
        bloqueEntry.place(x=320, y=390, width=240, height=40)

        def checkCodPlan(codPlan):
            codPlan = codigoEntry.get().strip()
            var = [(codPlan)]
            select_query = "SELECT codigoPlan FROM planEstudios WHERE codigoPlan = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            if user is not None:
                return True
            else:
                return False

        def checkCodCurso(codCurso):
            codCurso = codigoCursoEntry.get().strip()
            var = [(codCurso)]
            select_query = "SELECT codigoCurso FROM curso WHERE codigoCurso = %s"
            c.execute(select_query, var)
            user = c.fetchone()
            x = 0
            if user is None:
                return True
            else:
                return False
            

        def registroPlan():
            nombreEscuela = escuelaVar.get().strip()
            codPlan = codigoEntry.get().strip()
            vigencia = vigenciaEntry.get().strip()
            codCurso = codigoCursoEntry.get().strip()
            bloque = bloqueVar.get().strip()
            escuela = nombreEscuela[2:-3]
            bloqueV = bloque[2:-3]
            nombreVar = escuela.replace(' ', '')
            
            if nombreVar != '' and codPlan != '' and vigencia != '' and codCurso != '' and bloque != '':
                if len(codCurso) == 6:
                    if checkCodPlan(codPlan) == False and checkCodCurso(codCurso) == False:
                        vals = (codPlan, escuela, vigencia, codCurso, bloqueV)
                        insert_query = "INSERT INTO planEstudios SET codigoPlan = %s, nombreEscuela = %s, fechaVigencia = %s, codigoCurso = %s, detalleBloque = (select detalleBloque from bloque where detalleBloque = %s)"
                        c.execute(insert_query, vals)
                        connection.commit()
                        messagebox.showinfo('Registrado','El plan de estudio ha sido registrado')
                    else:
                        messagebox.showwarning('Error', 'El plan de estudio ya existe, elija otro')
                else:
                    messagebox.showwarning('Error', 'El codigo debe ser de longitud 6')
            else:
                messagebox.showwarning('Error', 'Debe llenar todos los espacios')
            

        botonR = tk.Button(root, text='REGISTRAR', borderwidth=1, relief='raised')
        botonR.config(bg=azul, font='Cambria 18 bold', fg= fgcolor)
        botonR.pack()
        botonR.place(x=150, y=500, width=300)
        botonR['command']=registroPlan

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

#---------------------------------- Modificaciones ----------------------------------#

def eliminarReq():
    if rol == '1':
        root = tk.Toplevel()
        root.title('Eliminar Requisito')
        w = 600
        h = 400
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Eliminar Requisito', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=160, y=15)

        nombreLabel = tk.Label(root, text='Nombre del curso:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=20, y=140)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=300, y=140, width=280, height=40)

                            
        '''
            def consultarReq
            
        
        '''

        botonCR = tk.Button(root, text='ELIMINAR', borderwidth=1, relief='raised')
        botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCR.pack()
        botonCR.place(x=150, y=280, width=300)

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')


def eliminarCo():
    if rol == '1':
        root = tk.Toplevel()
        root.title('Eliminar Correquisito')
        w = 600
        h = 400
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Eliminar Correquisito', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=140, y=15)

        nombreLabel = tk.Label(root, text='Nombre del curso:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=20, y=140)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=300, y=140, width=280, height=40)

        '''
            def consultarReq
            
        
        '''

        botonCR = tk.Button(root, text='ELIMINAR', borderwidth=1, relief='raised')
        botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCR.pack()
        botonCR.place(x=150, y=280, width=300)

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

def eliminarCurso():
    if rol == '1':
        root = tk.Toplevel()
        root.title('Eliminar Curso')
        w = 600
        h = 400
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Eliminar Curso', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=200, y=15)

        nombreLabel = tk.Label(root, text='Nombre del curso:', fg=azul, font=(fuente, 20, 'bold'))
        nombreLabel.pack()
        nombreLabel.place(x=20, y=140)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=300, y=140, width=280, height=40)

        def limpiarCampos():
                nombreEntry.delete(0, "end")

                            
        '''
            def consultarReq
            
        
        '''

        botonCR = tk.Button(root, text='ELIMINAR', borderwidth=1, relief='raised')
        botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCR.pack()
        botonCR.place(x=150, y=280, width=300)

    else: 
        messagebox.showwarning('Error', 'Solo el Admin puede realizar esta función')

#---------------------------------- Rol de Consultor ----------------------------------#

def consultarPlan():
    if rol == '2':
        root = tk.Toplevel()
        root.title('Consultar Plan Estudio')
        w = 1000
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Consultar Plan de Estudio', bg=azul, fg=fgcolor, font=(fuente, 24))
        labelFrame.pack()
        labelFrame.place(x=320, y=15)

        escuelaLabel = tk.Label(root, text='Escuela propietaria del plan:', fg=azul, font=(fuente, 20, 'bold'))
        escuelaLabel.pack()
        escuelaLabel.place(x=20, y=80)

        escuela = 'select nombreEscuela from escuela'
        c.execute(escuela)
        varE = c.fetchall()

        opciones = varE
        opcionesVar = tk.StringVar()

        escuelaEntry = tk.OptionMenu(root, opcionesVar, *opciones)
        escuelaEntry.config(font=(fuente, 16, 'bold'))
        escuelaEntry.place(x=450, y=80, width=480, height=40)

        codigoLabel = tk.Label(root, text='Código Plan de Estudios:', fg=azul, font=(fuente, 20, 'bold'))
        codigoLabel.pack()
        codigoLabel.place(x=20, y=150)

        codigoEntry = tk.Entry(root, font=(fuente,16))
        codigoEntry.place(x=400, y=150, width=150, height=40)

        vigenciaLabel = tk.Label(root, text = 'Vigencia:', fg = azul, font = (fuente, 20, 'bold'))
        vigenciaLabel.pack()
        vigenciaLabel.place(x = 600, y = 150)

        vigenciaEntry = tk.Entry(root, font=(fuente,14))
        vigenciaEntry.place(x=765, y=150, width=160, height=40)

        
        #buscar como cambiar el tamaño de las columnas 
        tree = ttk.Treeview(root, columns=('Nombre', 'Fecha', 'Curso', 'Bloque'))
        tree['show']='headings'
        tree.pack()
        tree.place(x=50, y=200, width=900, height=250)

        tree.heading('#1', text='Nombre Escuela')
        tree.heading('#2', text='Fecha Vigencia')
        tree.heading('#3', text='Curso')
        tree.heading('#4', text='Bloque')

        def consultaPE():
            codigo = codigoEntry.get().strip()
            val = [(codigo)]
            select_query = ('Select nombreEscuela, fechaVigencia, codigoCurso, detalleBloque from planEstudios where codigoPlan = %s')
            c.execute(select_query, val)
            user = c.fetchall()

            for ro in user:
                tree.insert('',END, text="",values=(ro[0],ro[1],ro[2],ro[3]))
           
        botonCPE = tk.Button(root, text='CONSULTAR', borderwidth=1, relief='raised')
        botonCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCPE.pack()
        botonCPE.place(x=300, y=500, width=300)
        botonCPE['command']=consultaPE

    else: 
         messagebox.showwarning('Error', 'Solo el Consultor puede realizar esta función')


def consultarCurso():
    if rol == '2':
        root = tk.Toplevel()
        root.title('Consultar Curso')
        w = 1000
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Consultar Curso', bg=azul, fg=fgcolor, font=(fuente, 30))
        labelFrame.pack()
        labelFrame.place(x=350, y=10)

        nombreLabel = tk.Label(root, text='Nombre:', fg=azul, font=(fuente, 20, 'bold'), justify='left')
        nombreLabel.pack()
        nombreLabel.place(x=40, y=100)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=180, y=106, width=280, height=30)

        planLabel = tk.Label(root, text='Plan al que pertenece:', fg=azul, font=(fuente, 20, 'bold'))
        planLabel.pack()
        planLabel.place(x=500, y=100)

        planEntry = tk.Entry(root, font=(fuente,14))
        planEntry.place(x=840, y=106, width=106, height=30)
        
        tree = ttk.Treeview(root, columns=('Codigo','Requisitos','Correquisitos','Horas','Creditos'))
        tree.pack()
        tree.place(x=50, y=200, width=900, height=250)

        tree.heading('#0', text='Código ')
        tree.heading('#1', text='Nombre del curso')
        tree.heading('#2', text='Bloque')
        tree.heading('#3', text='Horas del curso')
        tree.heading('#4', text='Creditos')
        
        '''        
        def consCurso:
            vigencia = vigenciaEntry.get().strip()
            codigo = codigoEntry.get().strip()
            
            tree.insert('', END, text='Ale', values=(vigencia, codigo))
            tree.insert('', END, text='Iris', values=('45', '78'))'''
            

        botonCCPE = tk.Button(root, text='CONSULTAR', borderwidth=1, relief='raised')
        botonCCPE.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCCPE.pack()
        botonCCPE.place(x=350, y=500, width=300)

    else: 
         messagebox.showwarning('Error', 'Solo el Consultor puede realizar esta función')


def consultarReq():
    if rol == '2':
        root = tk.Toplevel()
        root.title('Consultar Requisitos')
        w = 800
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Consultar Requisito', bg=azul, fg=fgcolor, font=(fuente, 30))
        labelFrame.pack()
        labelFrame.place(x=220, y=10)

        nombreLabel = tk.Label(root, text='Curso:', fg=azul, font=(fuente, 20, 'bold'), justify='left')
        nombreLabel.pack()
        nombreLabel.place(x=40, y=100)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=180, y=106, width=280, height=30)
        
        tree = ttk.Treeview(root, columns=('Curso','Codigo','Requisitos'))
        tree.pack()
        tree.place(x=50, y=200, width=700, height=250)

        tree.heading('#0', text='Nombre del curso')
        tree.heading('#1', text='Código Requisito')
        tree.heading('#2', text='Requisitos')
        
        '''        
        def consCurso:
            vigencia = vigenciaEntry.get().strip()
            codigo = codigoEntry.get().strip()
            
            tree.insert('', END, text='Ale', values=(vigencia, codigo))
            tree.insert('', END, text='Iris', values=('45', '78'))'''


        botonCR = tk.Button(root, text='CONSULTAR', borderwidth=1, relief='raised')
        botonCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCR.pack()
        botonCR.place(x=550, y=102, width=200)

    else: 
         messagebox.showwarning('Error', 'Solo el Consultor puede realizar esta función')


def consultarCo():
     if rol == '2':
        root = tk.Toplevel()
        root.title('Consultar Correquisitos')
        w = 800
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(0,0)
        headerFrame = tk.Frame(root, bg='#001b2e', width=w, height=70)
        headerFrame.pack()

        labelFrame = tk.Label(headerFrame, text='Consultar Correquisitos', bg=azul, fg=fgcolor, font=(fuente, 30))
        labelFrame.pack()
        labelFrame.place(x=200, y=15)

        nombreLabel = tk.Label(root, text='Curso:', fg=azul, font=(fuente, 20, 'bold'), justify='left')
        nombreLabel.pack()
        nombreLabel.place(x=40, y=100)

        nombreEntry = tk.Entry(root, font=(fuente,14))
        nombreEntry.place(x=180, y=106, width=280, height=30)
        
        tree = ttk.Treeview(root, columns=('Curso','Codigo','Correquisitos'))
        tree.pack()
        tree.place(x=50, y=200, width=700, height=250)

        tree.heading('#0', text='Nombre del curso')
        tree.heading('#1', text='Código Correquisito')
        tree.heading('#2', text='Correquisitos')


        '''
        def consCurso:
            vigencia = vigenciaEntry.get().strip()
            codigo = codigoEntry.get().strip()
            
            tree.insert('', END, text='Ale', values=(vigencia, codigo))
            tree.insert('', END, text='Iris', values=('45', '78'))'''

        botonCCR = tk.Button(root, text='CONSULTAR', borderwidth=1, relief='raised')
        botonCCR.config(bg=azul, font='Cambria 16 bold', fg= fgcolor)
        botonCCR.pack()
        botonCCR.place(x=150, y=280, width=300)

     else: 
         messagebox.showwarning('Error', 'Solo el Consultor puede realizar esta función')


#---------------------------------------------------Final---------------------------------------------------#
root.mainloop()
