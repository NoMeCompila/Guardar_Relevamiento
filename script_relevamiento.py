# Importar librerias
import socket #libreria para saber nombre del PC
import platform #libreria para obtener especificaciones de hardware
import urllib.request #libreria para obtener ip publica y privada
import psutil #libreria para el manejo de memoria
import winapps #libreria para manejo de aplicaciones de windows
from subprocess import Popen #libreria para ejecutar subprocesos de windows
# Importar las librerias del Sistema Operativo
from os import rename, remove, write # libreria que permite borrar un archivo del sistema
from os import path # libreria que permite obtener la ruta de un archivo del sistema
from io import open # libreria para manejo de archivos de entrada y salida estandar
from datetime import datetime #libreria para importar la fecha y hora actual del sistema

# Abrir el archivo con una variable global
archivo = open("info_pc.txt","w")

# Script que muestra un titulo y fecha de creacion del txt

# Funcion que centra los titulos: recibe como parametro un string y retorna un string en formato de titulo
def titulo(cadena):
    return cadena.center(50, "=") 

#  Funcion que devuelve la fecha con formato simple
def fecha():
    fecha_hora = datetime.now()
    return str(fecha_hora)

# Función para obtener el nombre de la maquina
def nombrePC():
    nombre_PC = socket.gethostname()
    archivo.write("Nombre de la PC: " + nombre_PC)

# Funcion para obtener las IP
def IPpriv():
    nombre_PC = socket.gethostname()
    IPpriv = socket.gethostbyname(nombre_PC)
    archivo.write("IP privada: " + IPpriv)

def IPpub():
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    archivo.write("IP publica: " + ip_externa)

# Función  que devuelve nformacion del sistema
def sist():
    arqui_sist=platform.architecture()
    archivo.write("Arquitectura y SO: " + str(arqui_sist))
    vers = platform.release()
    archivo.write("\nVersion: " + vers)

# Funcion que devuelve informacion sobre el hardware
def Cores():
    tipo_mauina=platform.machine()
    archivo.write("Tipo de maquina: " + tipo_mauina)
    procesador = platform.processor()
    archivo.write("\n" + "Procesador: " + procesador)
    cores_fisicos = psutil.cpu_count(logical=False)
    cores_totales = psutil.cpu_count(logical=True)
    archivo.write("\n" + "cores fisicos: " + str(cores_fisicos) + "\n" + "cores totales: " + str(cores_totales))

# Funcion de convfersion de unidades de almacenamiento
"""
    Reescala los bytes al formato adecuado
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
"""
def get_size(bytes, sufijo="B"):
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor_conversion:
            return f"{bytes:.2f}{unidad}{sufijo}" #retorna la unidad de medida final redondeada a 2 decimales con su correspondiente abreviatura
        bytes /= factor_conversion

def memoriaRAM():
    ram = psutil.virtual_memory()
    archivo.write("\nMemoria RAM  total: " + get_size(ram.total))
    archivo.write("\nMemoria RAM usada: " + get_size(ram.used))
    archivo.write("\nMemoria RAM disponible: " + get_size(ram.available))
    # print(f"Percentage: {swap.percent}%")
    archivo.write("\nPorcentage de memoria ram usado: " + str(ram.percent) + "%")
    if ram.percent > 90:
        archivo.write("\nestado: crítico\n")
    elif ram.percent >= 50 and ram.percent <= 90:
        archivo.write("\nestado: estable\n")
    else: 
        archivo.write("\nestado: optimo\n")

# Funcion que devuelve el espacio en disco disponible

def espacioEnDisco():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        archivo.write(f"=== Disco Local: {partition.device} ===\n")
        archivo.write(f"Punto de montaje: {partition.mountpoint}\n")
        archivo.write(f"File system type: {partition.fstype}\n")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        archivo.write("Espacio total en disco: " + get_size(partition_usage.total))
        archivo.write("\nEspacio usado en disco: " + get_size(partition_usage.used))
        archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free))
        # print(f"  Percentage: {partition_usage.percent}%")
        archivo.write("\nProcentage de espacio utilizado: " + str(partition_usage.percent) + "%\n")

        if partition_usage.percent > 90:
            archivo.write("\nestado: crítico\n")
        elif partition_usage.percent >= 50 and partition_usage.percent <= 90:
            archivo.write("\nestado: estable\n")
        else: 
            archivo.write("\nestado: optimo\n")
            archivo.write("-" * 50 + "\n")

# Funcion que ejecuta al bat para obtener la id y guardarla en un txt
def get_id():
    p = Popen("get_id_any.bat")
    stdout, stderr = p.communicate()

# Función que devuelve una lista y filtra para verificar que el any_desk esté instalado
def any_instalado():
    # obtiene una lista con cada aplicacion instalada en windows
    for item in winapps.list_installed():
        if item.name == "AnyDesk":
            archivo.write("Anydesk Instalado || ")
            get_id()# llamada a la funcion para obtener el id y guardarlo en un txt
            #concatenar()#llamada a la funcion que ejecuta la concatencacion del txt con especificaciones y la id del any        
            
def mostrar_programas():
    
    # Creacion de un archivo de texto para almacenar todos los programas instalados
    archivo_programas = open("programas_instalados.txt","w")
    
    cadena  =  "Programas Instalados - Fecha: " + fecha()
    
    archivo_programas.write(titulo(cadena) + "\n\n")
    # Grabar en el archivo un título indicando el nombre de la PC

    cadena = "Programas instalados en " + socket.gethostname()
    archivo_programas.write(titulo(cadena) + "\n\n")
    # loop que recorre la lista de programas instalados 
    
    cantidad_programas = 0
    for item in winapps.list_installed():
        cantidad_programas+=1
        # Grabacion en el achivo de texto de los programas instalados

        if item.install_date == None:
            archivo_programas.write("Programa: " + item.name + "\n")
            archivo_programas.write("Version: " + str(item.version) + "\n")
            archivo_programas.write("Fecha de instalacion: de Fabrica o instalado por sistemas" + "\n")
            archivo_programas.write("------------------------------------------------------------------------------------\n")
        else:
            archivo_programas.write("Programa: " + item.name + "\n")
            archivo_programas.write("Version: " + str(item.version) + "\n")
            archivo_programas.write("Fecha de instalacion: " + str(item.install_date) + "\n")
            archivo_programas.write("------------------------------------------------------------------------------------\n")
    archivo_programas.write("Cantidad de progeramas instalados: " + str(cantidad_programas))
    # Cierre del archivo con los programas instalados
    archivo_programas.close()

# Funcion que une a todas las anteriores y cierra el archivo
def EjecutarTodo():

    cadena  = "Relevamiento - Fecha: " + fecha()
    archivo.write(titulo(cadena))

    cadena = "Nombre PC"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    nombrePC()
    
    cadena = "Informacion IP"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    IPpriv()
    archivo.write("\n")
    IPpub()
    
    archivo.write("\n")
    cadena  = "SISTEMA"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    sist()

    archivo.write("\n")
    cadena = "Hardware"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    Cores()

    cadena = "Memoria RAM"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    memoriaRAM()


    cadena = "Memoria en Disco"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    espacioEnDisco()
    

    cadena = "AnyDesk"
    archivo.write(titulo(cadena) + "\n")
    any_instalado()
    archivo.close() # CERRAR ARCHIVO SIEMPRE AL FINAL

    mostrar_programas()

EjecutarTodo()

# Concatenar los 2 archivos en uno solo
filenames = ['info_pc.txt', 'Any_id.txt']
# nombre_PC = socket.gethostname()
# ipprivada = (socket.gethostbyname(nombre_PC))

with open('especificaciones.txt','w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Eliminar los 2 archivos restantes
if path.exists('info_pc.txt') and path.exists('Any_id.txt'):
    remove('info_pc.txt')
    remove('Any_id.txt') 

def ipRenombrar():
    nombre_PC = socket.gethostname()
    ipprivada = (socket.gethostbyname(nombre_PC))
    return  ipprivada + ".txt"

archivo1 = "especificaciones.txt"
nombre_nuevo = ipRenombrar()

rename(archivo1, nombre_nuevo)
