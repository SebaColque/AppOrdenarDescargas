from tkinter import *
from funciones.funciones import *

# INICIAL CONFIG
aplicacion = Tk()
aplicacion.title('OrdenarDescargas')
aplicacion.resizable(False, False)
aplicacion.geometry('700x500+350+100')
icono = resource_path("appico.ico")
aplicacion.iconbitmap(icono)

# PANEL SUPERIOR
panel_superior = Frame(aplicacion, bg='#ECE0DE')
panel_superior.pack(side=TOP)
# TITULO
lblTitulo = Label(panel_superior, text='Ordenar Descargas', font=('Arial', 20, 'bold'), bg='#ECE0DE', width=42)
lblTitulo.grid(column=0, row=0)
# BOTON INFO
buttonInfo = Button(panel_superior, text='ⓘ', font=('italic', 10, 'bold'), cursor='hand2', command=mostrarInfo)
buttonInfo.place(x=665, y=5)

# PANEL CENTRAL
panel_central = Frame(aplicacion)
panel_central.pack(side=TOP, pady=0)
# SUBTITULO
lbl_panel_izq = Label(panel_central, text='Seleccione las Carpetas que deseas crear    o    Seleccione las Carpetas donde ordenar',  
                      font=('Arial', 12))
lbl_panel_izq.place(x=20, y=0)



# PANEL IZQUIERDO
panel_izq = Frame(panel_central, border=5, bg='#EA906C', relief='solid', bd=2)
panel_izq.pack(side=LEFT, padx=10, pady=30)

# PANEL DERECHO
panel_der = Frame(panel_central, border=5, bg='#EA906C', relief='solid', bd=2, pady=5)
panel_der.pack(side=RIGHT, ipady=0, ipadx=5)

# PANEL BOTONES
panel_botones = Frame(aplicacion,
                      bd=1,
                      relief=FLAT)
panel_botones.pack()

# LISTA CARPETAS
lista_carpetas = ['PDF', 'WORD', 'EXCEL', 'IMAGENES', 'VIDEOS', 'EJECUTABLES', 'ZIP-RAR', 'POWERPOINTS', 'OTROS']

# Generar items carpetas
variables_carpeta = []
cuadros_carpeta = []
texto_carpeta = []
botones_carpeta = []

# CARGAR CONTENIDO PANEL IZQ
contador = 0
for carpeta in lista_carpetas:
    # Crear ckeckbuttons
    variables_carpeta.append('')
    variables_carpeta[contador] = StringVar()
    carpeta = Checkbutton(panel_izq, 
                         text=carpeta.title(),
                         font=('Dosis', 13, 'bold'),
                         onvalue=carpeta.title(),
                         offvalue='0',
                         variable=variables_carpeta[contador],
                         padx=100,
                         bg='#EA906C',
                         cursor='hand2')
    carpeta.deselect()
    carpeta.grid(row=contador,
                column=0,
                sticky=W)

    contador += 1
    
contador = 0
for index, carpeta in enumerate(lista_carpetas):
    # Crear ckeckbuttons
    carpeta = Label(panel_der, 
                         text=carpeta.title() + ':',
                         font=('Dosis', 13, 'bold'),
                         padx=0,
                         pady=3,
                         bg='#EA906C')
    carpeta.grid(row=contador,
                column=0,
                sticky=W)
    
    # Crear cuadros de entrada
    cuadros_carpeta.append('')
    texto_carpeta.append('')
    texto_carpeta[contador] = StringVar()
    cuadros_carpeta[contador] = Entry(panel_der,
                                     font=('Dosis', 10),
                                     bd=1,
                                     width=20,
                                     state=DISABLED,
                                     textvariable=texto_carpeta[contador],)
    cuadros_carpeta[contador].grid(row=contador, column=1)
    
    contador += 1

botones_carpeta.append('')
botones_carpeta[0] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(0, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[0].grid(row=0, column=2)
botones_carpeta.append('')
botones_carpeta[1] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(1, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[1].grid(row=1, column=2)
botones_carpeta.append('')
botones_carpeta[2] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(2, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[2].grid(row=2, column=2)
botones_carpeta.append('')
botones_carpeta[3] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(3, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[3].grid(row=3, column=2)
botones_carpeta.append('')
botones_carpeta[4] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(4, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[4].grid(row=4, column=2)
botones_carpeta.append('')
botones_carpeta[5] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(5, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[5].grid(row=5, column=2)
botones_carpeta.append('')
botones_carpeta[6] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(6, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[6].grid(row=6, column=2)
botones_carpeta.append('')
botones_carpeta[7] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(7, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[7].grid(row=7, column=2)
botones_carpeta.append('')
botones_carpeta[8] = Button(panel_der,
                                       text='Cargar',
                                       font=('Dosis', 10),
                                       bd=1,
                                       width=6,
                                       command=lambda: cargar_carpeta(8, boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                                       padx= 5,
                                       cursor='hand2')
botones_carpeta[8].grid(row=8, column=2)

# BOTONES
boton_crear = Button(panel_izq,
                   text='Crear carpetas',
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=15,
                   command=lambda: crear_carpetas(cuadros_carpeta, variables_carpeta, boton_ordenar, ruta_de_descarga),
                   cursor='hand2')
boton_crear.grid(row=contador, column=0, padx=40, pady=15)

boton_cargar_auto = Button(panel_der,
                   text='Cargar carpetas auto',
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=16,
                   command=lambda: cargar_carpetas_auto(boton_ordenar, cuadros_carpeta, ruta_de_descarga),
                   cursor='hand2')
boton_cargar_auto.grid(row=contador, column=1, padx=0, pady=15)

boton_ordenar = Button(panel_botones,
                   text='Ordenar archivos',
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=15,
                   command=lambda: ordenar_archivos(ruta_de_descarga),
                   state='disabled',)
boton_ordenar.grid(row=contador+1, column=1, pady=20)

# MOSTAR INFO
mostrarInfo()

ruta_de_descarga = ruta_descarga()

aplicacion.mainloop()