from tkinter import *
from Pacientes import Paciente 
from videoManager import *

ventana =  Tk()
ventana.title("Análisis Biomecánico")
ventana.geometry("500x500")
ventanaPaciente = Frame(ventana)
ventanaAnalisis = Frame(ventana)
ventanaPrincipal = Frame(ventana) 
ventanaOpcionVideo = Frame(ventana)
ventanaCargarVideo = Frame(ventana)
ventanaWebcam = Frame(ventana)
ventanaInfPaciente = Frame(ventana)

paciente = Paciente() 
#Restricciones--------------------------------------------------------
def validate_entry(text, new_text, digits):
    digits = int(digits)
    if len(new_text) > digits:
        return False
    return text.isdecimal()

def validate_entry_char(text):
    caracteres_baneados = "!#$%&/()=?¡¨*][_:>°1234567890'¿´+}{.-,<*-+°¬\~^`}´´¿´}]|"
    if text in caracteres_baneados or text == '"':
        return False
    return True
def textoDelCuadro():
    global sexo, paciente
    mandar = (cuadroNombre.get(), cuadroApellidos.get(), cuadroEdad.get(), cuadroPeso.get(), cuadroAltura.get(), sexo)
    paciente.set_personal_data(cuadroNombre.get(), cuadroApellidos.get(),'Rockhopper', int(cuadroEdad.get()), int(cuadroPeso.get()), int(cuadroAltura.get()), sexo)
    aux_flag = True
    print(mandar)
    for elemento in mandar:
        if len(elemento) < 1:
            aux_flag = False
            break
    if aux_flag:
        ventana.title("Tipo de analisis del paciente")
        ventanaAnalisis.pack(fill='both', expand=1)
        ventanaPaciente.pack_forget()
    else:
        return
# boton1 = Button(ventanaCargarVideo, text = "Elegir y Visualizar video", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
# boton1.grid(column = 0, row = 0, columnspan=2)    
##Widgets de la ventana webcam------------------------------------------
def CambiarVentanaWebcam():
    ventana.title("Grabar video")
    ventana.geometry("640x500")
    ventanaWebcam.pack(fill='both', expand=1)
    ventanaOpcionVideo.pack_forget()


btnIniciar = Button(ventanaWebcam, text="Iniciar", width=45, command = lambda: iniciar(LabelVideoWebcam))
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(ventanaWebcam, text="Finalizar", width=45, command = lambda: finalizar() )
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

LabelVideoWebcam = Label(ventanaWebcam)
LabelVideoWebcam.grid(column=0, row=1, columnspan=2)

# boton1 = Button(ventanaWebcam, text = "Iniciar grabacion", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
# boton1.grid(column = 0, row = 0, columnspan=2)
##Widgets de la ventana video------------------------------------------
def CambiarVentanaVideo():
    ventana.title("Cargar Video")
    ventana.geometry("640x500")
    ventanaCargarVideo.pack(fill='both', expand=1)
    ventanaOpcionVideo.pack_forget()

Label1 = Label(ventanaCargarVideo, text = "Video de entrada:")
Label1.grid(column = 0, row= 1)

LabelInfoVideoPath = Label(ventanaCargarVideo, text = "Aun no se ha seleccionado un video")
LabelInfoVideoPath.grid(column = 1, row = 1)

LabelVideo = Label(ventanaCargarVideo)
LabelVideo.grid(column = 0, row = 2, columnspan=2)

boton1 = Button(ventanaCargarVideo, text = "Elegir y Visualizar video", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
boton1.grid(column = 0, row = 0, columnspan=2)
##Widgets de la ventana opcion video------------------------------------------
def CambiarVentanaOpcionVideo():
    ventana.title("Elegir opcion de video")
    ventanaOpcionVideo.pack(fill='both', expand=1)
    ventanaAnalisis.pack_forget()
boton8 =  Button(ventanaOpcionVideo, text = "Seleccionar Video", width = 20, height = 5, command = CambiarVentanaVideo)
boton9 =  Button(ventanaOpcionVideo, text = "Utilizar Webcam", width = 20, height = 5, command = CambiarVentanaWebcam)
boton8.place(x = 180, y = 100)
boton9.place(x = 180, y = 250)
##Widgets de la ventana analisis------------------------------------------
def CambiarVentanaAnalisis():
    ventana.title("Tipo de analisis del paciente")
    ventanaAnalisis.pack(fill='both', expand=1)
    ventanaPaciente.pack_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()
# boton5 =  Button(ventanaAnalisis, text = "Análsis antropométrico", width = 20, height = 5)
boton6 =  Button(ventanaAnalisis, text = "Análisis de ángulos", width = 20, height = 5, command = CambiarVentanaOpcionVideo)
# boton7 =  Button(ventanaAnalisis, text = "Siguiente", width = 10, height = 5, command = CambiarVentanaOpcionVideo)
# boton5.place(x = 180, y = 100)
boton6.place(x = 180, y = 150)
# boton7.place(x = 400, y = 350)
##Widgets de la ventana nuevo paciente-------------------------------------
def CambiarVentanaPaciente():
    ventana.title("Hoja de datos del paciente")
    ventanaPaciente.pack(fill='both', expand=1)
    ventanaPrincipal.pack_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()
NombreEtiqueta =  Label(ventanaPaciente, text = "Nombre:")
NombreEtiqueta.grid(row =0, column = 0)
ApellidoEtiqueta =  Label(ventanaPaciente, text = "Apellido:")    
ApellidoEtiqueta.grid(row =1, column = 0)
EdadEtiqueta =  Label(ventanaPaciente, text = "Edad:")    #solo admitira 2 numeros  
EdadEtiqueta.grid(row =2, column = 0)
AñosEtiqueta = Label(ventanaPaciente, text = "años")
AñosEtiqueta.grid(row =2, column = 2)
PesoEtiqueta =  Label(ventanaPaciente, text = "Peso:")    #solo admitira 3 numeros 
PesoEtiqueta.grid(row =3, column = 0)
KgEtiqueta =  Label(ventanaPaciente, text = " kg")
KgEtiqueta.grid(row =3, column = 2)
AlturaEtiqueta =  Label(ventanaPaciente, text = "Altura:")  #valor en centimetros
AlturaEtiqueta.grid(row =4, column = 0)
CmEtiqueta =  Label(ventanaPaciente, text = "cm")
CmEtiqueta.grid(row =4, column = 2)
SexoEtiqueta =  Label(ventanaPaciente, text = "Sexo:")   #solo permitira seleccionar 1 parametro de dos 
SexoEtiqueta.grid(row=5, column=0, rowspan=2)

l = Label(ventanaPaciente, bg='white', width=20, text='Vacio')
l.grid(row=7, column = 0)

sexo = ""
def print_selectionMasculino():
    global sexo
    sexo = 'Masculino'
    varFemenino.set(0)
    l.config(text=sexo)
    return sexo

def print_selectionFemenino():
    global sexo
    sexo = 'Femenino'
    varMasculino.set(0)
    l.config(text=sexo) 
    return sexo

varMasculino = IntVar()
varFemenino = IntVar()
checkMasculino = Checkbutton(ventanaPaciente, text='Masculino',variable=varMasculino, onvalue=1, offvalue=0, command=print_selectionMasculino)
checkMasculino.grid(row =5, column = 1)
checkFemenino = Checkbutton(ventanaPaciente, text='Femenino',variable=varFemenino, onvalue=1, offvalue=0, command=print_selectionFemenino)
checkFemenino.grid(row =6, column = 1)
 
###Entry's-----------------------------------------
cuadroNombre =  Entry(ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry_char), "%S" )
)
cuadroNombre.grid(row =0, column = 1)
cuadroApellidos = Entry(ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry_char), "%S" )
)
cuadroApellidos.grid(row =1, column = 1)
cuadroEdad =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroEdad.grid(row =2, column = 1)
cuadroPeso =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroPeso.grid(row =3, column = 1)
cuadroAltura =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroAltura.grid(row =4, column = 1)

boton3 =  Button(ventanaPaciente, text = "Enviar", command = textoDelCuadro)
#boton4 =  Button(ventanaPaciente, text = "Siguiente", width = 20, height = 5, command = CambiarVentanaAnalisis)
boton3.place(x = 250, y =150)
#boton4.place(x = 250, y = 350)
##Widgets de la primera ventana-------------------------------------------
def CambiarVentanaPrincipal():
    ventana.title("Bienvenido al sistema JJJ")
    ventana.geometry("500x500")
    ventanaPrincipal.pack(fill='both', expand=1)
    ventanaInfPaciente.pack_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()
def CambiarInfPaciente():
    ventana.title("Cargar Video")
    ventana.geometry("640x500")
    ventanaInfPaciente.pack(fill='both', expand=1)
    ventanaPrincipal.pack_forget()
    iniciarMostrar(LabelVideo3, 'videos_out/video_prueba56.avi')
boton1 =  Button(ventanaPrincipal, text = "Nuevo paciente", width = 20, height = 5, command = CambiarVentanaPaciente)
boton2 =  Button(ventanaPrincipal, text = "Ver informe del paciente", width = 20, height = 5, command = CambiarInfPaciente)
boton1.place(x = 180, y = 100)
boton2.place(x = 180, y = 250)
##Widgets de la ventana info paciente------------------------------------------
LabelInf1 = Label(ventanaInfPaciente, text = "Video de entrada:")
LabelInf1.grid(column = 1, row= 0)

NombreEtiqueta =  Label(ventanaInfPaciente, text = "Nombre: Juan Jose")
NombreEtiqueta.grid(row =0, column = 0)
ApellidoEtiqueta =  Label(ventanaInfPaciente, text = "Apellido: Anchoa")    
ApellidoEtiqueta.grid(row =1, column = 0)

LabelInfoVideoPath2 = Label(ventanaInfPaciente, text = "Mostrar datos del paciente")
LabelInfoVideoPath2.grid(column = 1, row = 1)

LabelVideo3 = Label(ventanaInfPaciente)
LabelVideo3.grid(column = 0, row = 2, columnspan=2)

btnRegresar = Button(ventanaInfPaciente, text="Volver", width=45, command = CambiarVentanaPrincipal)
btnRegresar.grid(column = 0, row=3, columnspan = 2, padx=5, pady=5)
#-----------------------main def--------------------------------------
CambiarVentanaPrincipal()
# CambiarInfPaciente() 

ventana.mainloop()
