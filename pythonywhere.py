import mysql.connector

# Se genera una coneccion a una base de datos
conexion1=mysql.connector.connect(host="sistemassoporte.mysql.pythonanywhere-services.com", 
                                  user="sistemassoporte", 
                                  passwd="Chizzo1991", 
                                  database="sistemassoporte$relevamiento_jufec")

cursor1=conexion1.cursor()
        # se genera el objeto con el que se guardan los datos
sql="""insert into farmacia_probando_programas(nombre, 
                                        version, 
                                        fecha_install, 
                                        pc_id) 
                                        values(%s,%s,%s,%s)"""