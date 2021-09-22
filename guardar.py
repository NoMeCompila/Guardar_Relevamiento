# #se importan las librerias necesarias para extraer los detalles de la pc
# import socket 
# from datetime import datetime 
# import mysql.connector
# from subprocess import Popen #libreria para ejecutar subprocesos de windows

# # Se genera una coneccion a una base de datos
# conexion1=mysql.connector.connect(host="localhost", 
#                                   user="root", 
#                                   passwd="", 
#                                   database="mydb")

# # se genera el objeto con el que se guardan los datos
# cursor1=conexion1.cursor()

# # Consulta SQL que sequiere realizar
# sql="""insert into farmacia_pc_detalle(ip, 
#                                         nombre_pc, 
#                                         id_AnyDesk, 
#                                         fecha_hora) 
#                                         values(%s,%s,%s,%s)"""

# # Función que devuelve el nombre del equipo 
# def get_name():
#     nombre_PC = socket.gethostname()
#     return nombre_PC

# # Funcioin que devuelve la ip privada
# def get_ip():
#     nombre_PC = socket.gethostname()
#     IPpriv = socket.gethostbyname(nombre_PC)
#     return IPpriv

# # Funcion que ejecuta al bat para obtener la id y guardarla en un txt
# def exec_bat():
#     p = Popen("get_id_any.bat")
#     stdout, stderr = p.communicate()
# exec_bat()

# # Funcion que lee el archivo generado por get_id_any.bat y guarda su contenido en una lista, luego la retorna transformada en un str 
# def get_any_id():
#     datos2 = []
#     with open("Any_id.txt") as fname:
# 	    for lineas in fname:
# 		    datos2.extend(lineas.split())
#     idAny = "".join(datos2)
#     return idAny

# # Funcion que devuelve la fecha y hora
# def get_datetime():
#     fecha_hora = datetime.now()
#     return fecha_hora

# # se guardan todos los datos en una variable
# datos=(get_ip(),get_name(),get_any_id(),get_datetime())

# #ejecucion de la consulta para insertar los datos
# cursor1.execute(sql, datos)

# # Termina la conexion
# conexion1.commit()

# # Se cierra la conexion
# conexion1.close()

#se importan las librerias necesarias para extraer los detalles de la pc
import socket 
from datetime import datetime 
import mysql.connector
from subprocess import Popen #libreria para ejecutar subprocesos de windows

# Se genera una coneccion a una base de datos
conexion1=mysql.connector.connect(host="sistemassoporte.mysql.pythonanywhere-services.com", 
                                  user="sistemassoporte", 
                                  passwd="Chizzo1991", 
                                  database="sistemassoporte$u551789018_relevamiento")

# se genera el objeto con el que se guardan los datos
cursor1=conexion1.cursor()

# Consulta SQL que sequiere realizar
sql="insert into persona(dni,nombre) values(%s,%s)"

dni = 37654559
nombre = "Fulanoide"

# se guardan todos los datos en una variable
datos=(dni,nombre)

#ejecucion de la consulta para insertar los datos
cursor1.execute(sql, datos)

# Termina la conexion
conexion1.commit()

# Se cierra la conexion
conexion1.close()
