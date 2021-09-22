#se importan las librerias necesarias para extraer los detalles de la pc
import socket 
from datetime import datetime 
import mysql.connector
from subprocess import Popen #libreria para ejecutar subprocesos de windows
import urllib.request
import platform 
import psutil
import winapps
import os
import re
# Se genera una coneccion a una base de datos
conexion1=mysql.connector.connect(host="185.201.11.212", 
                                  user="u551789018_agus_fer", 
                                  passwd="Chizzo1991", 
                                  database="u551789018_relevamiento")

# se genera el objeto con el que se guardan los datos
cursor1=conexion1.cursor()

# Consulta SQL que sequiere realizar
sql="""insert into farmacia_pc_farmacia(fecha_relevamiento,
                                        ip,
                                        nombre_pc,  
                                        ip_publica,
                                        arquitectura_so, 
                                        version_so, 
                                        tipo_maquina,
                                        procesador, 
                                        cores_fisicos,
                                        cores_totales,
                                        RAM_tot, 
                                        RAM_usada, 
                                        RAM_disponible,
                                        RAM_procentaje_disponible,
                                        espacio_tot_C, 
                                        espacio_tot_D, 
                                        espacio_usado_C, 
                                        espacio_usado_D,
                                        espacio_disponible_C,
                                        espacio_disponible_D,
                                        procentaje_disponible_C,
                                        procentaje_disponible_D,
                                        AnyDesk_instalado,
                                        id_AnyDesk,
                                        nro_cliente_id)
                                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# funciion que retorna fecha y hora
def get_datetime():
    fecha_relevamiento = datetime.now()
    return fecha_relevamiento
    
# funcion que retorna la ip privada
def get_ip():
    # nombre_PC = socket.gethostname()
    # IPpriv = socket.gethostbyname(nombre_PC)
    # return IPpriv
    return '198.162.0.123'

# funcion que retorna el nombre del device
def get_name():
    nombre_PC = socket.gethostname()
    return nombre_PC

# funcion que retorna la ipo publica como un string
def get_public_ip():
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip_externa

# funcion que retorna la arquitectura del SO
def get_arch_so():
    arqui_sist = str(platform.architecture())
    return arqui_sist

# Funcón que retorna la vbersion del sistema operativo
def get_version():
    vers = str(platform.release())
    return vers

# Funcion que retorna el tipo de maquina
def get_mach_type():
    tipo_maquina = platform.machine()
    return  tipo_maquina

# Funcion que retorna el tipo de procesador
def get_processor():
    procesador = platform.processor()
    return procesador

# Función que retorna los cores físicos
def phiscal_cores():
    cores_fisicos = psutil.cpu_count(logical=False)
    return cores_fisicos

# Función que retorna los cores totales
def get_logic_cores():
    cores_logicos = psutil.cpu_count(logical=True)
    return cores_logicos 

# Función que retronra todas las unidades de medida transformadas a GB 
def get_size(bytes, sufijo="B"):
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor_conversion:
            return f"{bytes:.2f}{unidad}{sufijo}" #retorna la unidad de medida final redondeada a 2 decimales con su correspondiente abreviatura
        bytes /= factor_conversion

# Funcion que retorna la ram total
def tot_RAM():
    ram = psutil.virtual_memory()
    ram_total = get_size(ram.total)
    return ram_total

# Función que retorna la cantidad de RAM usada
def used_RAM():
    ram = psutil.virtual_memory()
    ram_usada = get_size(ram.used)
    return ram_usada

# Función que retorna la cantidad de ram disponible
def aval_RAM():
    ram = psutil.virtual_memory()
    ram_disponible = get_size(ram.available)
    return ram_disponible 

# Función que retorna el porcentaje de ram usado
def percent_RAM():
    ram = psutil.virtual_memory()
    porcentaje_ram = str(ram.percent) + "%"
    return porcentaje_ram

# Funcion que recorre una lista con todos los puntos de montaje y busca el disco local C y retorna su espacio total
def tot_C():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'C:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                espacio_tot_C = get_size(partition_usage.total)
            except PermissionError:
                continue
        
    return espacio_tot_C

# Funcion que recorre una lista con todos los puntos de montaje y busca el disco local D y retorna su espacio total
def tot_D():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'D:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                espacio_tot_D = get_size(partition_usage.total)
            except PermissionError:
                continue
        
    return espacio_tot_D

# Funcion que recorre una lista con todos los puntos de montaje y busca el disco local C y retorna su espacio usado
def used_C():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'C:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                usado_C = get_size(partition_usage.used)
            except PermissionError:
                continue
        
    return usado_C

# Funcion que recorre una lista con todos los puntos de montaje y busca el disco local D y retorna su espacio usado
def used_D():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'D:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                usado_D = get_size(partition_usage.used)
            except PermissionError:
                continue
        
    return usado_D

# Función que recorre una lista con todos los puntos de montaje y busca el disco local C y retorna el espacio libre
def free_C():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'C:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                libre_C = get_size(partition_usage.free)
            except PermissionError:
                continue
        
    return libre_C

# Función que recorre una lista con todos los puntos de montaje y busca el disco local D y retorna el espacio libre
def free_D():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'D:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                libre_D = get_size(partition_usage.free)
            except PermissionError:
                continue
        
    return libre_D

# Función que recorre una lista con todos los puntos de montaje y busca el disco local C y retorna el procentaje usado
def percent_C():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'C:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                porcentaje_C = str(get_size(partition_usage.percent)) + "%"
            except PermissionError:
                continue
        
    return porcentaje_C

# Función que recorre una lista con todos los puntos de montaje y busca el disco local D y retorna el procentaje usado
def percent_D():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        devi = partition.device + " "
        if devi == 'D:\ ': 
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                porcentaje_D = str(get_size(partition_usage.percent)) + "%"
            except PermissionError:
                continue
        
    return porcentaje_D

# Función que recorre una lista con todos los programas instalados en windows y busca el programa any desk y retorna "SI" en caso de encontrarlo o "NO" en caso contrario
def any_instalado():
    # obtiene una lista con cada aplicacion instalada en windows
    for item in winapps.list_installed():
        if  item.name == 'AnyDesk':
            app = "SI"
        else:
            app = "NO" #verificar que efectivamente devuelva "NO" cuando no tiene isntalado
    return app

# Funcion que ejecuta al bat para obtener la id y guardarla en un txt
def exec_bat():
    p = Popen("get_id_any.bat")
    stdout, stderr = p.communicate()
exec_bat()

# Funcion que lee el archivo generado por get_id_any.bat y guarda su contenido en una lista, luego la retorna transformada en un str 
def get_any_id():
    datos2 = []
    with open("Any_id.txt") as fname:
	    for lineas in fname:
		    datos2.extend(lineas.split())
    idAny = "".join(datos2)
    return idAny

# Función provisoria para relacionar el relevamiento de una PC con una farmacia
def get_nro_cliente():
    nro_cliente = [ 'C:\\3303.txt', 'C:\\2986.txt', 'C:\\3183.txt', 'C:\\6200.txt',  'C:\\5800.txt', 'C:\\8100.txt', 'C:\\693.txt', 
                    'C:\\700.txt', 'C:\\1480.txt', 'C:\\1920.txt',  'C:\\2023.txt',  'C:\\2193.txt', 'C:\\2279.txt', 'C:\\2500.txt', 
                    'C:\\3431.txt', 'C:\\5100.txt', 'C:\\5200.txt', 'C:\\5500.txt',  'C:\\5700.txt', 'C:\\8700.txt', 'C:\\8800.txt', 
                    'C:\\9070.txt', 'C:\\9080.txt', 'C:\\9170.txt', 'C:\\1916.txt',  'C:\\2241.txt', 'C:\\3414.txt', 'C:\\9130.txt', 
                    'C:\\2987.txt', 'C:\\8200.txt', 'C:\\701.txt',  'C:\\707.txt',   'C:\\1249.txt', 'C:\\1250.txt', 'C:\\1252.txt', 
                    'C:\\1253.txt', 'C:\\1255.txt', 'C:\\1256.txt', 'C:\\1257.txt',  'C:\\1274.txt', 'C:\\1418.txt', 'C:\\1645.txt', 
                    'C:\\1731.txt', 'C:\\1814.txt', 'C:\\1875.txt', 'C:\\1966.txt',  'C:\\3419.txt', 'C:\\3444.txt', 'C:\\6600.txt', 
                    'C:\\7000.txt', 'C:\\7500.txt', 'C:\\7600.txt', 'C:\\7800.txt',  'C:\\8000.txt', 'C:\\8400.txt', 'C:\\9000.txt', 
                    'C:\\9010.txt', 'C:\\9040.txt', 'C:\\9060.txt', 'C:\\9090.txt',  'C:\\9100.txt', 'C:\\9120.txt', 'C:\\9140.txt', 
                    'C:\\9160.txt', 'C:\\9190.txt', 'C:\\6500.txt', 'C:\\7400.txt',  'C:\\1900.txt', 'C:\\2419.txt', 'C:\\5000.txt', 
                    'C:\\8500.txt', 'C:\\9150.txt', 'C:\\7700.txt', 'C:\\6700.txt',  'C:\\8300.txt', 'C:\\5600.txt', 'C:\\9050.txt', 
                    'C:\\3524.txt', 'C:\\8900.txt', 'C:\\6000.txt', 'C:\\7900.txt',  'C:\\3010.txt', 'C:\\3055.txt', 'C:\\6300.txt', 
                    'C:\\8600.txt', 'C:\\3366.txt', 'C:\\5300.txt', 'C:\\6100.txt',  'C:\\2919.txt', 'C:\\3019.txt', 'C:\\3231.txt', 
                    'C:\\3275.txt', 'C:\\7200.txt', 'C:\\9020.txt', 'C:\\9030.txt',  'C:\\9110.txt', 'C:\\9180.txt', 'C:\\2628.txt', 
                    'C:\\2765.txt', 'C:\\2879.txt', 'C:\\3022.txt']

    for nro in nro_cliente:
        
        if  os.path.exists(nro):
                        
            numero = re.findall(r'\d+', nro)

            numero_cliente = "".join(numero)
    
    return int(numero_cliente)
    
    #return nro_cliente

"""
se necesita una funcion que retorne el numero de cliente
"""

#variable que guarda todos los datos en una lista
datos=(get_datetime(),
        get_ip(),
        get_name(),
        get_public_ip(),
        get_arch_so(),
        get_version(),
        get_mach_type(),
        get_processor(),
        phiscal_cores(),
        get_logic_cores(),
        tot_RAM(),
        used_RAM(),
        aval_RAM(),
        percent_RAM(),
        tot_C(),
        tot_D(),
        used_C(),
        used_D(),
        free_C(),
        free_D(),
        percent_C(),
        percent_D(),
        any_instalado(),
        get_any_id(),
        get_nro_cliente())

#ejecucion de la consulta para insertar los datos
cursor1.execute(sql, datos)

# Termina la conexion
conexion1.commit()

# Se cierra la conexion
conexion1.close()