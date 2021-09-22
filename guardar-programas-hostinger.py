#se importan las librerias necesarias para extraer los detalles de la pc
import mysql.connector
import winapps
# loop que recorre la lista de programas instalados 
for item in winapps.list_installed():
    # Se genera una coneccion a una base de datos
    # Se genera una coneccion a una base de datos
    conexion1=mysql.connector.connect(host="185.201.11.212", 
                                  user="u551789018_agus_fer", 
                                  passwd="Chizzo1991", 
                                  database="u551789018_relevamiento")
    cursor1=conexion1.cursor()
        # se genera el objeto con el que se guardan los datos
    sql="""insert into farmacia_programas_instalados(nombre, 
                                        version, 
                                        fecha_install, 
                                        pc_id) 
                                        values(%s,%s,%s,%s)"""
    programa_nombre = item.name
    programa_version = str(item.version)
    programa_fecha = str(item.install_date)
    
    #modificar la funcion
    pc = '192.168.1.548'

    """
        se necesita una funcion que retorne el id de la farmacia a la que corresponde el relevamiento de la PC
    """


    # se guardan todos los datos en una variable
    datos=(programa_nombre,programa_version,programa_fecha,pc)

    #ejecucion de la consulta para insertar los datos
    cursor1.execute(sql, datos)

    # Termina la conexion
    conexion1.commit()

    # Se cierra la conexion
    conexion1.close()