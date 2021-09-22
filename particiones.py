# import mysql.connector
# import winapps

# # Se genera una coneccion a una base de datos
# conexion1 = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydb")

# cursor1 = conexion1.cursor()

# sql = "insert into farmacia_cantidad_programas(cantidad,tabla_programas_id) values(%s,%s)"

# pc = '181.15.193.99'

# def cantidad_programas():
#     cantidad = 0
#     for item in winapps.list_installed():
#         cantidad += 1
#     return cantidad

# datos = (cantidad_programas(),pc)

# #ejecucion de la consulta para insertar los datos
# cursor1.execute(sql, datos)

# # Termina la conexion
# conexion1.commit()

# # Se cierra la conexion
# conexion1.close()

import os
import socket

nombre_PC = socket.gethostname()
IPpri = socket.gethostbyname(nombre_PC)

IPpri = socket.gethostbyname(nombre_PC)

print(IPpri)