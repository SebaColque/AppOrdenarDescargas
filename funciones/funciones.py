import os
from pathlib import Path
import sys
from tkinter import DISABLED, END, NORMAL, filedialog, messagebox

def mostrarInfo():
    mensaje = '''
    1- Este programa funciona para ordenar los archivos que se van descargando y quedan en la carpeta de descargas
    2- Si es la primera vez que usa el programa o no tiene todas las carpetas para guardar los archivos de descargas, seleccione que carpetas desea crear en el lado izquierdo y apriete "Crear carpetas"
    3- Si ya existen las carpetas a donde ordenar los archivos de descargas, seleccionelas apretando en "Cargar" o en "Cargar carpetas automaticamente"
    4- IMPORTANTE: es necesario ya sea crear las carpetas o seleccionarlas manualamente/automaticamente para poder realizar el ordenamiento
    5- Finalemente apriete en 'Ordenar Archivos' para realizar el ordenamiento
    
    sebacolque06@gmail.com 
    '''
    messagebox.showinfo(message=mensaje, title='Informacion')

# SOLUCION PROBLEMA DESCARGA
def ruta_descarga():
    
    ruta = Path(Path.home(), 'Downloads')
    while not Path(ruta).is_dir():
        mensaje = '''
        Para poder continuar, porfavor seleccione
        la carpeta "Descargas" en donde se realizan
        las descargas en tu sistema.
        '''
        seguir = messagebox.askquestion(message=mensaje, title='Carpeta Descargas')
        
        if seguir == 'yes':    
            ruta = filedialog.askdirectory()
        else:
            sys.exit()

    return ruta

# FUNCIONES COMMAND    
mensaje_mostrado = False
carpetas_ordenar = [0] * 9
def cargar_carpeta(index, btn, cuadros, ruta):
    mensaje = '''IMPORTANTE: las carpetas a seleccionar
deben estar en la carpeta de Descargas!!!'''
    global mensaje_mostrado
    if not mensaje_mostrado:
        messagebox.showinfo(message=mensaje, title='IMPORTANTE')
        mensaje_mostrado = True
    
    nombre_carpeta = filedialog.askdirectory(initialdir=ruta)
    
    if nombre_carpeta:
        if str(ruta) not in str(Path(nombre_carpeta)):
            messagebox.showinfo(message=mensaje, title='IMPORTANTE')
        else:
            cargar_nombre_carpeta(index, nombre_carpeta.split('/')[-1], cuadros)            
            btn.config(state='normal', cursor='hand2')

def crear_carpetas(cuadros, variables, btn, ruta):
    carpetas_repetidas = []
    carpetas_creadas = []
    x = 0
    for c in cuadros:
        if variables[x].get() != '0':
            nombre_carpeta = variables[x].get().upper() + '_Descargas'
            if Path(ruta, nombre_carpeta).exists():
                carpetas_repetidas.append(nombre_carpeta)
            else:
                os.mkdir(Path(ruta, nombre_carpeta))
                carpetas_creadas.append(nombre_carpeta)
            carpetas_ordenar[x] = nombre_carpeta
            cargar_nombre_carpeta(x, nombre_carpeta, cuadros)
            btn.config(state='normal', cursor='hand2')
        x += 1
    
    mensaje = f'''
    Carpetas creadas: 
    {' - '.join(carpetas_creadas)}
    
    Carpetas que ya existian y no se crearon:
    {' - '.join(carpetas_repetidas)}
    '''
    messagebox.showinfo(message=mensaje, title='Informacion')
    
def cargar_nombre_carpeta(index, nombre, cuadro):
    cuadro[index].config(state=NORMAL)
    cuadro[index].delete(0, END)
    cuadro[index].insert(0, nombre)
    cuadro[index].config(state=DISABLED)
    carpetas_ordenar[index] = nombre

# def detrminar_tipo_capeta(ruta, *args):
#     carpetas_full = []
    
#     carpetas = os.listdir(ruta)
#     for carpeta in carpetas:
#         if os.path.isdir(Path(ruta, carpeta)):
#             archivos = os.listdir(Path(ruta, carpeta))
#             igual = True
#             for archivo in archivos:
#                 name_arch, extension = os.path.splitext(archivo)
#                 if extension.lower() not in args:
#                     igual = False
#             if igual:
#                 carpetas_full.append(carpeta)
#     return carpetas_full
        
def cargar_carpetas_auto(btn, cuadro, ruta):
    mensaje = '''IMPORTANTE: esta funcion sirve para cargar
las carpetas automaticamente si usan nombres representativos 
(Ej: PDF.. para archivos pdfs | EXE... o EJECTUABLE... para archivos ejectuables)
y se encuentren en la carpeta de Descargas!!!
Sugerencias para nombres carpetas:
PDF | WORD | EXCEL | FOTOS o IMAGENES | VIDEOS | EJECUTABLES o PROGRAMAS
ZIP o RAR o COMPRIMIDO | POWERS o PPTS | OTROS
    '''
    messagebox.showinfo(message=mensaje, title='Automatico')
    
    carpetas = os.listdir(ruta)

    for carpeta in carpetas:
            if not os.path.isdir(Path(ruta, carpeta)): continue
            if ('PDF') in carpeta.upper():
                cargar_nombre_carpeta(0, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('DOCUMENT', 'WORD')):
                cargar_nombre_carpeta(1, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('EXCEL', 'CALCULO', 'PLANTILLA')):
                cargar_nombre_carpeta(2, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('IMAGEN', 'FOTO', 'ALBUM', 'IMG', 'SNAP', 'SCREEN')):
                cargar_nombre_carpeta(3, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('VIDEO', 'PELI', 'CLIP', 'GRABA', 'RECORD')):                
                cargar_nombre_carpeta(4, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('EJEC', 'EXE', 'PROG', 'SOFT', 'INSTAL', 'BIN')):                
                cargar_nombre_carpeta(5, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('ZIP', 'RAR', 'COMPR', 'TAR', '7Z')):                
                cargar_nombre_carpeta(6, carpeta, cuadro)
            elif any(keyword in carpeta.upper() for keyword in ('PRESENT', 'POWER', 'PPT', 'POINT', 'PPT')):                
                cargar_nombre_carpeta(7, carpeta, cuadro)
            elif ('OTRO') in carpeta.upper():
                cargar_nombre_carpeta(8, carpeta, cuadro)
                
    btn.config(state='normal', cursor='hand2')         


def ordenar_archivos(ruta):
    extensiones = ['.pdf', '.doc', '.docx', '.xlsx', '.csv', '.jpg', '.jpeg', '.png', '.ico', '.webp', '.svg' 
                   '.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', 'webm', 'm4v', '.gif',
                   '.exe', '.app', '.py', '.jar', '.bin', '.msi', '.zip', '.rar', '.7z', '.tar', '.gz',
                   '.ppt', '.pptx', '.pps', '.ppsx', '.pot', '.potx', '.ppa']
    
    for filename in os.listdir(ruta):
        name, extension = os.path.splitext(Path(ruta, filename))
        name_arch, a = os.path.splitext(filename)
        if extension in ['.pdf']:
            if carpetas_ordenar[0] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[0],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[0], name_arch + '(REPETIDO)' + extension))
        
        if extension in ['.doc', '.docx']:
            if carpetas_ordenar[1] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[1],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[1], name_arch + '(REPETIDO)' + extension))
        
        if extension in ['.xlsx', '.csv']:
            if carpetas_ordenar[2] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[2],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[2], name_arch + '(REPETIDO)' + extension))
        
        if extension in ['.jpg', '.jpeg', '.png', '.ico', '.webp', '.svg']:
            if carpetas_ordenar[3] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[3],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[3], name_arch + '(REPETIDO)' + extension))
        
        if extension in ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', 'webm', '.m4v', '.gif']:
            if carpetas_ordenar[4] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[4],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[4], name_arch + '(REPETIDO)' + extension))        
        if extension in ['.exe', '.app', '.py', '.jar', '.bin', '.msi']:
            if carpetas_ordenar[5] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[5],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[5], name_arch + '(REPETIDO)' + extension))
        if extension in ['.zip', '.rar', '.7z', '.tar', '.gz']:
            if carpetas_ordenar[6] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[6],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[6], name_arch + '(REPETIDO)' + extension))
        if extension in ['.ppt', '.pptx', '.pps', '.ppsx', '.pot', '.potx', '.ppa']:
            if carpetas_ordenar[7] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[7],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[7], name_arch + '(REPETIDO)' + extension))
        if extension not in extensiones and not os.path.isdir(name):
            if carpetas_ordenar[8] == 0:
                continue
            try: 
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[8],  filename))
            except:
                os.rename(Path(ruta, filename), Path(ruta, carpetas_ordenar[8], name_arch + '(REPETIDO)' + extension))

    messagebox.showinfo(message='Archivos Ordenados', title='Completado')
    

# FUNCION PARA SOLUCIONAR EL PROBLEMA DEL ICONO
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
