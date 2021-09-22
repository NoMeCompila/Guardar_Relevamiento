# Importar librerias
import socket  # libreria para saber nombre del PC
import platform  # libreria para obtener especificaciones de hardware
import urllib.request  # libreria para obtener ip publica y privada
import psutil  # libreria para el manejo de memoria
import winapps  # libreria para manejo de aplicaciones de windows
from subprocess import Popen  # libreria para ejecutar subprocesos de windows
# Importar las librerias del Sistema Operativo
from os import remove # libreria que permite borrar un archivo del sistema
from io import open  # libreria para manejo de archivos de entrada y salida estandar
from datetime import datetime  # libreria para importar la fecha y hora actual del sistema

def ipRenombrar2():
    nombre_PC = socket.gethostname()
    return nombre_PC + "-especificaciones.txt"

#funcion booleana que retorna True en caso de que sea una arquitectura de 64 bits
def is_os_64bit():
    return platform.machine().endswith('64')


# Abrir el archivo con una variable global
archivo = open(ipRenombrar2(), "w")

# Script que muestra un titulo y fecha de creacion del txt

# Funcion que centra los titulos: recibe como parametro un string y retorna un string en formato de titulo
def titulo(cadena):
    return cadena.center(50, "=")

def sistema_op():
    sistema = platform.system()
    archivo.write(f"sistema operativo: {sistema}")
#print(arq)
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
    vers = platform.release()
    archivo.write("\nVersion: " + vers)
    #arqui_sist = platform.architecture()
    if is_os_64bit():
        archivo.write("arquitectura: 64-bit")
    else:
        archivo.write("arquitectura: 32-bit")


# Funcion que devuelve informacion sobre el hardware
def Cores():
    tipo_mauina = platform.machine()
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
            return f"{bytes:.2f}{unidad}{sufijo}"  # retorna la unidad de medida final redondeada a 2 decimales con su correspondiente abreviatura
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
    if is_os_64bit():
        p = Popen("get-any-ID-64.bat")
        stdout, stderr = p.communicate()
    else:
        p = Popen("get-any-ID-32.bat")
        stdout, stderr = p.communicate()


def any_instalado():
    coleccion = []
    #obtiene una lista con cada aplicacion instalada en windows
    for item in winapps.list_installed():
        if item in coleccion:
            continue
        else:
            if item.name == "AnyDesk":
                get_id()  # llamada a la funcion para obtener el id y guardarlo en un txt
                # concatenar()#llamada a la funcion que ejecuta la concatencacion del txt con especificaciones y la id del any
        coleccion.append(item)
# Función que devuelve una lista y filtra para verificar que el any_desk esté instalado

#def rename_programas():
#    nombre_PC = socket.gethostname()
#    return nombre_PC + "-programas.txt"

#def mostrar_programas():
    # Creacion de un archivo de texto para almacenar todos los programas instalados
#    archivo_programas = open(rename_programas(), "w")

#    cadena = "Programas Instalados - Fecha: " + fecha()

#    archivo_programas.write(titulo(cadena) + "\n\n")
    # Grabar en el archivo un título indicando el nombre de la PC

#    cadena = "Programas instalados en " + socket.gethostname()
#    archivo_programas.write(titulo(cadena) + "\n\n")
    # loop que recorre la lista de programas instalados
    #lista_instalados = list(winapps.list_installed())
    #mitad_lista = lista_instalados[len(lista_instalados) // 2:]
#    for item in winapps.list_installed():
#        # Grabacion en el achivo de texto de los programas instalados
#        if item.install_date == None:
#            archivo_programas.write("Programa: " + item.name + "\n")
#            archivo_programas.write("Version: " + str(item.version) + "\n")
#            archivo_programas.write("Fecha de instalacion: de Fabrica o instalado por sistemas" + "\n")
#            archivo_programas.write("--------------------------------------------------\n")
#        else:
#            archivo_programas.write("Programa: " + item.name + "\n")
#            archivo_programas.write("Version: " + str(item.version) + "\n")
#            archivo_programas.write("Fecha de instalacion: " + str(item.install_date) + "\n")
#            archivo_programas.write("--------------------------------------------------\n")
    #cantidad = str(len(lista_instalados))
    #archivo_programas.write("Cantidad de programas: " + cantidad + "\n")
    #archivo_programas.write("------------------------------------\n")
    # Cierre del archivo con los programas instalados
    #print(lista_instalados)
#    archivo_programas.close()

# Funcion que une a todas las anteriores y cierra el archivo
def EjecutarTodo():
    cadena = "Relevamiento - Fecha: " + fecha()
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
    cadena = "SISTEMA"
    archivo.write("\n\n" + titulo(cadena))
    archivo.write("\n")
    sist()
    #archivo.write("\n")
    sistema_op()

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
    archivo.close()  # CERRAR ARCHIVO SIEMPRE AL FINAL
    any_instalado()

#mostrar_programas()
EjecutarTodo()
