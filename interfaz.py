from tkinter import *
# import customtkinter
import pacients 
# from videoManager import *
import videoManager
import angles

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
ventanaSelectInfPaciente = Frame(ventana)

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
    global sexo
    mandar = (cuadroNombre.get(), cuadroApellidos.get(), cuadroEdad.get(), cuadroPeso.get(), cuadroAltura.get(), sexo)
    aux_flag = True
    print(mandar)
    for elemento in mandar:
        if len(elemento) < 1:
            aux_flag = False
            break
    if aux_flag:
        pacients.set_personal_data(cuadroNombre.get(), cuadroApellidos.get(),cuadroBicicleta.get(), int(cuadroEdad.get()), int(cuadroPeso.get()), int(cuadroAltura.get()), sexo)
        ventana.title("Tipo de analisis del paciente")
        ventanaAnalisis.pack(fill='both', expand=1)
        ventanaPaciente.pack_forget()
    else:
        return
##Funciones para cambiar de pantalla
def CambiarVentanaSelectInfPaciente():
    ventana.title("Seleccione paciente")
    ventana.geometry("640x500")
    ventanaSelectInfPaciente.pack(fill='both', expand=1)
    ventanaPrincipal.pack_forget()
def CambiarVentanaWebcam():
    ventana.title("Grabar video")
    ventana.geometry("640x500")
    ventanaWebcam.pack(fill='both', expand=1)
    ventanaOpcionVideo.pack_forget()

def CambiarVentanaVideo():
    ventana.title("Cargar Video")
    ventana.geometry("640x500")
    ventanaCargarVideo.pack(fill='both', expand=1)
    ventanaOpcionVideo.pack_forget()
    ventanaInfPaciente.pack_forget()

def CambiarVentanaOpcionVideo():
    ventana.title("Elegir opcion de video")
    ventanaOpcionVideo.pack(fill='both', expand=1)
    ventanaAnalisis.pack_forget()

def CambiarVentanaAnalisis():
    ventana.title("Tipo de analisis del paciente")
    ventanaAnalisis.pack(fill='both', expand=1)
    ventanaPaciente.pack_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()

def CambiarVentanaPaciente():
    ventana.title("Hoja de datos del paciente")
    ventanaPaciente.pack(fill='both', expand=1)
    ventanaPrincipal.pack_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()

def CambiarVentanaPrincipal():
    ventana.title("Bienvenido al sistema JJJ")
    ventana.geometry("500x500")
    ventanaPrincipal.pack(fill='both', expand=1)
    ventanaInfPaciente.pack_forget()
    # boton2.place_forget()
    #order.pack_forget() para todas las demas ventanas hay que borrarlas con pack_forget()

def CambiarInfPaciente(Id_paciente):
    global datos_paciente
    ventana.title("Cargar Video")
    ventana.geometry("1080x550")
    ventanaInfPaciente.pack(fill='both', expand=1)
    ventanaPrincipal.pack_forget()
    ventanaCargarVideo.pack_forget()
    datos_paciente = pacients.get_pacient_data(Id_paciente)
    ActualizarTextosInforme()
def VerificarIdValido():
    if entradaIdPaciente.get() != '':
        id = int(entradaIdPaciente.get())
        try:
            pacients.get_pacient_data(id)
        except:
            mensajeErrorTexto.configure(text='No hay paciente con ese ID!!', fg='red')
        else:
            CambiarInfPaciente(id) 
    else:
        mensajeErrorTexto.configure(text='El campo ID esta vacio!!', fg='red')
def ActualizarTextosInforme():
    #muestra el video en el labelvideo3
    videoManager.iniciarMostrar(LabelVideo3, datos_paciente['url_video'])
    #muestra las imagenes en las etiquetas correspondientes
    videoManager.visualizarImagen(etiquetaImagenMax, datos_paciente['url_img_max'])
    videoManager.visualizarImagen(etiquetaImagenMin, datos_paciente['url_img_min'])
    #Actualiza las etiquetas de informacion
    IdEtiqueta.configure(text = f"ID: {datos_paciente['id']}")
    NombreEtiqueta.configure(text = f"Nombre: {datos_paciente['name']}")
    ApellidoEtiqueta.configure(text = f"Apellido: {datos_paciente['last_name']}")
    EdadEtiqueta.configure(text = f"Edad: {datos_paciente['age']} años")
    AlturaEtiqueta.configure(text = f"Altura: {datos_paciente['height']} cm")
    RodillaEtiqueta.configure(text = f"Rodilla: {datos_paciente['knee_min']} - {datos_paciente['knee_max']}") 
    CaderaEtiqueta.configure(text = f"Cadera: {datos_paciente['hip_min']} - {datos_paciente['hip_max']}")  
    HombroEtiqueta.configure(text = f"Hombro promedio: {datos_paciente['shoulder_avg']} ")  
    etiquetaAjusteRecomendado.configure(text = angles.ProcessAngles(datos_paciente['knee_min'], datos_paciente['knee_max'])) 
    TrasCaderaEtiqueta.configure(text = f"Traslacion de cadera:\n Vertical: {datos_paciente['hip_traslation_x']}  Horizontal:   {datos_paciente['hip_traslation_y']}  ")
def GuardarDatos():
    #Llama a pacients para que guarde los datos en la db 
    #Actualiza el labbel de guardado
    try:
        savedLabbel.configure(text = 'Ha ocurrido un error, no se han generado datos correctamente')
        if pacients.save_data():
            savedLabbel.configure(text = 'Los datos han sido guardados correctamente')
            saveButton.grid(column = 2, row = 3, pady = 5)       
    except:
        savedLabbel.configure(text = 'Ha ocurrido un error, porfavor reinicie')
def EjecutarAnalisisDenuevo():
    savedLabbel.configure(text='')
    saveButton.grid_forget()
    pacients.set_personal_data(datos_paciente['name'], datos_paciente['last_name'],datos_paciente['bike'], datos_paciente['age'], datos_paciente['weigth'], datos_paciente['height'], datos_paciente['gender'])
    CambiarVentanaVideo()
def finalizarGrabacion():
    videoManager.finalizar()
    pacients.save_data()

##Widgets de cada pantalla-------------------------------------------------------
##Widgets de la Ventana principal+-------------------------------------------
boton1 =  Button(ventanaPrincipal, text = "Nuevo paciente", width = 20, height = 5, command = CambiarVentanaPaciente)
mensajeErrorTexto = Label(ventanaPrincipal, text='', font=("Arial", 12))
mensajeErrorTexto.grid(row = 3, column=0, columnspan = 2, pady = 5)
entradaTexto = Label(ventanaPrincipal, text='Ingrese ID del paciente')
entradaTexto.grid(row = 1, column = 0)
entradaIdPaciente =  Entry(
    ventanaPrincipal,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
entradaIdPaciente.grid(row=2, column=0)
boton2 =  Button(ventanaPrincipal, text = "Ver informe del paciente", width = 20, height = 5, command = VerificarIdValido)
boton1.grid(row=0, column=0,columnspan=2,padx=170, pady=50)
boton2.grid(row=1, column=1, rowspan = 2)
##Widgets de la ventana webcam------------------------------------------
btnIniciar = Button(ventanaWebcam, text="Iniciar", width=45, command = lambda: videoManager.iniciarMostrar(LabelVideoWebcam, 0))
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(ventanaWebcam, text="Finalizar", width=45, command = finalizarGrabacion )
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

btnIniciar = Button(ventanaWebcam, text="Iniciar Grabacion", width=45, command = lambda: videoManager.iniciar(LabelVideoWebcam))
btnIniciar.grid(column=0, row=1, padx=5, pady=5, columnspan = 2)

LabelVideoWebcam = Label(ventanaWebcam)
LabelVideoWebcam.grid(column=0, row=2, columnspan=2)

savedLabbelCam = Label(ventanaWebcam, text='')
savedLabbelCam.grid(column = 0, row = 3, pady = 5, padx=5)

# boton1 = Button(ventanaWebcam, text = "Iniciar grabacion", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
# boton1.grid(column = 0, row = 0, columnspan=2)

##Widgets de la ventana video------------------------------------------
Label1 = Label(ventanaCargarVideo, text = "Video de entrada:")
Label1.grid(column = 0, row= 1)

LabelInfoVideoPath = Label(ventanaCargarVideo, text = "Aun no se ha seleccionado un video")
LabelInfoVideoPath.grid(column = 1, row = 1)

LabelVideo = Label(ventanaCargarVideo)
LabelVideo.grid(column = 0, row = 2, columnspan=2)

saveButton = Button(ventanaCargarVideo, text = 'Guardar', command = GuardarDatos)
saveButton.grid(column = 0, row = 3, pady = 5)

saveButton = Button(ventanaCargarVideo, text = 'Informe', command = lambda: CambiarInfPaciente(pacients.get_id()) )


savedLabbel = Label(ventanaCargarVideo, text='')
savedLabbel.grid(column = 1, row = 3, pady = 5, padx=5)

boton1 = Button(ventanaCargarVideo, text = "Elegir y Visualizar video", width = 20, height = 5, command = lambda: videoManager.visualizarVideo(LabelVideo, LabelInfoVideoPath))
boton1.grid(column = 0, row = 0, columnspan=2)

##Widgets de la ventana opcion video------------------------------------------

boton8 =  Button(ventanaOpcionVideo, text = "Seleccionar Video", width = 20, height = 5, command = CambiarVentanaVideo)
boton9 =  Button(ventanaOpcionVideo, text = "Utilizar Webcam", width = 20, height = 5, command = CambiarVentanaWebcam)
boton8.grid(row=0, column=0,padx=170, pady=50)
boton9.grid(row=1, column=0,padx=170, pady=50)

##Widgets de la ventana analisis------------------------------------------

# boton5 =  Button(ventanaAnalisis, text = "Análsis antropométrico", width = 20, height = 5)
boton6 =  Button(ventanaAnalisis, text = "Análisis de ángulos", width = 20, height = 5, command = CambiarVentanaOpcionVideo)
# boton7 =  Button(ventanaAnalisis, text = "Siguiente", width = 10, height = 5, command = CambiarVentanaOpcionVideo)
# boton5.place(x = 180, y = 100)
boton6.place(x = 180, y = 150)
# boton7.place(x = 400, y = 350)

##Widgets de la ventana nuevo paciente-------------------------------------
NombreEtiqueta =  Label(ventanaPaciente, text = "Nombre:")
NombreEtiqueta.grid(row =0, column = 0)
ApellidoEtiqueta =  Label(ventanaPaciente, text = "Apellido:")    
ApellidoEtiqueta.grid(row =1, column = 0)
BicicletaEtiqueta =  Label(ventanaPaciente, text = "Bicicleta:")    
BicicletaEtiqueta.grid(row = 2, column = 0)
EdadEtiqueta =  Label(ventanaPaciente, text = "Edad:")    #solo admitira 2 numeros  
EdadEtiqueta.grid(row =3, column = 0)
AñosEtiqueta = Label(ventanaPaciente, text = "años")
AñosEtiqueta.grid(row =3, column = 2)
PesoEtiqueta =  Label(ventanaPaciente, text = "Peso:")    #solo admitira 3 numeros 
PesoEtiqueta.grid(row =4, column = 0)
KgEtiqueta =  Label(ventanaPaciente, text = " kg")
KgEtiqueta.grid(row =4, column = 2)
AlturaEtiqueta =  Label(ventanaPaciente, text = "Altura:")  #valor en centimetros
AlturaEtiqueta.grid(row =5, column = 0)
CmEtiqueta =  Label(ventanaPaciente, text = "cm")
CmEtiqueta.grid(row =5, column = 2)
SexoEtiqueta =  Label(ventanaPaciente, text = "Sexo:")   #solo permitira seleccionar 1 parametro de dos 
SexoEtiqueta.grid(row=6, column=0, rowspan=2)

labelSexo = Label(ventanaPaciente, bg='red', width=20, text='Vacio')
labelSexo.grid(row=8, column = 0)

sexo = ""
def print_selectionMasculino():
    global sexo
    sexo = 'Masculino'
    varFemenino.set(0)
    labelSexo.config(text=sexo, bg='white')
    return sexo

def print_selectionFemenino():
    global sexo
    sexo = 'Femenino'
    varMasculino.set(0)
    labelSexo.config(text=sexo, bg='white') 
    return sexo

varMasculino = IntVar()
varFemenino = IntVar()
checkMasculino = Checkbutton(ventanaPaciente, text='Masculino',variable=varMasculino, onvalue=1, offvalue=0, command=print_selectionMasculino)
checkMasculino.grid(row =6, column = 1)
checkFemenino = Checkbutton(ventanaPaciente, text='Femenino',variable=varFemenino, onvalue=1, offvalue=0, command=print_selectionFemenino)
checkFemenino.grid(row =7, column = 1)
 
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
cuadroBicicleta = Entry(ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry_char), "%S" )
)
cuadroBicicleta.grid(row =2, column = 1)
cuadroEdad =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroEdad.grid(row =3, column = 1)
cuadroPeso =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroPeso.grid(row =4, column = 1)
cuadroAltura =  Entry(
    ventanaPaciente,
    validate="key",
    validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
)
cuadroAltura.grid(row =5, column = 1)

boton3 =  Button(ventanaPaciente, text = "Enviar", command = textoDelCuadro)
#boton4 =  Button(ventanaPaciente, text = "Siguiente", width = 20, height = 5, command = CambiarVentanaAnalisis)
boton3.place(x = 250, y =150)
#boton4.place(x = 250, y = 350)
##Widgets de la ventana info paciente------------------------------------------
LabelInf1 = Label(ventanaInfPaciente, text = "Datos de paciente", font=("Arial", 18))
LabelInf1.grid(column = 0, row= 0, padx=10)
LabelInf2 = Label(ventanaInfPaciente, text = "Datos goniometricos", font=("Arial", 18), padx=200, pady=5)
LabelInf2.grid(column = 1, row= 0, columnspan=3)

IdEtiqueta =  Label(ventanaInfPaciente, text = "ID: " )
IdEtiqueta.grid(row = 1, column = 0, padx=5)
NombreEtiqueta =  Label(ventanaInfPaciente, text = "Nombre:")
NombreEtiqueta.grid(row = 2, column = 0, padx=5)
ApellidoEtiqueta =  Label(ventanaInfPaciente, text = "Apellido" )    
ApellidoEtiqueta.grid(row = 3, column = 0, padx=5)
EdadEtiqueta =  Label(ventanaInfPaciente, text = "Edad:")    #solo admitira 2 numeros  
EdadEtiqueta.grid(row = 4, column = 0, padx=5)
AlturaEtiqueta =  Label(ventanaInfPaciente, text = "Altura:")    #solo admitira 2 numeros  
AlturaEtiqueta.grid(row = 5, column = 0, padx=5)
etiquetaAjuste = Label(ventanaInfPaciente, text = "Ajustes", bg='red', font=("Arial", 12))
etiquetaAjuste.grid(column = 0, row=6, pady=5)
etiquetaAjusteRecomendado = Label(ventanaInfPaciente, text = "Ej. Bajar sillin")
etiquetaAjusteRecomendado.grid(column = 0, row=7, padx=(15,0), pady=5)
analizarDeNuevoBtn = Button(ventanaInfPaciente, text="Analizar de nuevo", width=15, height=5, command = EjecutarAnalisisDenuevo)
analizarDeNuevoBtn.grid(column = 0, row=8,rowspan=3, padx=5, pady=5)
btnRegresar = Button(ventanaInfPaciente, text="Volver", width=15, command = CambiarVentanaPrincipal)
btnRegresar.grid(column = 0, row=11,rowspan=3, pady=5)


#botonVideo = Button(ventanaInfPaciente, text = "Elegir y Visualizar video", width = 20, height = 5, command = lambda: visualizarVideo(LabelVideo, LabelInfoVideoPath))
#botonVideo.grid(column = 2, row = 2, columnspan=2)
etiquetaVideo =  Label(ventanaInfPaciente, text = "Video procesado: ")    #solo admitira 2 numeros  
etiquetaVideo.grid(column = 1, row = 1,  pady=5, padx=(0, 30))
LabelVideo3 = Label(ventanaInfPaciente)
LabelVideo3.grid(column = 1, row = 2, rowspan = 6, columnspan=2)
AngulosEtiqueta =  Label(ventanaInfPaciente, text = "Angulos:")    #solo admitira 2 numeros  
AngulosEtiqueta.grid(column = 1, row = 8)
RodillaEtiqueta =  Label(ventanaInfPaciente, text = "Rodilla:")    #solo admitira 2 numeros  
RodillaEtiqueta.grid(column = 1,row=9 ,padx=5)
CaderaEtiqueta =  Label(ventanaInfPaciente, text = "Cadera: ")    #solo admitira 2 numeros  
CaderaEtiqueta.grid(column = 1,row=10 ,padx=5)
HombroEtiqueta =  Label(ventanaInfPaciente, text = "Hombro: ")    #solo admitira 2 numeros  
HombroEtiqueta.grid(column = 1, row=11,padx=5)
TrasCaderaEtiqueta =  Label(ventanaInfPaciente, text = "Traslacion de cadera:\n Vertical: " + "" + " - " + " Horizontal: " + "")    #solo admitira 2 numeros  
TrasCaderaEtiqueta.grid(column = 1, row=12,padx=5)

etiquetaRodilloMinimo =  Label(ventanaInfPaciente, text = "Angulo minimo de rodilla: ")    #solo admitira 2 numeros  
etiquetaRodilloMinimo.grid(column = 3, row = 1,  pady=5)
etiquetaImagenMin = Label(ventanaInfPaciente)
etiquetaImagenMin.grid(column = 3, row = 2, rowspan = 4)
etiquetaRodillaMaximo =  Label(ventanaInfPaciente, text = "Angulo maximo de rodilla: ")    #solo admitira 2 numeros  
etiquetaRodillaMaximo.grid(column = 3, row = 6, pady=5)
etiquetaImagenMax = Label(ventanaInfPaciente)
etiquetaImagenMax.grid(column = 3, row = 7, rowspan=6)
#-----------------------main def--------------------------------------
CambiarVentanaPrincipal()
# CambiarVentanaVideo()
# CambiarVentanaSelectInfPaciente()
# CambiarInfPaciente(1) 
# CambiarVentanaWebcam()


ventana.mainloop()
