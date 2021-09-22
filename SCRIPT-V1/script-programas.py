from datetime import datetime  # libreria para importar la fecha y hora actual del sistema
import winapps  # libreria para manejo de aplicaciones de windows
import socket  # libreria para saber nombre del PC
import platform

def titulo(cadena):
    return cadena.center(50, "=")

#Funcion que devuelve la fecha con formato simple
def fecha():
    fecha_hora = datetime.now()
    return str(fecha_hora)

def renombrar():
    nombre_PC = socket.gethostname()
    return nombre_PC + "-programas.txt"

def mostrar_programas():
    #Creacion de un archivo de texto para almacenar todos los programas instalados
    archivo_programas = open(renombrar(), "w")

    cadena = "Programas Instalados - Fecha: " + fecha()

    archivo_programas.write(titulo(cadena) + "\n\n")
    # Grabar en el archivo un título indicando el nombre de la PC

    cadena = "Programas instalados en " + socket.gethostname()
    archivo_programas.write(titulo(cadena) + "\n\n")
    # loop que recorre la lista de programas instalados
    #lista_instalados = list(winapps.list_installed())
    #mitad_lista = lista_instalados[len(lista_instalados) // 2:]
    coleccion = []
    total = 0
    for item in winapps.list_installed():
        if item in coleccion:
            continue
        else:
            total += 1
        # Grabacion en el achivo de texto de los programas instalados
            if item.install_date == None:
                archivo_programas.write("Programa: " + item.name + "\n")
                archivo_programas.write("Version: " + str(item.version) + "\n")
                archivo_programas.write("Fecha de instalacion: de Fabrica o instalado por sistemas" + "\n")
                archivo_programas.write("--------------------------------------------------\n")
            else:
                archivo_programas.write("Programa: " + item.name + "\n")
                archivo_programas.write("Version: " + str(item.version) + "\n")
                archivo_programas.write("Fecha de instalacion: " + str(item.install_date) + "\n")
                archivo_programas.write("--------------------------------------------------\n")


        coleccion.append(item)

    archivo_programas.write(f"Total de programas: {str(total)}")
    archivo_programas.close()

mostrar_programas()
