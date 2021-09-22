#se importan las librerias necesarias para extraer los detalles de la pc
import mysql.connector
import winapps

# loop que recorre la lista de programas instalados 
for item in winapps.list_installed():
    # Se genera una coneccion a una base de datos
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="mydb")
    cursor1=conexion1.cursor()
        # se genera el objeto con el que se guardan los datos
            
    sql="""insert into farmacia_probando_programas(nombre, 
                                        version, 
                                        fecha_install, 
                                        pc_id) 
                                        values(%s,%s,%s,%s)"""

    programa_nombre = item.name
    programa_version = str(item.version)
    programa_fecha = str(item.install_date)
    
    #hacer una funcion que retorne el nro de cliente de la fcia para guardar en la consulta
    pc = '181.15.193.99'

    # se guardan todos los datos en una variable
    datos=(programa_nombre,programa_version,programa_fecha,pc)

    #ejecucion de la consulta para insertar los datos
    cursor1.execute(sql, datos)

    # Termina la conexion
    conexion1.commit()

    # Se cierra la conexion
    conexion1.close()